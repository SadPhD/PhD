# file with the main algorithm
import numpy as np
from time import process_time
from sortedcontainers import SortedSet

class AlgorithmCOTPOptimal:

    def __init__(self, data, factor_qual, nb_points):
        # data = data[:nb_points+1, :] # uncomment if using the recipe dataset with the number of recipes passed as parameter of the algorithm
        self.column_id = np.ravel(data[:1, 1:-1])
        self.line_id = np.ravel(data[1:, :1])
        data[data == ''] = '0'
        self.data = data[1:, 1:].astype(float)
        self.data = self.data[self.data[:,-1].argsort()[::-1]]
        self.data_attr = self.data[:,:-1].astype(float)
        self.data_tar = np.ravel(self.data[:, -1:]).astype(float)
        self.data_tar_og = self.data_tar.copy()
        self.mean_tar = self.data_tar.mean()
        self.data_tar = self.data_tar - self.mean_tar
        self.obj_count = np.size(self.line_id)
        self.attr_count = np.size(self.column_id)
        self.call_count = 0
        self.factor_qual = factor_qual
        self.top_K = dict()
        self.min_extent = frozenset()
        self.min_threshold = 0
        self.nb_points = nb_points
        self.pos = SortedSet(np.where(self.data_tar > 0)[0].flatten())


    def start(self):
        t = process_time()
        self.initAttrDomains()
        min_pattern = self.computeClosedOnThePositiveIntervalPattern(self.pos)
        extent_neg = SortedSet(list(range(self.obj_count))) - self.pos
        extent_min_patt = self.computeExtentCOTP(min_pattern, extent_neg, 0)
        extent_min_patt.update(self.pos)
        qual = self.computeQuality(extent_min_patt)
        self.top_K.update({frozenset(extent_min_patt):qual})
        self.min_threshold = qual
        self.min_extent = frozenset(extent_min_patt)
        self.call_count += 1
        self.process(min_pattern, extent_min_patt, 0, 0)
        elapsed_time = process_time() - t
        print("Call count : " + str(self.call_count) + " ----- Compression rate : " + str(1- (self.call_count/self.domain_size)) +
        " ------ Runtime : " + str(elapsed_time))
        print(self.toStringTopPatterns())


    def initAttrDomains(self):
        self.domains = np.empty(self.attr_count, dtype=object)
        self.domain_size = 1

        for i in range(0, self.attr_count):
            self.domains[i] = np.sort(np.unique(self.data_attr[:, i]))
            self.domain_size  *= (len(self.domains[i])*(len(self.domains[i])+1)/2)


    def getMinimalPattern(self):
        min_pattern = np.empty([self.attr_count, 2], dtype=float)
        for i in range(0, self.attr_count):
            min_pattern[i][0] = self.domains[i].min()
            min_pattern[i][1] = self.domains[i].max()
        return min_pattern


    def toStringIntervalPattern(self, intervalpattern):
        ip_str = "<"
        for i in range(0, len(intervalpattern)):
            ip_str += "[" + str(intervalpattern[i][0]) + "," + str(intervalpattern[i][1]) + "]"
        return ip_str + ">"


    def computeExtent(self, intervalPattern, eligible, attr):
        new_extent = SortedSet()
        for i in eligible:
            if not(intervalPattern[attr][0] > self.data_attr[i][attr] or intervalPattern[attr][1] < self.data_attr[i][attr]):
                new_extent.add(i)
        return new_extent


    def computeExtentCOTP(self, intervalPattern, eligible, attr):
        new_extent = SortedSet()
        for i in eligible:
            valid = True
            for j in range(attr, self.attr_count):
                if intervalPattern[j][0] > self.data_attr[i][j] or intervalPattern[j][1] < self.data_attr[i][j]:
                    valid = False
                    break
            if valid:
                new_extent.add(i)
        return new_extent


    def toStringExtent(self, extent):
        extent_str = "Extent: {"
        for i in extent: 
            extent_str += str(self.line_id[i]) + ","
        extent_str = extent_str[:-1] + "}"
        return extent_str


    def computeClosedOnThePositiveIntervalPattern(self, extent):
        closed_pattern = np.empty([self.attr_count, 2], dtype=float)
        array_obj =  self.data_attr[list(extent), :]
        array_min = np.amin(array_obj, axis=0)
        array_max = np.amax(array_obj, axis=0)
        closed_pattern[:, 0] = array_min
        closed_pattern[:, 1] = array_max
        return closed_pattern


    def verifyCanonicity(self, intervalpattern, closed_intervalpattern, attr):
        return np.array_equal(intervalpattern[0:attr,:], closed_intervalpattern[0:attr,:])


    def computeQuality(self, extent):
        array_tar = self.data_tar[list(extent)]
        len_ext = len(array_tar)
        return (len_ext**self.factor_qual)*(np.sum(array_tar)/len_ext)


    def computeTightOptimisticEstimate(self, extent):
        for i in range(0,len(extent)):
            array_tar = self.data_tar[extent[0:i+1]]
            len_ext = len(array_tar)
            qual = (len_ext**self.factor_qual)*(np.sum(array_tar)/len_ext)
            if i == 0:
                oe = qual
            else:
                if qual > oe:
                    oe = qual
        return oe
        

    def toStringTopPatterns(self):
        res = "Optimal pattern: \n"
        for i in sorted(self.top_K, key=self.top_K.__getitem__, reverse = True):
            res += "Pattern: " + self.toStringIntervalPattern(self.computeClosedOnThePositiveIntervalPattern(i)) + "\n ----- " + self.toStringExtent(i) + "\n ------------ Quality: " + str(self.top_K[i])
        return res


    def process(self, closed_intervalpattern, extent, attr, pos):
        dict_min_change =  dict()
        for i in range(attr, self.attr_count):
            if closed_intervalpattern[i][0] == closed_intervalpattern[i][1]:
                continue
            if not(pos == 1 and i == attr):
                ip_right = closed_intervalpattern.copy()
                ip_right[i][1] = self.domains[i][np.argwhere(self.domains[i] == closed_intervalpattern[i][1])[0][0]-1]
                if ip_right[i][0] <= ip_right[i][1]:
                    self.call_count += 1
                    new_temp_extent = self.computeExtent(ip_right, extent, i)
                    extent_posit = new_temp_extent.intersection(self.pos)
                    new_closed_ip = self.computeClosedOnThePositiveIntervalPattern(extent_posit)
                    if(self.verifyCanonicity(ip_right, new_closed_ip, i)):
                        extent_neg = new_temp_extent - extent_posit
                        new_extent = self.computeExtentCOTP(new_closed_ip, extent_neg, i)
                        new_extent.update(extent_posit)
                        new_opt_est = self.computeTightOptimisticEstimate(extent_posit)
                        if(new_opt_est > self.min_threshold):
                            dict_min_change.update({frozenset(new_extent):list([new_opt_est, new_closed_ip, i, 0])})
                            new_qual = self.computeQuality(new_extent)
                            if(new_qual > self.min_threshold):
                                self.top_K.update({frozenset(new_extent):new_qual})
                                del self.top_K[self.min_extent]
                                key_min = min(self.top_K.keys(), key=(lambda k: self.top_K[k]))
                                self.min_threshold = self.top_K[key_min]
                                self.min_extent = key_min
            ip_left = closed_intervalpattern.copy()
            ip_left[i][0] = self.domains[i][np.argwhere(self.domains[i] == closed_intervalpattern[i][0])[0][0]+1]
            if ip_left[i][0] <= ip_left[i][1]:
                self.call_count += 1
                new_temp_extent = self.computeExtent(ip_left, extent, i)
                extent_posit = new_temp_extent.intersection(self.pos)
                new_closed_ip = self.computeClosedOnThePositiveIntervalPattern(extent_posit)
                if(self.verifyCanonicity(ip_left, new_closed_ip, i)):
                    extent_neg = new_temp_extent - extent_posit
                    new_extent = self.computeExtentCOTP(new_closed_ip, extent_neg, i)
                    new_extent.update(extent_posit)
                    new_opt_est = self.computeTightOptimisticEstimate(extent_posit)
                    if(new_opt_est > self.min_threshold):
                        dict_min_change.update({frozenset(new_extent):list([new_opt_est, new_closed_ip, i, 1])})
                        new_qual = self.computeQuality(new_extent)
                        if(new_qual > self.min_threshold):
                            self.top_K.update({frozenset(new_extent):new_qual})
                            del self.top_K[self.min_extent]
                            key_min = min(self.top_K.keys(), key=(lambda k: self.top_K[k]))
                            self.min_threshold = self.top_K[key_min]
                            self.min_extent = key_min
        for i in sorted(dict_min_change.items(), key=(lambda k: k[1][0]), reverse = True):
            if(dict_min_change[i[0]][0] > self.min_threshold):
                self.process(dict_min_change[i[0]][1], SortedSet(i[0]), dict_min_change[i[0]][2], dict_min_change[i[0]][3])            