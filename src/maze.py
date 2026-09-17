from pygame import Surface, Vector2, draw
from collections import deque
import random
class Cell():
    def __init__(self, side_len, position: Vector2, maze):
        self.side_len = side_len #the maze class manages the walls
        self.position = position #x and y coordinates of this cell, NOT pixel coordinates
        self.maze = maze
        self.connected_neighbours = [] #which neighbours it's connected to, saved as a Vector2 (north is (0,-1), east is (1, 0) and so on)

class Maze():
    def __init__(self, size_pixels, cells_per_side, walls_width):
        self.size_pixels = size_pixels #pixels per side
        self.cells_per_side = cells_per_side
        self.cell_size = size_pixels//cells_per_side #size of one cell
        self.walls_width = walls_width
        self.grid = []
        for y in range(self.cells_per_side):
            temp = []
            for x in range(self.cells_per_side):
                temp.append(Cell(self.cell_size, Vector2(x, y), self))
            self.grid.append(temp)

    def draw_maze(self, screen: Surface):
        maze_sur = Surface((self.size_pixels, self.size_pixels))
        maze_sur.fill("white")
        #keep track of already drawn walls as tuples of integers using hash tables' "in" which is O(1). 
        #Each integer "idx" is a cell of y = idx/cells_per_side and x = idx%cells_per_side
        #first the min, then the max to avoid doing a double check
        walls = set()
        #draw on maze_sur
        for idx in range(len(self.grid[0])*len(self.grid)):
            y = idx//self.cells_per_side
            x = idx%self.cells_per_side
            cell = self.grid[idx//self.cells_per_side][ idx%self.cells_per_side]
            cell_pixelpos = cell.position * self.cell_size #upper left corner of the cell
            possible_neighbours = [Vector2(-1,0), Vector2(1, 0), Vector2(0, -1), Vector2(0, 1)]
            #draw a wall between unconnected neighbours
            for neighbour in possible_neighbours:
                neighbour_idx = idx + neighbour.y*self.cells_per_side + neighbour.x #this formula gets the i of the neighbour
                #neighbours are not connected and teh wall is still not drawn and the neighbour not inside (meaning it's a border wall)
                if not self._is_inside(Vector2(x, y) + neighbour) or (neighbour not in cell.connected_neighbours and (min(idx, neighbour_idx), max(idx, neighbour_idx)) not in walls): #??and not self._is_inside(Vector2(x, y) + neighbour)
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
                    walls.add((min(idx, neighbour_idx), max(idx, neighbour_idx)))
        blit_x = (screen.get_size()[0]-self.size_pixels)/2
        blit_y = (screen.get_size()[1]-self.size_pixels)/2
        screen.blit(maze_sur, (blit_x, blit_y))
    
    def prim(self):
        genset = set([0])
        togen = [0]
        directions = [
            Vector2(0,-1),
            Vector2(0,1),
            Vector2(1,0),
            Vector2(-1,0)
        ]
        last_print = 0
        while(len(togen) >0):
            curr = togen.pop(random.randint(0, len(togen)-1))
            curr_vec = self._idx_to_vec(curr)
            curr_cell = self.grid[int(curr_vec.y)][int(curr_vec.x)]
            ranchoice = [] #this is to choose a generated neighbour to be connected to later
            for i in range(len(directions)):
                neighbour = curr_vec+directions[i]
                if self._is_inside(neighbour) and self._vec_to_idx(neighbour) not in genset:
                    if self._vec_to_idx(neighbour) not in togen:
                        togen.append(self._vec_to_idx(neighbour))
                elif self._is_inside(neighbour):
                    ranchoice.append(neighbour)
            if len(ranchoice) != 0:
                chosen_neighbour = random.choice(ranchoice)
                neighbour_cell = self.grid[int(chosen_neighbour.y)][int(chosen_neighbour.x)]
                curr_cell.connected_neighbours.append(chosen_neighbour-curr_vec)
                neighbour_cell.connected_neighbours.append(curr_vec-chosen_neighbour)
            if (len(genset)/(self.cells_per_side**2)) - last_print > 0.01:
                print(f"{100*len(genset)/(self.cells_per_side**2)}%")
                last_print = len(genset)/(self.cells_per_side**2)
            genset.add(curr)

    def color_cell(self):
        pass    

    def _is_inside(self, position: Vector2):
        return 0 <= position.x < self.cells_per_side and 0 <= position.y < self.cells_per_side

    def _idx_to_vec(self, idx):
        return Vector2(idx%self.cells_per_side, idx//self.cells_per_side)

    def _vec_to_idx(self, vec: Vector2):
        return int(vec.y*self.cells_per_side + vec.x)
