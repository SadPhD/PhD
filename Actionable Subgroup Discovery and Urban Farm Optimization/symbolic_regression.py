import pickle
import numpy as np
from gplearn.genetic import SymbolicRegressor

data = np.load('./data/data_pcse_3attributes_3phases_1000sim.npy')
data = data[1:188, 1:]
data = data.astype(float)
print(data.shape)

row_nb, col_nb = data.shape

X_train, y_train = data[:int(0.8*row_nb), :-1], data[:int(0.8*row_nb), -1]
X_test, y_test = data[int(0.8*row_nb):, :-1], data[int(0.8*row_nb):, -1]

est_gp = SymbolicRegressor(population_size=2000,
                           generations=1000, stopping_criteria=0.01,
                           p_crossover=0.7, p_subtree_mutation=0.1,
                           p_hoist_mutation=0.05, p_point_mutation=0.1,
                           max_samples=0.9, verbose=1,
                           parsimony_coefficient=0.01, random_state=0)

est_gp.fit(X_train, y_train)

with open('./best_classifier.pkl', 'wb') as f:
    pickle.dump(est_gp, f)

print(est_gp._program)

with open('./best_classifier.pkl', 'rb') as f:
    est_gp = pickle.load(f)

print(est_gp._program)

