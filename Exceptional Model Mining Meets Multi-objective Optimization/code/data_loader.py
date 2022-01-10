# File for importing data
# Supports only csv, but others can easily be added
import pandas as pd 

def loadData(file) :
    data = pd.read_csv(file)
    return data