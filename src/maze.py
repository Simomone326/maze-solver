import pygame
from pygame import Surface, Vector2, draw
import math
class Cell():
    def __init__(self, side_len, position: Vector2, maze):
        self.side_len = side_len #the maze class manages the walls
        self.position = position #x and y coordinates of this cell, NOT pixel coordinates
        self.maze = maze
        self.connected_neighbours = [] #which neighbours it's connected to, saved as a Vector2 (north is (0,-1), east is (1, 0) and so on)

class Maze():
    def __init__(self, size_pixels, cell_size, walls_width):
        self.size_pixels = size_pixels #pixels per side
        self.cell_size = cell_size #size of one cell
        self.cells_per_side = size_pixels//cell_size
        self.walls_width = walls_width
        self.grid = []
        for y in range(self.cells_per_side):
            temp = []
            for x in range(self.cells_per_side):
                temp.append(Cell(cell_size, Vector2(x, y), self))
            self.grid.append(temp)

    def draw_maze(self, screen: Surface):
        maze_sur = Surface((self.size_pixels, self.size_pixels))
        maze_sur.fill("white")
        #keep track of already drawn walls as tuples of integers using hash tables' "in" which is O(1). 
        #Each integer "i" is a cell of y = i/cells_per_side and x = i%cells_per_side
        #first the min, then the max to avoid doing a double check
        walls = set()
        #draw on maze_sur
        for i in range(len(self.grid[0])*len(self.grid)):
            y = math.floor(i/self.cells_per_side)
            x = i%self.cells_per_side
            cell = self.grid[math.floor(i/self.cells_per_side)][ i%self.cells_per_side]
            cell_pixelpos = cell.position * self.cell_size #upper left corner of the cell
            possible_neighbours = [Vector2(-1,0), Vector2(1, 0), Vector2(0, -1), Vector2(0, 1)]
            #draw a wall between unconnected neighbours
            for neighbour in possible_neighbours:
                neighbour_i = i + neighbour.y*self.cells_per_side + neighbour.x #this formula gets the i of the neighbour
                #neighbours are not connected and teh wall is still not drawn and the neighbour not inside (meaning it's a border wall)
                if neighbour not in cell.connected_neighbours and (min(i, neighbour_i), max(i, neighbour_i)) not in walls and not self._is_inside(Vector2(x, y) + neighbour):
                    #North
                    if neighbour == Vector2(0,-1):
                        draw.line(maze_sur, "black", cell_pixelpos, cell_pixelpos + Vector2(self.cell_size, 0), width= self.walls_width)
                    #South
                    if neighbour == Vector2(0, 1):
                        draw.line(maze_sur, "black", cell_pixelpos + Vector2(0, self.cell_size), cell_pixelpos + Vector2(self.cell_size, self.cell_size), width= self.walls_width)
                    #East
                    if neighbour == Vector2(1, 0):
                        draw.line(maze_sur, "black", cell_pixelpos + Vector2(self.cell_size, 0), cell_pixelpos + Vector2(self.cell_size, self.cell_size), width= self.walls_width)
                    #West
                    if neighbour == Vector2(-1, 0):
                        draw.line(maze_sur, "black", cell_pixelpos, cell_pixelpos + Vector2(0, self.cell_size), width= self.walls_width)
                    #Add this wall to the set
                    walls.add((min(i, neighbour_i), max(i, neighbour_i)))
        blit_x = (screen.get_size()[0]-self.size_pixels)/2
        blit_y = (screen.get_size()[1]-self.size_pixels)/2
        screen.blit(maze_sur, (blit_x, blit_y))
    
    def generate(self):
        #use Prim's algorithm
        pass

    def color_cell(self):
        pass    

    def _is_inside(self, position: Vector2):
        return 0 <= position.x < self.cells_per_side and 0 <= position.y < self.cells_per_side