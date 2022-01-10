import pickle 
import copy
import numpy as np
from gplearn.genetic import SymbolicRegressor
from sortedcontainers import SortedList

data = np.load('./data/data_pcse_3attributes_3phases_1000sim.npy')
data = data[1:150,1:]

with open('./best_classifier.pkl', 'rb') as f:
    est_gp = pickle.load(f)

data = data.astype(float)

min_values = data.min(axis=0)
max_values = data.max(axis=0)

disc_grid = 4
search_space_size = disc_grid ** len(max_values)
iteration_count = 0
top_k = 1
print(min_values)

print('Search space size {}'.format(search_space_size))

def compute_rec(recipe, position, min_values, max_values, max_depth, best_recipes):
    global iteration_count
    global top_k
    if position == max_depth:
        formated_recipe = [recipe] 
        predicted_value = est_gp.predict(formated_recipe)

        if predicted_value > best_recipes[-1][0]:
            best_recipes.update([[predicted_value, copy.deepcopy(recipe)]])
            if len(best_recipes) > 18:
                best_recipes.pop()

        iteration_count += 1
        if iteration_count % 10000 == 0:
            print('{} %'.format(int(iteration_count / search_space_size * 100)))
        return

    min_value = min_values[position]
    max_value = max_values[position]

    for x in np.linspace(min_value, max_value, disc_grid):
        recipe[position] = x
        compute_rec(recipe, position + 1, min_values, max_values, max_depth, best_recipes)
        recipe[position] = -1

recipe = [-1 for i in range(data.shape[1] - 1)]
best_recipes = SortedList(key=lambda x: -x[0])
best_recipes.update([[-1, []]])

# we do not take into account the last element which is the target class
compute_rec(recipe, 0, min_values, max_values, data.shape[1] - 1, best_recipes)
print(best_recipes)
