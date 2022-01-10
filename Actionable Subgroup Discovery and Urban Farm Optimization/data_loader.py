# file with functions for loading et pre-processing the data files
import numpy as np
import os

def loadData(file) :
    filename, file_extension = os.path.splitext(file)
    if file_extension == ".txt":
        data = np.loadtxt(file, delimiter = "\t", dtype='object')
    else:
        data = np.load(file)
    return data