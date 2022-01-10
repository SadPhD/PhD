import pandas as pd
import numpy as np
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate
from sklearn.metrics import make_scorer
from sklearn.datasets import fetch_california_housing
from sklearn.neural_network import MLPRegressor
from sklearn import preprocessing


# # Generate data for MLP regressor on the california housing dataset
# X_california, y_california = fetch_california_housing(return_X_y=True, as_frame = True)

# y_california_temp = y_california.values.astype(float)
# y_california_temp = y_california_temp.reshape(-1, 1)
# min_max_scaler = preprocessing.MinMaxScaler()
# y_california_scaled = min_max_scaler.fit_transform(y_california_temp)
# y_california_normalized = pd.DataFrame(y_california_scaled)

# hidden_layer_sizes = [3,6,9,12,15,18,21,24,27,30]
# alpha = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.01]
# batch_size = [32,64,128,256,512,1024]
# learning_rate_init = [0.001,0.01,0.1,1]
# max_iter = [50,100,200,300,500]
# beta_1 = [0.9,0.93,0.96,0.99]
# beta_2 = [0.990,0.993,0.996,0.999]
# epsilon = [1e-8,1e-6,1e-4,1e-2,1e-1]
# n_iter_no_change = [5,10,20]

# df_res = pd.DataFrame(columns=['hidden_layer_sizes','alpha','batch_size','learning_rate_init','max_iter','beta_1','beta_2','epsilon','n_iter_no_change',
#                                'explained_variance_max','max_error'])

# i = 0
# while i < 200:
#     print("Iter : " + str(i))
#     hidden_layer_sizes_val = np.random.choice(hidden_layer_sizes)
#     alpha_val = np.random.choice(alpha)
#     batch_size_val = np.random.choice(batch_size)
#     learning_rate_init_val = np.random.choice(learning_rate_init)
#     max_iter_val = np.random.choice(max_iter)
#     beta_1_val = np.random.choice(beta_1)
#     beta_2_val = np.random.choice(beta_2)
#     epsilon_val = np.random.choice(epsilon)
#     n_iter_no_change_val = np.random.choice(n_iter_no_change)

#     scoring_ = {'explained_variance','max_error'}
#     NN = MLPRegressor(hidden_layer_sizes = (hidden_layer_sizes_val, ), alpha = alpha_val, batch_size = batch_size_val, learning_rate_init = learning_rate_init_val,
#     max_iter = max_iter_val, beta_1 = beta_1_val, beta_2 = beta_2_val, epsilon = epsilon_val, n_iter_no_change = n_iter_no_change_val, random_state = 1)
#     scores = cross_validate(NN, X_california, y_california_normalized.values.ravel(), cv = 10, scoring = scoring_)
#     if(abs(scores["test_explained_variance"].mean()) <= 1 and abs(scores["test_max_error"].mean()) <= 1):
#         i += 1
#         df_res.loc[len(df_res)] = [hidden_layer_sizes_val,alpha_val,batch_size_val,learning_rate_init_val,max_iter_val,beta_1_val,beta_2_val,epsilon_val,n_iter_no_change_val,
#                                    abs(scores["test_explained_variance"].mean()),abs(scores["test_max_error"].mean())]
# df_res.to_csv("../data/california_housing_MLP_200_2.csv", sep=',', index = False)




# # Generate data for RF multi-label classifier on the yeast dataset with 2 objectives
# df = pd.read_csv("../data/yeast.csv")
# X = df.iloc[:,0:103]
# Y = df.iloc[:,103:117]

# n_estimators = [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900]
# max_depth = [4,8,12,16,20,24,28,32,36,40]
# min_samples_split = [0.02,0.06,0.1,0.14,0.18,0.22,0.26,0.30,0.34,0.38]
# min_samples_leaf = [0.01,0.03,0.05,0.07,0.09,0.11,0.13,0.15,0.17,0.19]
# max_features = [2,4,6,8,10]

# df_res = pd.DataFrame(columns=['n_estimators','max_depth','min_samples_split','min_samples_leaf','max_features','recall_micro_max','precision_micro_max'])

# for i in range(0, 200):
#     print("Iter : " + str(i))
#     n_estimators_val = np.random.choice(n_estimators)
#     max_depth_val = np.random.choice(max_depth)
#     min_samples_split_val = np.random.choice(min_samples_split)
#     min_samples_leaf_val = np.random.choice(min_samples_leaf)
#     max_features_val = np.random.choice(max_features)
#     scoring_ = {'recall_micro':'recall_micro','precision_micro':'precision_micro'}
#     clfs = RandomForestClassifier(random_state = 1, n_estimators = n_estimators_val, max_depth = max_depth_val, min_samples_split = min_samples_split_val,
#     min_samples_leaf = min_samples_leaf_val, max_features = max_features_val)
#     scores = cross_validate(clfs, X, Y, cv = 10, scoring = scoring_)
#     print(scores)
#     df_res.loc[len(df_res)] = [n_estimators_val,max_depth_val,min_samples_split_val,min_samples_leaf_val,max_features_val,
#                               scores["test_recall_micro"].mean(),scores["test_precision_micro"].mean()]

# df_res.to_csv("../data/yeast_RF_200_2.csv", sep=',', index = False)




# # Generate data for RF multi-label classifier on the yeast dataset with 3 objectives
# df = pd.read_csv("../data/yeast.csv")
# X = df.iloc[:,0:103]
# Y = df.iloc[:,103:117]

# n_estimators = [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900]
# max_depth = [4,8,12,16,20,24,28,32,36,40]
# min_samples_split = [0.02,0.06,0.1,0.14,0.18,0.22,0.26,0.30,0.34,0.38]
# min_samples_leaf = [0.01,0.03,0.05,0.07,0.09,0.11,0.13,0.15,0.17,0.19]
# max_features = [2,4,6,8,10]

# df_res = pd.DataFrame(columns=['n_estimators','max_depth','min_samples_split','min_samples_leaf','max_features','recall_micro_max','precision_micro_max','time'])

# for i in range(0, 400):
#     print("Iter : " + str(i))
#     n_estimators_val = np.random.choice(n_estimators)
#     max_depth_val = np.random.choice(max_depth)
#     min_samples_split_val = np.random.choice(min_samples_split)
#     min_samples_leaf_val = np.random.choice(min_samples_leaf)
#     max_features_val = np.random.choice(max_features)
#     scoring_ = {'recall_micro':'recall_micro','precision_micro':'precision_micro'}
#     clfs = RandomForestClassifier(random_state = 1, n_estimators = n_estimators_val, max_depth = max_depth_val, min_samples_split = min_samples_split_val,
#     min_samples_leaf = min_samples_leaf_val, max_features = max_features_val)
#     scores = cross_validate(clfs, X, Y, cv = 10, scoring = scoring_)
#     print(scores)
#     df_res.loc[len(df_res)] = [n_estimators_val,max_depth_val,min_samples_split_val,min_samples_leaf_val,max_features_val,
#                               scores["test_recall_micro"].mean(),scores["test_precision_micro"].mean(),scores["fit_time"].mean()]

# df_res.to_csv("../data/yeast_RF_400_3.csv", sep=',', index = False)