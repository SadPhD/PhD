# main file to run the algorithm
from algorithm_cotp_optimal import *
from algorithm_cotp_tight import *
from algorithm_closed_optimal import *
from data_loader import *
import pandas as pd

# Uncomment the dataset to test
data_file = "data/BL.txt"
# data_file = "data/BK.txt"
# data_file = "data/AP.txt"
# data_file =  "data/body_temperature_heart_rate.txt"
# data_file =  "data/pollution.txt"

# if ou want to test the models with growth reicpes, you need to passe the number of recipes to test as parameter of the model in place of len(data)-1 
# and uncomment one line in the code of the algorithm in question
# data_file = "data/data_pcse_3var_3phases_1000sim.npy"

def main():
    data = loadData(data_file)
    # Comment/uncomment the algorithm to test
    # We pass as parameter the purely numerical dataset considered 
    # the value of parameter "a" (between 0 and 1) necessary for the quality measures considere in our paper, and the size of the dataset.
    # This is the OSMIND algorithm
    AlgorithmCOTPOptimal(data, 0.5, len(data)-1).start()
    # This is the OSMIND algorithm without the tight optimistic estimate introduced in our paper.
    # AlgorithmCOTPTight(data, 0.5, len(data)-1).start()                     
    # This is the OSMIND algorithm without the tight optimistic estimate but without the closure on the positives.
    # AlgorithmClosedOptimal(data, 0.5, len(data)-1).start()

if __name__ == "__main__":
    main()