# main file to run the algorithm
from data_loader import *
import pandas as pd
from algo_ida import *
from virtuous_circle_framework import *
from domainknowledge import *
from randomsearchida import *

# data file containing random recipes from which the first round of random recipes are extracted when running the virtuous circle framework
data_file = "data/data_pcse_3attributes_3phases_1000sim.npy"

# function to run the virtuous circle nb_rep times and then average the best recipe found fort each repetition
def runVirtuousCircle(data, a, nb_points_it, nb_it, min_imp, samp_method, card_var_samp, nb_phases, nb_var, nb_rep):
    random.seed(1)
    np.random.seed(1)
    score_max = 0
    for j in range(0, nb_rep):
        best_rec = VirtuousCircle(data = data, a = a, nb_points_it = nb_points_it, nb_it = nb_it, 
                                                                                min_imp = min_imp, samp_method = samp_method, card_var_samp = card_var_samp, 
                                                                                nb_phases = nb_phases, nb_var = nb_var).start()
        score_max += best_rec
    return(int(round(score_max/nb_rep)))


def main():
    data = loadData(data_file)
    
    # uncomment to run the subgroup discovery algorithm by itself
    # as parameters, value of parameter a (between 0 and 1) and number of objects
    # top_pattern, mean_sg, domains, elapsed_time, best_recipe = AlgorithmClosed(data, a = 0.5, nb_points = 30).start()
    # print(best_recipe)

    # uncomment to generate the expert recipe and its yield
    # expert_recipe_yield = generateExpertRecipe()
    # print(expert_recipe_yield)

    # uncomment to generate recipes through random search with 150 recipes per iteration and 10 iterations
    # returns the average of the best recipe over the 10 iterations
    # random_search_yield = generateDataRandomSearch(nb_phases = 3, nb_var = 3, nb_sim = 150, nb_rep = 10, seed = 0)
    # print(random_search_yield)

    # uncomment to generate recipes through random search with 150 recipes per iteration and 10 iterations
    # returns the average of the best recipe over the 10 iterations
    virtuous_circle_recipe_yield = runVirtuousCircle(data = data, a = 0.5, nb_points_it = 30, nb_it = 5, min_imp = 0, samp_method = 1, card_var_samp = 15, nb_phases = 3, nb_var = 3, nb_rep = 10)
    print(virtuous_circle_recipe_yield)

if __name__ == "__main__":
    main()