# The main algorithm file for our model
# It discovers the top-K most exceptional pareto fronts according to the chosen quality measure

from subgroup import *
from pareto_front import *
from quality_measures import *
import heapq
import random
import copy
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import csv
import pandas as pd
import time


class EPFAM:

    def __init__(self, data, k, beam_width, search_depth, nb_target, file, loc_factor, min_support, gen_type, gen_factor, skyline):
        self.k = k
        self.beam_width = beam_width
        self.search_depth = search_depth
        self.beam = []
        self.top_k = []
        self.domains = dict()
        self.data = data.iloc[:, 0:-nb_target]
        self.depth = 0
        self.beam_changed = False
        self.targets = data.iloc[:, -nb_target:]
        self.file = file
        self.quality_measure = "HV2"
        self.nb_target = nb_target
        self.loc_factor = loc_factor
        self.min_support = min_support
        self.gen_type = gen_type
        self.gen_factor = gen_factor
        self.skyline = skyline
        self.df_skyline = []
        self.runtime = 0


    def start(self):
        start_time = time.time()
        for column in self.data:
            self.domains.update({column:self.data[column].unique().tolist()})
        self.temp_targets = copy.deepcopy(self.targets)
        normalization_values = dict()
        for column in self.temp_targets:
            normalization_values.update({column:list([self.temp_targets[column].min(),self.temp_targets[column].max()])})
        for col in self.temp_targets:
            if(col[-3:] == "max"):
                self.temp_targets[col] = (self.temp_targets[col] - normalization_values[col][0])/(normalization_values[col][1]-normalization_values[col][0])
                self.temp_targets[col] = 1 - self.temp_targets[col]
            else:
                self.temp_targets[col] = (self.temp_targets[col] - normalization_values[col][0])/(normalization_values[col][1]-normalization_values[col][0])
        self.pareto_front_global = computeParetoFront(self.temp_targets)
        self.targets_pareto_front = self.temp_targets.loc[self.pareto_front_global]

        self.nadir_point = []
        for col in self.temp_targets:
            self.nadir_point.append(self.temp_targets[col].max())

        self.hv_pareto_front = computeQualityHV(self.nadir_point,copy.deepcopy(self.targets_pareto_front))

        if(self.min_support == 0):
            if(self.gen_type == "ent"):
                self.df_skyline = pd.DataFrame(columns=['sg','extent','dist','ent','loc'])
            else:
                self.df_skyline = pd.DataFrame(columns=['sg','extent','dist','cov','loc'])
        else:
            self.df_skyline = pd.DataFrame(columns=['sg','extent','dist','loc'])

        self.process()
        self.runtime = round(time.time() - start_time, 2)
        
        if(self.skyline == 1):
            self.subgroupsSkylineToCSV()
            self.SkylineToCSV()
        else:
            self.subgroupsToCSV()
            self.generatePlot()
            self.generatePF()


    # We generate files to build plots that show the exceptional approximation found
    def generatePlot(self):
        cmpt = 0
        for sg in heapq.nlargest(self.k,self.top_k):
            cmpt += 1
            column_grp = list()
            column_grp_weight = list()
            current_targets = copy.deepcopy(self.temp_targets)
            current_targets = current_targets[current_targets.index.isin(sg[2])]
            current_pf = computeParetoFront(current_targets)
            current_targets_bis = copy.deepcopy(self.temp_targets)
            for elem in current_targets_bis.index:
                if(elem in current_pf):
                    column_grp.append("PF_model")
                elif(elem in self.pareto_front_global):
                    column_grp.append("PF_true")
                elif(elem in sg[2]):
                    column_grp.append("SG")
                else:
                    column_grp.append("ND")
            current_targets_bis['label'] = np.array(column_grp)
            columns = list(current_targets_bis)
            current_targets_bis = current_targets_bis.sort_values('label')
            current_targets_bis.to_csv("../res/"+self.file+"_"+self.quality_measure+"_"+str(self.loc_factor)+"_"+str(self.min_support)+"_"+str(self.beam_width)+"_"+str(self.search_depth)+"_rank"+str(cmpt)+"_results_method.csv", sep=',', index = False)


    # We generate PF_true files to build plots
    def generatePF(self):
        column_grp = list()
        current_targets = copy.deepcopy(self.temp_targets)
        for elem in current_targets.index:
            if(elem in self.pareto_front_global):
                column_grp.append("PF_true")
            else:
                column_grp.append("ND")
        current_targets['label'] = np.array(column_grp)
        columns = list(current_targets)
        current_targets = current_targets.sort_values('label')
        current_targets.to_csv("../res/"+self.file+"_PF_true.csv", sep=',', index = False)


    def subgroupsToCSV(self):
        cmpt = 0
        for elem in heapq.nlargest(self.k,self.top_k):
            cmpt += 1
            if(self.min_support == 0):
                if(self.gen_type == "ent"):
                    lst_row = [self.file,self.beam_width,self.search_depth,self.quality_measure,self.loc_factor,self.min_support,self.gen_type,self.gen_factor,self.skyline,self.runtime,cmpt,str(elem[3].get()),str(elem[2]),str(elem[0])]
                else:
                    lst_row = [self.file,self.beam_width,self.search_depth,self.quality_measure,self.loc_factor,self.min_support,self.gen_type,self.gen_factor,self.skyline,self.runtime,cmpt,str(elem[3].get()),str(elem[2]),str(elem[0])]
            else:
                lst_row = [self.file,self.beam_width,self.search_depth,self.quality_measure,self.loc_factor,self.min_support,self.gen_type,self.gen_factor,self.skyline,self.runtime,cmpt,str(elem[3].get()),str(elem[2]),str(elem[0])]
            with open("../res/results_experiments.csv", 'a+') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow(lst_row)


    def subgroupsSkylineToCSV(self):
        cmpt = 0
        for index, row in self.df_skyline.iterrows():
            cmpt += 1
            if(self.min_support == 0):
                if(self.gen_type == "ent"):
                    lst_row = [self.file,self.beam_width,self.search_depth,self.quality_measure,self.loc_factor,self.min_support,self.gen_type,self.gen_factor,self.skyline,self.runtime,cmpt,str(row['sg'].get()),str(row['extent']),str(row['dist']),str(row['ent']),str(row['loc'])]
                else:
                    lst_row = [self.file,self.beam_width,self.search_depth,self.quality_measure,self.loc_factor,self.min_support,self.gen_type,self.gen_factor,self.skyline,self.runtime,cmpt,str(row['sg'].get()),str(row['extent']),str(row['dist']),str(row['cov']),str(row['loc'])]
            else:
                lst_row = [self.file,self.beam_width,self.search_depth,self.quality_measure,self.loc_factor,self.min_support,self.gen_type,self.gen_factor,self.skyline,self.runtime,cmpt,str(row['sg'].get()),str(row['extent']),str(row['dist']),str(self.min_support),str(row['loc'])]
            with open("../res/results_experiments_skyline.csv", 'a+') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow(lst_row)

    def SkylineToCSV(self):
        df_skyline = pd.DataFrame(columns=['loc','qual'])
        for index, row in self.df_skyline.iterrows():
           df_skyline.loc[len(df_skyline)] = [row['loc'],row['dist']]
        df_skyline.to_csv("../res/"+self.file+"_Skyline.csv", sep=',', index = False)


    # A slightly modified version of beam search
    def process(self):
        # If we want top-K subgroups
        if(self.skyline == 0):
            if(self.depth == 0):
                self.depth += 1
                for var in self.domains:
                    for val in self.domains[var]:
                        current_sg = subgroup(var,val)
                        current_ext = current_sg.computeExtent(self.data)
                        duplicate = False
                        duplicate_top_k = False
                        if(len(list(set(self.pareto_front_global).intersection(current_ext)))/len(self.pareto_front_global) > self.min_support):
                            for elem in self.beam:
                                if(set(elem[2]) == set(current_ext)):
                                    duplicate = True
                                    break
                            if(duplicate == False):
                                current_targets = copy.deepcopy(self.temp_targets)
                                current_targets = current_targets[current_targets.index.isin(current_ext)] 
                                current_pf = computeParetoFront(current_targets)
                                targets_current_pf = copy.deepcopy(self.temp_targets).loc[current_pf]
                                qual_pareto = computeQualityHV(self.nadir_point,targets_current_pf)/self.hv_pareto_front
                                qual = computeQualityGlobal(qual_pareto,self.loc_factor,self.min_support,self.gen_type,self.gen_factor,self.skyline,self.pareto_front_global,current_ext,len(self.data.index),len(current_ext))
                                if(len(self.beam) < self.beam_width):
                                    heapq.heappush(self.beam,(qual, id(current_sg), current_ext, current_sg))
                                elif(qual >= self.beam[0][0]):
                                    heapq.heappop(self.beam)
                                    heapq.heappush(self.beam,(qual, id(current_sg), current_ext, current_sg))
                                if(len(self.top_k) < self.k):
                                    heapq.heappush(self.top_k,(qual, id(current_sg), current_ext, current_sg))
                                elif(qual >= self.top_k[0][0]):
                                    for elem in self.top_k:
                                        if(set(elem[2]) == set(current_ext)):
                                            duplicate_top_k = True
                                            break
                                    if(duplicate_top_k == False):
                                        heapq.heappop(self.top_k)
                                        heapq.heappush(self.top_k,(qual, id(current_sg), current_ext, current_sg))
            while(self.depth < self.search_depth):
                beam_temp = copy.deepcopy(self.beam)
                self.beam = []
                for subg in beam_temp:
                    subg_b = copy.deepcopy(subg)
                    if(subg_b[3].size() == self.depth):
                        for var in self.domains:
                            if(var not in list(subg_b[3].get().keys())):
                                for val in self.domains[var]:
                                    current_sg = copy.deepcopy(subg_b[3])
                                    current_sg.add(var,val)
                                    current_ext = current_sg.computeExtent(self.data)
                                    duplicate = False
                                    duplicate_top_k = False
                                    if(len(list(set(self.pareto_front_global).intersection(current_ext)))/len(self.pareto_front_global) > self.min_support):
                                        for elem in self.beam:
                                            if(set(elem[2]) == set(current_ext)):
                                                duplicate = True
                                                break
                                        if(duplicate == False):
                                            current_targets = copy.deepcopy(self.temp_targets)
                                            current_targets = current_targets[current_targets.index.isin(current_ext)] 
                                            current_pf = computeParetoFront(current_targets)
                                            targets_current_pf = copy.deepcopy(self.temp_targets).loc[current_pf]
                                            qual_pareto = computeQualityHV(self.nadir_point,targets_current_pf)/self.hv_pareto_front
                                            qual = computeQualityGlobal(qual_pareto,self.loc_factor,self.min_support,self.gen_type,self.gen_factor,self.skyline,self.pareto_front_global,current_ext,len(self.data.index),len(current_ext))
                                            if(len(self.beam) < self.beam_width):
                                                heapq.heappush(self.beam,(qual, id(current_sg), current_ext, current_sg))
                                            elif(qual >= self.beam[0][0]):
                                                heapq.heappop(self.beam)
                                                heapq.heappush(self.beam,(qual, id(current_sg), current_ext, current_sg))
                                            if(len(self.top_k) < self.k):
                                                heapq.heappush(self.top_k,(qual, id(current_sg), current_ext, current_sg))
                                            elif(qual >= self.top_k[0][0]):
                                                for elem in self.top_k:
                                                    if(set(elem[2]) == set(current_ext)):
                                                        duplicate_top_k = True
                                                        break
                                                if(duplicate_top_k == False):
                                                    heapq.heappop(self.top_k)
                                                    heapq.heappush(self.top_k,(qual, id(current_sg), current_ext, current_sg))
                self.depth += 1
        # If we want the skyline with no fixed beam width
        elif(self.beam_width == 0):
            if(self.depth == 0):
                if(self.min_support == 0):
                    if(self.gen_type == "ent"):
                        df_sg = pd.DataFrame(columns=['sg','extent','dist','ent','loc'])
                    else:
                        df_sg = pd.DataFrame(columns=['sg','extent','dist','cov','loc'])
                else:
                    df_sg = pd.DataFrame(columns=['sg','extent','dist','loc'])
                self.depth += 1
                for var in self.domains:
                    for val in self.domains[var]:
                        current_sg = subgroup(var,val)
                        current_ext = current_sg.computeExtent(self.data)
                        duplicate = False
                        duplicate_top_k = False
                        if(len(list(set(self.pareto_front_global).intersection(current_ext)))/len(self.pareto_front_global) > self.min_support):
                            for index, row in df_sg.iterrows():
                                if(set(row['extent']) == set(current_ext)):
                                    duplicate = True
                                    break
                            if(duplicate == False):
                                current_targets = copy.deepcopy(self.temp_targets)
                                current_targets = current_targets[current_targets.index.isin(current_ext)]
                                current_pf = computeParetoFront(current_targets)
                                targets_current_pf = copy.deepcopy(self.temp_targets).loc[current_pf]
                                qual_pareto = computeQualityHV(self.nadir_point,targets_current_pf)/self.hv_pareto_front
                                qual = computeQualityGlobal(qual_pareto,self.loc_factor,self.min_support,self.gen_type,self.gen_factor,self.skyline,self.pareto_front_global,current_ext,len(self.data.index),len(current_ext))
                                if(len(qual)== 2):
                                    df_sg.loc[len(df_sg)] = [current_sg,current_ext,-qual[0],-qual[1]]
                                else:
                                    df_sg.loc[len(df_sg)] = [current_sg,current_ext,-qual[0],-qual[1],-qual[2]]
                if(len(qual)== 2):
                    pf_current_lvl = computeParetoFront(df_sg.iloc[:, -2:])
                else:
                    pf_current_lvl = computeParetoFront(df_sg.iloc[:, -3:])
                df_sg_next_lvl = copy.deepcopy(df_sg)
                df_sg_next_lvl = df_sg_next_lvl[df_sg_next_lvl.index.isin(pf_current_lvl)]
                self.df_skyline = pd.concat([self.df_skyline,df_sg_next_lvl], ignore_index = True)
            while(self.depth < self.search_depth):
                if(self.min_support == 0):
                    if(self.gen_type == "ent"):
                        df_sg = pd.DataFrame(columns=['sg','extent','dist','ent','loc'])
                    else:
                        df_sg = pd.DataFrame(columns=['sg','extent','dist','cov','loc'])
                else:
                    df_sg = pd.DataFrame(columns=['sg','extent','dist','loc'])
                for index, row in df_sg_next_lvl.iterrows():
                    if(row['sg'].size() == self.depth):
                        for var in self.domains:
                            if(var not in list(row['sg'].get().keys())):
                                for val in self.domains[var]:
                                    current_sg = copy.deepcopy(row['sg'])
                                    current_sg.add(var,val)
                                    current_ext = current_sg.computeExtent(self.data)
                                    duplicate = False
                                    duplicate_top_k = False
                                    if(len(list(set(self.pareto_front_global).intersection(current_ext)))/len(self.pareto_front_global) > self.min_support):
                                        for index_b, row_b in df_sg.iterrows():
                                            if(set(row_b['extent']) == set(current_ext)):
                                                duplicate = True
                                                break
                                        if(duplicate == False):
                                            current_targets = copy.deepcopy(self.temp_targets)
                                            current_targets = current_targets[current_targets.index.isin(current_ext)]
                                            current_pf = computeParetoFront(current_targets)
                                            targets_current_pf = copy.deepcopy(self.temp_targets).loc[current_pf]
                                            qual_pareto = computeQualityHV(self.nadir_point,targets_current_pf)/self.hv_pareto_front
                                            qual = computeQualityGlobal(qual_pareto,self.loc_factor,self.min_support,self.gen_type,self.gen_factor,self.skyline,self.pareto_front_global,current_ext,len(self.data.index),len(current_ext))
                                            if(len(qual)== 2):
                                                df_sg.loc[len(df_sg)] = [current_sg,current_ext,-qual[0],-qual[1]]
                                            else:
                                                df_sg.loc[len(df_sg)] = [current_sg,current_ext,-qual[0],-qual[1],-qual[2]]
                if(len(qual)== 2):
                    pf_current_lvl = computeParetoFront(df_sg.iloc[:, -2:])
                else:
                    pf_current_lvl = computeParetoFront(df_sg.iloc[:, -3:])
                df_sg_next_lvl = copy.deepcopy(df_sg)
                df_sg_next_lvl = df_sg_next_lvl[df_sg_next_lvl.index.isin(pf_current_lvl)]
                self.df_skyline = pd.concat([self.df_skyline,df_sg_next_lvl], ignore_index = True)
                self.depth += 1
            if(len(qual)== 2):
                    pf_current_lvl = computeParetoFront(self.df_skyline.iloc[:, -2:])
            else:
                pf_current_lvl = computeParetoFront(self.df_skyline.iloc[:, -3:])
            self.df_skyline = self.df_skyline[self.df_skyline.index.isin(pf_current_lvl)]
            self.df_skyline['extent_bis'] = self.df_skyline.extent.map(sorted).astype(str)
            self.df_skyline = self.df_skyline.drop_duplicates('extent_bis',keep='last').drop('extent_bis',axis=1)
        # If we want the skyline with a fixed beam width
        else:
            if(self.depth == 0):
                if(self.min_support == 0):
                    if(self.gen_type == "ent"):
                        df_sg = pd.DataFrame(columns=['sg','extent','dist','ent','loc'])
                    else:
                        df_sg = pd.DataFrame(columns=['sg','extent','dist','cov','loc'])
                else:
                    df_sg = pd.DataFrame(columns=['sg','extent','dist','loc'])
                self.depth += 1
                for var in self.domains:
                    for val in self.domains[var]:
                        current_sg = subgroup(var,val)
                        current_ext = current_sg.computeExtent(self.data)
                        duplicate = False
                        duplicate_top_k = False
                        if(len(list(set(self.pareto_front_global).intersection(current_ext)))/len(self.pareto_front_global) > self.min_support):
                            for index, row in df_sg.iterrows():
                                if(set(row['extent']) == set(current_ext)):
                                    duplicate = True
                                    break
                            if(duplicate == False):
                                current_targets = copy.deepcopy(self.temp_targets)
                                current_targets = current_targets[current_targets.index.isin(current_ext)]
                                current_pf = computeParetoFront(current_targets)
                                targets_current_pf = copy.deepcopy(self.temp_targets).loc[current_pf]
                                qual_pareto = computeQualityHV(self.nadir_point,targets_current_pf)/self.hv_pareto_front
                                qual = computeQualityGlobal(qual_pareto,self.loc_factor,self.min_support,self.gen_type,self.gen_factor,self.skyline,self.pareto_front_global,current_ext,len(self.data.index),len(current_ext))
                                if(len(qual)== 2):
                                    df_sg.loc[len(df_sg)] = [current_sg,current_ext,-qual[0],-qual[1]]
                                else:
                                    df_sg.loc[len(df_sg)] = [current_sg,current_ext,-qual[0],-qual[1],-qual[2]]
                if(len(qual)== 2):
                    pf_current_lvl = computeParetoFront(df_sg.iloc[:, -2:])
                else:
                    pf_current_lvl = computeParetoFront(df_sg.iloc[:, -3:])
                df_pareto_front_lvl = copy.deepcopy(df_sg)
                df_pareto_front_lvl = df_pareto_front_lvl[df_pareto_front_lvl.index.isin(pf_current_lvl)]
                self.df_skyline = pd.concat([self.df_skyline,df_pareto_front_lvl], ignore_index = True)
                if(len(df_pareto_front_lvl) > self.beam_width):
                    df_sg_next_lvl = copy.deepcopy(df_pareto_front_lvl).sample(n = self.beam_width,random_state=1)
                else:
                    df_sg_next_lvl = copy.deepcopy(df_pareto_front_lvl)
            while(self.depth < self.search_depth):
                if(self.min_support == 0):
                    if(self.gen_type == "ent"):
                        df_sg = pd.DataFrame(columns=['sg','extent','dist','ent','loc'])
                    else:
                        df_sg = pd.DataFrame(columns=['sg','extent','dist','cov','loc'])
                else:
                    df_sg = pd.DataFrame(columns=['sg','extent','dist','loc'])
                for index, row in df_sg_next_lvl.iterrows():
                    if(row['sg'].size() == self.depth):
                        for var in self.domains:
                            if(var not in list(row['sg'].get().keys())):
                                for val in self.domains[var]:
                                    current_sg = copy.deepcopy(row['sg'])
                                    current_sg.add(var,val)
                                    current_ext = current_sg.computeExtent(self.data)
                                    duplicate = False
                                    duplicate_top_k = False
                                    if(len(list(set(self.pareto_front_global).intersection(current_ext)))/len(self.pareto_front_global) > self.min_support):
                                        for index_b, row_b in df_sg.iterrows():
                                            if(set(row_b['extent']) == set(current_ext)):
                                                duplicate = True
                                                break
                                        if(duplicate == False):
                                            current_targets = copy.deepcopy(self.temp_targets)
                                            current_targets = current_targets[current_targets.index.isin(current_ext)]
                                            current_pf = computeParetoFront(current_targets)
                                            targets_current_pf = copy.deepcopy(self.temp_targets).loc[current_pf]
                                            qual_pareto = computeQualityHV(self.nadir_point,targets_current_pf)/self.hv_pareto_front
                                            qual = computeQualityGlobal(qual_pareto,self.loc_factor,self.min_support,self.gen_type,self.gen_factor,self.skyline,self.pareto_front_global,current_ext,len(self.data.index),len(current_ext))
                                            if(len(qual)== 2):
                                                df_sg.loc[len(df_sg)] = [current_sg,current_ext,-qual[0],-qual[1]]
                                            else:
                                                df_sg.loc[len(df_sg)] = [current_sg,current_ext,-qual[0],-qual[1],-qual[2]]
                if(len(qual)== 2):
                    pf_current_lvl = computeParetoFront(df_sg.iloc[:, -2:])
                else:
                    pf_current_lvl = computeParetoFront(df_sg.iloc[:, -3:])
                df_pareto_front_lvl = copy.deepcopy(df_sg)
                df_pareto_front_lvl = df_pareto_front_lvl[df_pareto_front_lvl.index.isin(pf_current_lvl)]
                self.df_skyline = pd.concat([self.df_skyline,df_pareto_front_lvl], ignore_index = True)
                if(len(df_pareto_front_lvl) > self.beam_width):
                    df_sg_next_lvl = copy.deepcopy(df_pareto_front_lvl).sample(n = self.beam_width,random_state=1)
                else:
                    df_sg_next_lvl = copy.deepcopy(df_pareto_front_lvl)
                self.depth += 1
            if(len(qual)== 2):
                    pf_current_lvl = computeParetoFront(self.df_skyline.iloc[:, -2:])
            else:
                pf_current_lvl = computeParetoFront(self.df_skyline.iloc[:, -3:])
            self.df_skyline = self.df_skyline[self.df_skyline.index.isin(pf_current_lvl)]
            self.df_skyline['extent_bis'] = self.df_skyline.extent.map(sorted).astype(str)
            self.df_skyline = self.df_skyline.drop_duplicates('extent_bis',keep='last').drop('extent_bis',axis=1)

                    