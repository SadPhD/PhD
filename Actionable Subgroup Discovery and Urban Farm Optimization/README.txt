This README contains the necessary instructions to run the algorithms and methods introduced in our paper

The algorithms require a version of python >= 3.7 and the necessary packages installed and updated.

To install the required packages, run lthe following command : pip install -r requirements.txt 

The file "algo_ida.py" contains the new subgroup discovery algorithm introduced in the paper.

The file "expertknowledge.py" contains the algorithm to generate the recipe using expert knowledge.

The file "randomsearchida.py" contains the algorithm necessary to generate the recipes using a randomsearch.

The file "pcse_script.py" is used to generate recipes using the pcse environment.

The file "virtuous_circle_framework.py" is the main part of our framework which runs the virtuous circle.

The "data" folder contient the dataset used in our experimentations as well as files needed to generate recipes using the pcse simulator.

The methods need to be run using the command "python main.py".

To chose which method or algorithm to run, the required lines need to be uncommented in the file "main.py".

The file "symbolic_regression.py" can be run by itself using the command "python symbolic_regression.py". It generates the symbolic regression model needed.

The file "grid_search.py" can be run by itself using the command "python grid_search.py". It uses the symbolic regression model generated to find the best recipe according to a grid search.