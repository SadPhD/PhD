# This is the subgroup class file used to build subgroup objects
import copy

class subgroup:

    def __init__(self, var, value):
        self.sg = dict()
        self.sg.update({var:value})


    def get(self):
        return(self.sg)


    def add(self, var, value):
        self.sg.update({var:value})


    def size(self):
        return(len(self.sg))


    def computeExtent(self, data):
        data_sg = copy.deepcopy(data)
        for key in self.sg:
            data_sg = data_sg.loc[data_sg[key] == self.sg[key]]
        return list(data_sg.index)