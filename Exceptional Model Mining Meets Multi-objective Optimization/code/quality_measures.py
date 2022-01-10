# Quality measures can be added in the computeQuality function
# The quality measure is passed as parameter to the function
import statistics
import math
import numpy as np

def computeQuality(quality_measure, pf_data, pf_sg, targets_pf_data, targets_pf_sg, extent_sg, size_data, size_sg):
    if(quality_measure == "MHD"):
        len_common = len(list(set(pf_data).intersection(extent_sg)))
        len_pf_data = len(pf_data)
        if(len_common != len_pf_data):
            pf_only_sg = list(set(pf_sg) - set(pf_data))
            targets_only_pf_sg = targets_pf_sg.loc[pf_only_sg]
            pf_only_data = list(set(pf_data) - set(pf_sg))
            targets_only_pf_data = targets_pf_data.loc[pf_only_data]
            list_dist_sg = list()
            median_pf_sg = 0
            median_pf_data = 0
            if(len(targets_only_pf_sg) > 0):
                for i in range(0, len(targets_only_pf_sg.index)):
                    current_obj = targets_only_pf_sg.iloc[i,:]
                    current_obj_lst = list(current_obj)
                    arr_current_obj = np.array(current_obj_lst)
                    for j in range(0, len(targets_pf_data.index)):
                        next_obj = targets_pf_data.iloc[j,:]
                        if(j == 0):
                            current_low = 1000000000
                        next_obj_lst = list(next_obj)
                        arr_next_obj = np.array(next_obj_lst)
                        dist = np.linalg.norm(arr_current_obj-arr_next_obj)
                        if(dist < current_low):
                            current_low = dist
                    list_dist_sg.append(current_low)
                median_pf_sg = statistics.median(list_dist_sg)
            list_dist_data = list()
            if(len(targets_only_pf_data) > 0):
                for i in range(0, len(targets_only_pf_data.index)):
                    current_obj = targets_only_pf_data.iloc[i,:]
                    current_obj_lst = list(current_obj)
                    arr_current_obj = np.array(current_obj_lst)
                    for j in range(0, len(targets_pf_sg.index)):
                        next_obj = targets_pf_sg.iloc[j,:]
                        if(j == 0):
                            current_low = 1000000000
                        next_obj_lst = list(next_obj)
                        arr_next_obj = np.array(next_obj_lst)
                        dist = np.linalg.norm(arr_current_obj-arr_next_obj)
                        if(dist < current_low):
                            current_low = dist
                    list_dist_data.append(current_low)
                median_pf_data = statistics.median(list_dist_data)
            median_distance = max(median_pf_sg, median_pf_data)
            loc = 1-(size_sg/size_data)
            entropy = -((len_common/len_pf_data)*math.log2(len_common/len_pf_data))-(((len_pf_data-len_common)/len_pf_data)*math.log2((len_pf_data-len_common)/len_pf_data))
            quality = median_distance*entropy*loc
            return(quality)
        else:
            return(0)
    elif(quality_measure == "AHD"):
        len_common = len(list(set(pf_data).intersection(extent_sg)))
        len_pf_data = len(pf_data)
        if(len_common != len_pf_data):
            pf_only_sg = list(set(pf_sg) - set(pf_data))
            targets_only_pf_sg = targets_pf_sg.loc[pf_only_sg]
            pf_only_data = list(set(pf_data) - set(pf_sg))
            targets_only_pf_data = targets_pf_data.loc[pf_only_data]
            list_dist_sg = list()
            mean_pf_sg = 0
            mean_pf_data = 0
            if(len(targets_only_pf_sg) > 0):
                for i in range(0, len(targets_only_pf_sg.index)):
                    current_obj = targets_only_pf_sg.iloc[i,:]
                    current_obj_lst = list(current_obj)
                    arr_current_obj = np.array(current_obj_lst)
                    for j in range(0, len(targets_pf_data.index)):
                        next_obj = targets_pf_data.iloc[j,:]
                        if(j == 0):
                            current_low = 1000000000
                        next_obj_lst = list(next_obj)
                        arr_next_obj = np.array(next_obj_lst)
                        dist = np.linalg.norm(arr_current_obj-arr_next_obj)
                        if(dist < current_low):
                            current_low = dist
                    list_dist_sg.append(current_low)
                mean_pf_sg = statistics.mean(list_dist_sg)
            list_dist_data = list()
            if(len(targets_only_pf_data) > 0):
                for i in range(0, len(targets_only_pf_data.index)):
                    current_obj = targets_only_pf_data.iloc[i,:]
                    current_obj_lst = list(current_obj)
                    arr_current_obj = np.array(current_obj_lst)
                    for j in range(0, len(targets_pf_sg.index)):
                        next_obj = targets_pf_sg.iloc[j,:]
                        if(j == 0):
                            current_low = 1000000000
                        next_obj_lst = list(next_obj)
                        arr_next_obj = np.array(next_obj_lst)
                        dist = np.linalg.norm(arr_current_obj-arr_next_obj)
                        if(dist < current_low):
                            current_low = dist
                    list_dist_data.append(current_low)
                mean_pf_data = statistics.mean(list_dist_data)
            mean_distance = max(mean_pf_sg, mean_pf_data)
            loc = 1-(size_sg/size_data)
            entropy = -((len_common/len_pf_data)*math.log2(len_common/len_pf_data))-(((len_pf_data-len_common)/len_pf_data)*math.log2((len_pf_data-len_common)/len_pf_data))
            quality = mean_distance*entropy*loc
            return(quality)
        else:
            return(0)
    else:
        len_common = len(list(set(pf_data).intersection(extent_sg)))
        len_pf_data = len(pf_data)
        if(len_common != len_pf_data):
            pf_only_sg = list(set(pf_sg) - set(pf_data))
            targets_only_pf_sg = targets_pf_sg.loc[pf_only_sg]
            pf_only_data = list(set(pf_data) - set(pf_sg))
            targets_only_pf_data = targets_pf_data.loc[pf_only_data]
            list_dist_sg = list()
            max_pf_sg = 0
            max_pf_data = 0
            if(len(targets_only_pf_sg) > 0):
                for i in range(0, len(targets_only_pf_sg.index)):
                    current_obj = targets_only_pf_sg.iloc[i,:]
                    current_obj_lst = list(current_obj)
                    arr_current_obj = np.array(current_obj_lst)
                    for j in range(0, len(targets_pf_data.index)):
                        next_obj = targets_pf_data.iloc[j,:]
                        if(j == 0):
                            current_low = 1000000000
                        next_obj_lst = list(next_obj)
                        arr_next_obj = np.array(next_obj_lst)
                        dist = np.linalg.norm(arr_current_obj-arr_next_obj)
                        if(dist < current_low):
                            current_low = dist
                    list_dist_sg.append(current_low)
                max_pf_sg = max(list_dist_sg)
            list_dist_data = list()
            if(len(targets_only_pf_data) > 0):
                for i in range(0, len(targets_only_pf_data.index)):
                    current_obj = targets_only_pf_data.iloc[i,:]
                    current_obj_lst = list(current_obj)
                    arr_current_obj = np.array(current_obj_lst)
                    for j in range(0, len(targets_pf_sg.index)):
                        next_obj = targets_pf_sg.iloc[j,:]
                        if(j == 0):
                            current_low = 1000000000
                        next_obj_lst = list(next_obj)
                        arr_next_obj = np.array(next_obj_lst)
                        dist = np.linalg.norm(arr_current_obj-arr_next_obj)
                        if(dist < current_low):
                            current_low = dist
                    list_dist_data.append(current_low)
                max_pf_data = max(list_dist_data)
            max_distance = max(max_pf_sg, max_pf_data)
            loc = 1-(size_sg/size_data)
            entropy = -((len_common/len_pf_data)*math.log2(len_common/len_pf_data))-(((len_pf_data-len_common)/len_pf_data)*math.log2((len_pf_data-len_common)/len_pf_data))
            quality = max_distance*entropy*loc
            return(quality)
        else:
            return(0)
