from algo_ida import *
from pcse_script import *
import random
import pandas as pd
from pyDOE import *

class VirtuousCircle:

    def __init__(self, data, a, nb_points_it, nb_it, min_imp, samp_method, card_var_samp, nb_phases, nb_var):    
        self.data = data
        self.factor_qual = a
        self.nb_points_it = nb_points_it
        self.nb_it = nb_it
        self.min_imp = min_imp
        self.nb_phases = nb_phases
        self.nb_var = nb_var
        self.samp_method = samp_method
        self.card_var_samp = card_var_samp
        

    def start(self):
        top_pattern, mean_sg, domains, elapsed_time, best_recipe = AlgorithmClosed(self.data, self.factor_qual, self.nb_points_it).start()
        score_lst = np.array(mean_sg)
        best_rec = best_recipe
        runtime = elapsed_time
        if self.nb_it != 0: # if we work with a given number of iterations and not with a minimal improvement
            previous_val = mean_sg
            for k in range(0, self.nb_it-1):
                if self.samp_method == 2:
                    lhd = lhs(self.nb_phases*self.nb_var, samples=self.nb_points_it, criterion='c')
                for i in range(0, self.nb_points_it):
                    for j in range(0, len(top_pattern)):
                        if self.samp_method == 0:
                            sampled_val = random.choice(domains[j][(domains[j] >= top_pattern[j][0]) & (domains[j] <= top_pattern[j][1])])
                        elif self.samp_method == 1:
                            sampled_val = random.choice(np.linspace(top_pattern[j][0], top_pattern[j][1], self.card_var_samp))
                        elif self.samp_method == 2:
                            sampled_val = (top_pattern[j][1] - top_pattern[j][0])*lhd[i][j] + top_pattern[j][0]
                        if j == 0:
                            array_new_ex = np.array(sampled_val)
                        else:
                            array_new_ex = np.append(array_new_ex, sampled_val)
                    if i == 0:
                        arr_data_new = np.copy(array_new_ex)
                        arr_rows = np.array([[str(i)]])
                        arr_tar = np.array([[runPcse(array_new_ex, self.nb_phases, self.nb_var)]])
                    else:
                        arr_data_new = np.vstack((arr_data_new, array_new_ex))
                        arr_rows = np.vstack((arr_rows, [[str(i)]]))
                        arr_tar = np.vstack((arr_tar, [[runPcse(array_new_ex, self.nb_phases, self.nb_var)]]))
                for i in range(0, arr_data_new.shape[1]):
                    if i == 0:
                        arr_columns = np.array(["Rows", "Col" + str(i)])
                    else:
                        arr_columns = np.append(arr_columns, "Col" + str(i))
                arr_data_new = np.around(arr_data_new, 2)
                arr_tar = np.around(arr_tar, 2)
                arr_columns = np.append(arr_columns, "Tar")
                arr_data_new = np.hstack((arr_rows, arr_data_new))
                arr_data_new = np.hstack((arr_data_new, arr_tar))
                arr_data_new = np.vstack((arr_columns, arr_data_new))

                top_pattern, mean_sg, domains, elapsed_time, best_recipe = AlgorithmClosed(arr_data_new, self.factor_qual, self.nb_points_it).start()
                runtime += elapsed_time
                if mean_sg > previous_val:
                    score_lst = np.append(score_lst, mean_sg)
                    if(best_recipe > best_rec):
                        best_rec = best_recipe
                if (mean_sg - previous_val)/previous_val <= self.min_imp:
                    break
                else:
                    previous_val = mean_sg
                arr_data_new2 = arr_data_new[1:, 1:].astype(float)
                arr_data_new2 = arr_data_new2[arr_data_new2[:,-1].argsort()[::-1]]
        else: # if we work with a minimal improvement
            previous_val = mean_sg
            improving = True
            cmpt = 1
            while improving:
                cmpt += 1
                if self.samp_method == 2:
                    lhd = lhs(self.nb_phases*self.nb_var, samples=self.nb_points_it, criterion='c')
                for i in range(0, self.nb_points_it):
                    for j in range(0, len(top_pattern)):
                        if self.samp_method == 0:
                            sampled_val = random.choice(domains[j][(domains[j] >= top_pattern[j][0]) & (domains[j] <= top_pattern[j][1])])
                        elif self.samp_method == 1:
                            sampled_val = random.choice(np.linspace(top_pattern[j][0], top_pattern[j][1], self.card_var_samp))
                        elif self.samp_method == 2:
                            sampled_val = (top_pattern[j][1] - top_pattern[j][0])*lhd[i][j] + top_pattern[j][0]
                        if j == 0:
                            array_new_ex = np.array(sampled_val)
                        else:
                            array_new_ex = np.append(array_new_ex, sampled_val)
                    if i == 0:
                        arr_data_new = np.copy(array_new_ex)
                        arr_rows = np.array([[str(i)]])
                        arr_tar = np.array([[runPcse(array_new_ex, self.nb_phases, self.nb_var)]])
                    else:
                        arr_data_new = np.vstack((arr_data_new, array_new_ex))
                        arr_rows = np.vstack((arr_rows, [[str(i)]]))
                        arr_tar = np.vstack((arr_tar, [[runPcse(array_new_ex, self.nb_phases, self.nb_var)]]))
                for i in range(0, arr_data_new.shape[1]):
                    if i == 0:
                        arr_columns = np.array(["Rows", "Col" + str(i)])
                    else:
                        arr_columns = np.append(arr_columns, "Col" + str(i))
                arr_data_new = np.around(arr_data_new, 2)
                arr_tar = np.around(arr_tar, 2)
                arr_columns = np.append(arr_columns, "Tar")
                arr_data_new = np.hstack((arr_rows, arr_data_new))
                arr_data_new = np.hstack((arr_data_new, arr_tar))
                arr_data_new = np.vstack((arr_columns, arr_data_new))

                top_pattern, mean_sg, domains, elapsed_time, best_recipe = AlgorithmClosed(arr_data_new, self.factor_qual, self.nb_points_it).start()
                runtime += elapsed_time
                if mean_sg > previous_val:
                    score_lst = np.append(score_lst, mean_sg)
                    if(best_recipe > best_rec):
                        best_rec = best_recipe
                if (mean_sg - previous_val)/previous_val <= self.min_imp:
                    improving = False
                else:
                    previous_val = mean_sg
        return best_rec