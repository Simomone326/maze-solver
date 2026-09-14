import pygame
from pygame import Surface, Vector2

class Cell():
    def __init__(self, side_len, position: Vector2, maze):
        self.side_len = side_len #the maze class manages the walls
        self.position = position #x and y coordinates of this cell, NOT pixel coordinates
        self.maze = maze
        self.neighbours = [] #which neighbours it's connected to ("North", "East" ecc)

    def draw(self, surface):
        #blit the cell on the surface. Check if neighbouring cells have shared walls to avoid useless blits
        pass

class Maze():
    def __init__(self, size_pixels, size_cells):
        self.size_pixels = size_pixels #pixels per side
        self.size_cells = size_cells #cells per side
        self.grid = []
        for y in range(size_cells):
            temp = []
            for x in range(size_cells):
                temp.append(Cell(size_pixels/size_cells, Vector2(y, x), self))

    def draw(self, surface: Surface):
        pass

    def generate(self):
        #use Prim's algorithm
        pass

    def color_cell(self):
        pass    

    def _is_inside(self, position: Vector2):
        pass