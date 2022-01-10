# The function to compute the pareto front of any set of objects
# It returns the index of each point that belongs to the pareto front
def computeParetoFront(data):
    pareto_front = list()
    columns = list(data)
    for i in data.index:
        current_obj = data.loc[i,:]
        domine = False
        for j in data.index:
            cmpt = 0
            strict = False
            next_obj = data.loc[j,:]
            for k in range(0, data.shape[1]):
                if(next_obj[k] < current_obj[k]):
                    strict = True
                    cmpt += 1
                elif(next_obj[k] <= current_obj[k]):
                    cmpt += 1
            if(cmpt == data.shape[1] and strict == True):
                domine = True
                break
        if(domine == False):
            pareto_front.append(i)
    return(pareto_front)