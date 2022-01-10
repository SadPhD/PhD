# main file to run the method and the experiments
from data_loader import *
from beam_search import *

def main():

    # data_file = "../data/fonseca_5000.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4]).start()




    # data_file = "../data/pcse_binned_width_2.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "MHD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "AHD", file = data_file[8:-4]).start()

    # data_file = "../data/pcse_binned_width_3.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "MHD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "AHD", file = data_file[8:-4]).start()

    # data_file = "../data/pcse_binned_width_5.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "MHD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "AHD", file = data_file[8:-4]).start()

    # data_file = "../data/pcse_binned_width_10.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "MHD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "AHD", file = data_file[8:-4]).start()

    # data_file = "../data/pcse_binned_width_15.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "MHD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "AHD", file = data_file[8:-4]).start()

    # data_file = "../data/pcse_binned_width_20.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "MHD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "AHD", file = data_file[8:-4]).start()




    # data_file = "../data/pcse_binned_freq_2.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "MHD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "AHD", file = data_file[8:-4]).start()

    # data_file = "../data/pcse_binned_freq_3.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "MHD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "AHD", file = data_file[8:-4]).start()

    # data_file = "../data/pcse_binned_freq_5.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "MHD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "AHD", file = data_file[8:-4]).start()

    # data_file = "../data/pcse_binned_freq_10.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "MHD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "AHD", file = data_file[8:-4]).start()

    # data_file = "../data/pcse_binned_freq_15.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "MHD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "AHD", file = data_file[8:-4]).start()

    # data_file = "../data/pcse_binned_freq_20.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "MHD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4]).start()
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "AHD", file = data_file[8:-4]).start()




    # data_file = "../data/real_estate.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 3, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4]).start()




    # data_file = "../data/plant_defenses.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 3, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4]).start()
    



    # data_file = "../data/california_housing_MLP_200_2.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4]).start()




    # data_file = "../data/yeast_RF_200_2.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4]).start()




    # data_file = "../data/yeast_RF_400_3.csv"
    # data = loadData(data_file)
    # beam_search(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 3, quality_measure = "HD", file = data_file[8:-4]).start()



if __name__ == "__main__":
    main()