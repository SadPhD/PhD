import statistics
import math
import numpy as np
from hv import *

# Quality measures can be added in the computeQuality function (implemented measures are HD, AHD, and MHD)
# The quality measure is passed as parameter to the function
def computeQuality(quality_measure, pf_data, pf_sg, targets_pf_data, targets_pf_sg):
    if(quality_measure == "MHD"):
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
        return(median_distance)
    elif(quality_measure == "AHD"):
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
        return(mean_distance)
    else:
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
        return(max_distance)

# Computes the HV of a given Pareto front
def computeQualityHV(nadir_point,targets_current_pf):
    hv = HyperVolume(nadir_point)
    targets_current_pf = targets_current_pf.drop_duplicates()
    front = targets_current_pf.values.tolist()
    volume = hv.compute(front)
    return(volume)

# Computes the overall quality of the subgroup (i.e., includes its quality and its relevance)
def computeQualityGlobal(qual,loc_factor,min_support,gen_type,gen_factor,skyline,pf_data,extent_sg,size_data,size_sg):
    if(min_support == 0):
        if(skyline == 1):
            len_common = len(list(set(pf_data).intersection(extent_sg)))
            len_pf_data = len(pf_data)
            loc = (1-(size_sg/size_data))**loc_factor
            if(gen_type == "ent"):
                if(len_common != len_pf_data):
                    ent = (-((len_common/len_pf_data)*math.log2(len_common/len_pf_data))-(((len_pf_data-len_common)/len_pf_data)*math.log2((len_pf_data-len_common)/len_pf_data)))**gen_factor
                    quality = [qual,ent,loc]
                else:
                    quality = [qual,0,loc]
            else:
                cov = (len_common/len_pf_data)**gen_factor
                quality = [qual,cov,loc]
        else:
            len_common = len(list(set(pf_data).intersection(extent_sg)))
            len_pf_data = len(pf_data)
            loc = (1-(size_sg/size_data))**loc_factor
            if(gen_type == "ent"):
                if(len_common != len_pf_data):
                    ent = (-((len_common/len_pf_data)*math.log2(len_common/len_pf_data))-(((len_pf_data-len_common)/len_pf_data)*math.log2((len_pf_data-len_common)/len_pf_data)))**gen_factor
                    if(qual < 0):
                        quality = qual*(1-(ent*loc))
                    else:
                        quality = qual*ent*loc
                else:
                    quality = 0
            else:
                cov = (len_common/len_pf_data)**gen_factor
                if(qual < 0):
                    quality = qual*(1-(cov*loc))
                else:
                    quality = qual*cov*loc
    else:
        if(skyline == 1):
            loc = (1-(size_sg/size_data))**loc_factor
            quality = [qual,loc]
        else:
            loc = (1-(size_sg/size_data))**loc_factor
            if(qual < 0):
                quality = qual*(1-loc)
            else:
                quality = qual*loc
    return(quality)