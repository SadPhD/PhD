# main file to run the algorithm
from data_loader import *
from EPFDM import *
from EPFAM import *

def main():
# EPFDM on synthetic and real data (+ runtime)
    # data_file = "../data/fonseca_5000.csv"
    # data = loadData(data_file)
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "AHD", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "MHD", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()

    # data_file = "../data/obesity_binned.csv"
    # data = loadData(data_file)
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "AHD", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "MHD", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()

    # data_file = "../data/plant_defenses.csv"
    # data = loadData(data_file)
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "AHD", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "MHD", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()

    # data_file = "../data/real_estate.csv"
    # data = loadData(data_file)
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "AHD", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "MHD", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()


# Study of runtime on different configurations of the alorithm on the 4 datasets
    # data_file = "../data/fonseca_5000.csv"
    # data = loadData(data_file)
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0.3, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0.5, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "ent", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "ent", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "ent", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "cov", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "cov", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "cov", gen_factor = 1, skyline = 0).start()

    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0.3, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0.5, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "ent", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "ent", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "ent", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "cov", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "cov", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "cov", gen_factor = 1, skyline = 0).start()

    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.3, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.5, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "ent", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "ent", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "ent", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "cov", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "cov", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "cov", gen_factor = 1, skyline = 0).start()


    # data_file = "../data/obesity_binned.csv"
    # data = loadData(data_file)
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0.3, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0.5, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0.3, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0.5, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.3, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.5, gen_type = "", gen_factor = 1, skyline = 0).start()


    # data_file = "../data/plant_defenses.csv"
    # data = loadData(data_file)
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0.3, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0.5, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "ent", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "ent", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "ent", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "cov", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "cov", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "cov", gen_factor = 1, skyline = 0).start()

    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0.3, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0.5, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "ent", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "ent", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "ent", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "cov", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "cov", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "cov", gen_factor = 1, skyline = 0).start()

    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.3, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.5, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "ent", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "ent", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "ent", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "cov", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "cov", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "cov", gen_factor = 1, skyline = 0).start()


    # data_file = "../data/real_estate.csv"
    # data = loadData(data_file)
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0.3, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0.5, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "ent", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "ent", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "ent", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "cov", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "cov", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.1, min_support = 0, gen_type = "cov", gen_factor = 1, skyline = 0).start()

    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0.3, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0.5, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "ent", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "ent", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "ent", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "cov", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "cov", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 0.5, min_support = 0, gen_type = "cov", gen_factor = 1, skyline = 0).start()

    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.3, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.5, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "ent", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "ent", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "ent", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "cov", gen_factor = 0.1, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "cov", gen_factor = 0.5, skyline = 0).start()
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0, gen_type = "cov", gen_factor = 1, skyline = 0).start()


# EPFAM on synthetic and real data (+ runtime)
    # data_file = "../data/fonseca_5000.csv"
    # data = loadData(data_file)
    # EPFAM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()

    # data_file = "../data/obesity_binned.csv"
    # data = loadData(data_file)
    # EPFAM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()

    # data_file = "../data/real_estate.csv"
    # data = loadData(data_file)
    # EPFAM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()

    # data_file = "../data/plant_defenses.csv"
    # data = loadData(data_file)
    # EPFAM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()


# Application scenario
# Run EPFDM
    # data_file = "../data/data_pcse_couts_6var_300_[0.2461, 0.4922, 0.0515, 0.1074, 0.0514, 0.0514]_binned_2.csv"
    # data = loadData(data_file)
    # EPFDM(data, k = 3, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HD", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 3, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()

# Run EPFAM
    # data_file = "../data/data_pcse_couts_6var_300_[0.2461, 0.4922, 0.0515, 0.1074, 0.0514, 0.0514]_binned_2.csv"
    # data = loadData(data_file)
    # EPFAM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()

# Run EPFAM with new recipes
    # data_file = "../data/data_pcse_couts_6var_300_iter_[0.2461, 0.4922, 0.0515, 0.1074, 0.0514, 0.0514]_binned_2.csv"
    # data = loadData(data_file)
    # EPFAM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 2, file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()

# Run EPFDM and EPFAM with 3 objectives
    # data_file = "../data/data_pcse_3D_6var_300_[0.2461, 0.4922, 0.0515, 0.1074, 0.0514, 0.0514]_binned_2.csv"
    # data = loadData(data_file)
    # EPFDM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 3, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFAM(data, k = 1, beam_width = 10, search_depth = 5, nb_target = 3, file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()

# Run EPFDM with skylines
    # data_file = "../data/data_pcse_couts_6var_300_[0.2461, 0.4922, 0.0515, 0.1074, 0.0514, 0.0514]_binned_2.csv"
    # data = loadData(data_file)
    # EPFDM(data, k = 1, beam_width = 0, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 1).start()
    # EPFDM(data, k = 18, beam_width = 1, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 18, beam_width = 3, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 18, beam_width = 5, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 18, beam_width = 10, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 18, beam_width = 20, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()
    # EPFDM(data, k = 18, beam_width = 50, search_depth = 5, nb_target = 2, quality_measure = "HV", file = data_file[8:-4], 
    # loc_factor = 1, min_support = 0.1, gen_type = "", gen_factor = 1, skyline = 0).start()


if __name__ == "__main__":
    main()