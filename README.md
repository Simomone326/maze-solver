# MAZE SOLVER  

code that generates a maze using prim's algorithm and solves it using DFS  
  
## Prim algorithm  
  
starting from a cell in the maze, uses a list of cells sharing a border with at least one of the already generated ones, decides on one at random, and connects it to a random neighbouring cell between the ones already generated.  
The result is a perfect maze, meaning there's only one path to each cell, consequently there are no loops  
  
## Data structure  
The Maze class saves the cells in a grid, each cell saves the connected neighbours using a list of vectors.  
When solving, the maze is converted into a Tree as it is easier to work with.  
Then DFS is used to explore the tree and find the goal.  
To draw the path, the code starts from the goal and backtracks until it reaches the start.