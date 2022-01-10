This README contains the necessary instructions to run the OSMIND algorithm.

The model requires a version of python >= 3.7 and the imported packages updated.

To install the necessary packages, run the command : pip install -r requirements.txt 

The file "algorithm_cotp_optimal.py" contains the main optimized algorithm introduced in our paper.

The file "algorithm_cotp_tight.py" contains a version of our algorithm without the new tight optimistic estimate introduced in our paper.

The file "algorithm_closed_optimal.py" contains a version of our algorithm with the new tight optimistic estimate but without the closure on the positives.

The "data" folder contains the purely numerical datasets used in our experiments.

The algorithms need to be run using the command: "python main.py".

The algorithms have been implemented to work with the quality measures described in our paper.

To choose which algorithm and dataset to run, you need to comment/uncomment the necessary lines in the "main.py" file.