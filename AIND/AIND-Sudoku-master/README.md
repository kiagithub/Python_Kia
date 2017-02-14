# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: *my approach is as follow:*
* for each unit we find the values and then values with length of two. Then we compare each box with the others (in this stage, size of each box is two),
* if they're equal, then they're naked twins in that unit. Then we remove naked twins digits (two digits one by one) from values of all the boxes in that unit
* this is a blind approach so it removes those digits from the naked twin boxes too, we add all those digits in the end to the boxes with length of zero (naked boxes).
* constraint propagation has three steps here: 1) limiting search to each unit 2)limiting search to each box with the size of two 3)removing digits if there are two boxes with the same size


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: *my approach is as follow:*
* I made two lists from rows and cols, then constructed each diagonal unit with list comprehensions.
* constraint propagation for solving diagonal soduku is the same as original Sudoku, we just need to check two added units to unitlist, so two new members in unitlist, nothing more


### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.