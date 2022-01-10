# The main algorithm file for our model
# It discovers the top-K best most exceptional pareto fronts according to the chosen quality measure

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


class beam_search:

    def __init__(self, data, k, beam_width, search_depth, nb_target, quality_measure, file):
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
        self.quality_measure = quality_measure
        self.nb_target = nb_target


    def start(self):
        for column in self.data:
            self.domains.update({column:self.data[column].unique().tolist()})
        self.temp_targets = copy.deepcopy(self.targets)
        normalization_values = dict()
        for column in self.temp_targets:
            normalization_values.update({column:list([self.temp_targets[column].min(),self.temp_targets[column].max()])})
        for col in self.temp_targets:
            self.temp_targets[col] = (self.temp_targets[col] - normalization_values[col][0])/(normalization_values[col][1]-normalization_values[col][0])
        self.pareto_front_global = computeParetoFront(self.temp_targets)
        self.targets_pareto_front = self.temp_targets.loc[self.pareto_front_global]
        self.temp_data_pareto_front_global = self.data.loc[self.pareto_front_global]
        self.process()
        self.subgroupsToCSV()
        self.generatePlot()
        self.generatePF()

    # We generate plots that show the exceptional model found and deviation created by the absence of the subgroup
    def generatePlot(self):
        cmpt = 0
        for sg in heapq.nlargest(self.k,self.top_k):
            cmpt += 1
            column_grp = list()
            column_grp_weight = list()
            current_targets = copy.deepcopy(self.temp_targets)
            current_targets = current_targets[~current_targets.index.isin(sg[2])]
            current_pf = computeParetoFront(current_targets)
            current_targets_bis = copy.deepcopy(self.targets)
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
            if(len(pd.unique(current_targets_bis['label'])) == 3):
                my_palette = ["lightgray", "seagreen","red"]
            else:
                my_palette = ["lightgray", "seagreen","red","orange"]
            if(self.nb_target == 2):
                myplot = sns.scatterplot(x=columns[0], y=columns[1],data=current_targets_bis,hue=current_targets_bis.label.tolist(), palette=["lightgray", "seagreen","red","orange"])
                myplot.set_xlabel(columns[0],fontsize=10)
                myplot.set_ylabel(columns[1],fontsize=10)
                myplot.tick_params(labelsize=10)
                plt.legend(fontsize='medium', title_fontsize='10', loc = "upper right")
                myplot.figure.savefig("../res/"+self.file+"_"+self.quality_measure+"_"+str(self.beam_width)+"_"+str(self.search_depth)+"_rank"+str(cmpt)+"_results.png")
                plt.close()
            else:
                myplot = sns.scatterplot(x=columns[0], y=columns[1],data=current_targets_bis,hue=current_targets_bis.label.tolist(), palette=["lightgray", "seagreen","red","orange"])
                myplot.set_xlabel(columns[0],fontsize=10)
                myplot.set_ylabel(columns[1],fontsize=10)
                myplot.tick_params(labelsize=10)
                plt.legend(fontsize='medium', title_fontsize='10', loc = "upper right")
                myplot.figure.savefig("../res/"+self.file+"_"+self.quality_measure+"_"+str(self.beam_width)+"_"+str(self.search_depth)+"_rank"+str(cmpt)+"_results_"+columns[0]+"_"+columns[1]+".png")
                plt.close()
                myplot = sns.scatterplot(x=columns[0], y=columns[2],data=current_targets_bis,hue=current_targets_bis.label.tolist(), palette=["lightgray", "seagreen","red","orange"])
                myplot.set_xlabel(columns[0],fontsize=10)
                myplot.set_ylabel(columns[2],fontsize=10)
                myplot.tick_params(labelsize=10)
                plt.legend(fontsize='medium', title_fontsize='10', loc = "upper right")
                myplot.figure.savefig("../res/"+self.file+"_"+self.quality_measure+"_"+str(self.beam_width)+"_"+str(self.search_depth)+"_rank"+str(cmpt)+"_results_"+columns[0]+"_"+columns[2]+".png")
                plt.close()
                myplot = sns.scatterplot(x=columns[1], y=columns[2],data=current_targets_bis,hue=current_targets_bis.label.tolist(), palette=["lightgray", "seagreen","red","orange"])
                myplot.set_xlabel(columns[1],fontsize=10)
                myplot.set_ylabel(columns[2],fontsize=10)
                myplot.tick_params(labelsize=10)
                plt.legend(fontsize='medium', title_fontsize='10', loc = "upper right")
                myplot.figure.savefig("../res/"+self.file+"_"+self.quality_measure+"_"+str(self.beam_width)+"_"+str(self.search_depth)+"_rank"+str(cmpt)+"_results_"+columns[1]+"_"+columns[2]+".png")
                plt.close()


    # We generate PF_true plots with up to 3 objectives, for more, it needs to be modified
    def generatePF(self):
        column_grp = list()
        current_targets = copy.deepcopy(self.targets)
        for elem in current_targets.index:
            if(elem in self.pareto_front_global):
                column_grp.append("PF_true")
            else:
                column_grp.append("ND")
        current_targets['label'] = np.array(column_grp)
        columns = list(current_targets)
        current_targets = current_targets.sort_values('label')
        current_targets.to_csv("../res/"+self.file+"_PF_true.csv", sep=',', index = False)
        if(self.nb_target == 2):
            myplot = sns.scatterplot(x=columns[0], y=columns[1],data=current_targets,hue=current_targets.label.tolist(), palette=["lightgray","red"])
            myplot.set_xlabel(columns[0],fontsize=10)
            myplot.set_ylabel(columns[1],fontsize=10)
            myplot.tick_params(labelsize=10)
            plt.legend(fontsize='medium', title_fontsize='10', loc = "upper right")
            myplot.figure.savefig("../res/"+self.file+"_PF_true.png")
            plt.close()
        else:
            myplot = sns.scatterplot(x=columns[0], y=columns[1],data=current_targets,hue=current_targets.label.tolist(), palette=["lightgray","red"])
            myplot.set_xlabel(columns[0],fontsize=10)
            myplot.set_ylabel(columns[1],fontsize=10)
            myplot.tick_params(labelsize=10)
            plt.legend(fontsize='medium', title_fontsize='10', loc = "upper right")
            myplot.figure.savefig("../res/"+self.file+"_"+str(columns[0])+"_"+str(columns[1])+"_PF_true.png")
            plt.close()
            myplot = sns.scatterplot(x=columns[0], y=columns[2],data=current_targets,hue=current_targets.label.tolist(), palette=["lightgray","red"])
            myplot.set_xlabel(columns[0],fontsize=10)
            myplot.set_ylabel(columns[2],fontsize=10)
            myplot.tick_params(labelsize=10)
            plt.legend(fontsize='medium', title_fontsize='10', loc = "upper right")
            myplot.figure.savefig("../res/"+self.file+"_"+str(columns[0])+"_"+str(columns[2])+"_PF_true.png")
            plt.close()
            myplot = sns.scatterplot(x=columns[1], y=columns[2],data=current_targets,hue=current_targets.label.tolist(), palette=["lightgray","red"])
            myplot.set_xlabel(columns[1],fontsize=10)
            myplot.set_ylabel(columns[2],fontsize=10)
            myplot.tick_params(labelsize=10)
            plt.legend(fontsize='medium', title_fontsize='10', loc = "upper right")
            myplot.figure.savefig("../res/"+self.file+"_"+str(columns[1])+"_"+str(columns[2])+"_PF_true.png")
            plt.close()


    def subgroupsToString(self):
        for elem in self.top_k:
            print("Subgroup : " + str(elem[3].get()) + " Extent: " + str(elem[2]) + " Quality : " + str(elem[0]))


    def subgroupsToCSV(self):
        cmpt = 0
        for elem in heapq.nlargest(self.k,self.top_k):
            cmpt += 1
            lst_row = [self.file,self.beam_width,self.search_depth,self.quality_measure,cmpt,str(elem[3].get()),str(elem[2]),elem[0]]
            with open("../res/results_experiments.csv", 'a+') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow(lst_row)

    # A slightly modified version of beam search
    def process(self):
        if(self.depth == 0):
            self.depth += 1
            for var in self.domains:
                for val in self.domains[var]:
                    current_sg = subgroup(var,val)
                    current_ext = current_sg.computeExtent(self.data)
                    duplicate = False
                    duplicate_top_k = False
                    if(len(list(set(self.pareto_front_global).intersection(current_ext))) != 0):
                        for elem in self.beam:
                            if(set(elem[2]) == set(current_ext)):
                                duplicate = True
                                break
                        if(duplicate == False):
                            current_targets = copy.deepcopy(self.temp_targets)
                            current_targets = current_targets[~current_targets.index.isin(current_ext)]
                            current_pf = computeParetoFront(current_targets)
                            targets_current_pf = self.temp_targets.loc[current_pf]
                            qual = computeQuality(self.quality_measure,self.pareto_front_global,current_pf,self.targets_pareto_front,targets_current_pf,current_ext,len(self.data.index),len(current_ext))
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
                                if(len(list(set(self.pareto_front_global).intersection(current_ext))) != 0):
                                    for elem in self.beam:
                                        if(set(elem[2]) == set(current_ext)):
                                            duplicate = True
                                            break
                                    if(duplicate == False):
                                        current_targets = copy.deepcopy(self.temp_targets)
                                        current_targets = current_targets[~current_targets.index.isin(current_ext)]
                                        current_pf = computeParetoFront(current_targets)
                                        targets_current_pf = self.temp_targets.loc[current_pf]
                                        qual = computeQuality(self.quality_measure,self.pareto_front_global,current_pf,self.targets_pareto_front,targets_current_pf,current_ext,len(self.data.index),len(current_ext))
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
                    