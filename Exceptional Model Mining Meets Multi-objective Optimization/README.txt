This README contains the necessary instructions to run our method as well as the experiments described in our paper.

The model requires a version of python >= 3.7 and the imported packages updated.

To install the necessary packages, run the command : pip install -r requirements.txt 

The file "beam_search.py" contains the main beam search algorithm with our method implemented.

The file "data_generator.py" contains the code needed to generate the neural network and random forests data for the application case. Run the command "python data_generator.py" after uncommenting the needed lines in the file.

The "data" folder contains the datasets used in our experiments.

The "res" folder contains the results generated when any code is executed.

The main algorithm needs to be run using the command: "python main.py".

The algorithm has been implemented to work with the quality measures described in our paper.

To choose which algorithm and dataset to run, you need to comment/uncomment the necessary lines in the "main.py" file.