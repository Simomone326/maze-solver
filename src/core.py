import pygame
from maze import Maze
from solver import DFS
def core_loop():
    # Example file showing a basic pygame "game loop"

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    screen.fill("white")
    clock = pygame.time.Clock()
    running = True
    print("drawing maze...")
    maze = Maze(720, 50, 1)
    start = maze.grid[0][0]
    end = maze.grid[-1][-1]
    maze.prim()
    maze.draw_maze(screen)
    print("maze done")
    pygame.time.wait(1000)
    pygame.display.flip()
    print("starting to solve...")
    DFS(maze, start, end, screen)
    pygame.display.flip()
    print("solved!")
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        #screen.fill("purple")

        # RENDER YOUR GAME HERE
        



        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
