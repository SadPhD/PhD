This README contains the necessary instructions to run our method as well as the experiments described in our paper.

The model requires a version of python >= 3.7 and the imported packages updated.

To install the necessary packages, run the command : pip install -r requirements.txt 

The file "EPFDM.py" contains the algorithm with our method implemented for exceptional deviation mining (both top-K and Skyline EMM).

The file "EPFAM.py" contains the algorithm with our method implemented for exceptional approximation mining (both top-K and Skyline EMM).

The "data" folder contains the datasets used in our experiments.

The "res" folder contains the results generated when any code is executed.

The main algorithm needs to be run using the command: "python main.py".

The algorithms have been implemented to work with the quality measures described in our paper.

To choose which part of the experiments to run, you need to comment/uncomment the necessary lines in the "main.py" file.