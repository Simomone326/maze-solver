from maze import Maze, Cell
from collections import deque
from pygame import Vector2

#redefining the maze as a tree as it is simpler to work with here

class Node():
    def __init__(self, cell:Cell, parent=None, children:list=[]):
        self.cell = cell
        self.parent = parent
        self.children = children

class Tree():
    def __init__(self, start_cell: Cell, maze: Maze):
        self.start_cell = start_cell
        self.start = Node(start_cell)
        stack = deque()
        for to_neighbour in start_cell.connected_neighbours:
            pos = start_cell.position
            neighbour_pos = pos + to_neighbour
            neighbour_cell = maze.grid[neighbour_pos.y][neighbour_pos.x]
            neighbour_node = Node(neighbour_cell, parent=self.start)
            self.start.children.append(neighbour_node)
            stack.append(neighbour_node)
        while len(stack)>0:
            curr = stack.pop()
            for to_neighbour in curr.cell.connected_neighbours:
                pos = curr.cell.position
                neighbour_pos = pos + to_neighbour
                neighbour_cell = maze.grid[neighbour_pos.y][neighbour_pos.x]
                if neighbour_cell != curr.parent.cell:
                    neighbour_node = Node(neighbour_cell, parent=curr)
                    curr.children.append(neighbour_node)
                    stack.append(neighbour_node)

def DFS(Tree):

            


        
        


