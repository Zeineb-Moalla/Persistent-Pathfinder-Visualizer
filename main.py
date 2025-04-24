from maze import Maze
import pygame
from VersionManager import VersionManager

def lines(screen, WIDTH, HEIGHT, BLOCKSIZE):
    for line_row in range(0, WIDTH, BLOCKSIZE):
        pygame.draw.line(screen, (255, 255, 255), (0, line_row), (WIDTH, line_row), width=1)
    for line_col in range(0, HEIGHT, BLOCKSIZE):
        pygame.draw.line(screen, (255, 255, 255), (line_col, 0), (line_col, HEIGHT), width=1)

def draw_world(screen, WORLD, WIDTH, HEIGHT, BLOCKSIZE):
    for i in range(len(WORLD)):
        for j in range(len(WORLD[0])):
            x = j * BLOCKSIZE
            y = i * BLOCKSIZE
            if WORLD[i][j] == 1:
                pygame.draw.rect(screen, (127, 127, 127), pygame.Rect(0, 0, BLOCKSIZE, BLOCKSIZE).move(x, y), width=0)
            if WORLD[i][j] == 0:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, BLOCKSIZE, BLOCKSIZE).move(x, y), width=0)
            if WORLD[i][j] == "s":
                pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(0, 0, BLOCKSIZE, BLOCKSIZE).move(x, y), width=0)
            if WORLD[i][j] == "d":
                pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(0, 0, BLOCKSIZE, BLOCKSIZE).move(x, y), width=0)
            if WORLD[i][j] == "#":
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, BLOCKSIZE, BLOCKSIZE).move(x, y), width=0)
            if WORLD[i][j] == "*":
                pygame.draw.rect(screen, (0, 255, 255), pygame.Rect(0, 0, BLOCKSIZE, BLOCKSIZE).move(x, y), width=0)

def game():
    WIDTH, HEIGHT = 1000, 1000
    BLOCKSIZE = 25
    WORLD = [[1 for _ in range(WIDTH // BLOCKSIZE)] for _ in range(HEIGHT // BLOCKSIZE)]

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Pathfinder')

    version_manager = VersionManager()  
    version_manager.save_version(WORLD)  

    running = True
    pressed = False
    operation = "SET_START"

    while running:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                j = mouse_position[0] // BLOCKSIZE
                i = mouse_position[1] // BLOCKSIZE

                if event.button == 1 and operation == "SET_START":
                    if WORLD[i][j] == 1:
                        WORLD[i][j] = "s"
                        version_manager.save_version(WORLD)  # Save after setting start
                        start = j + i * (HEIGHT // BLOCKSIZE)
                        operation = "SET_DESTINATION"

                elif event.button == 1 and WORLD[i][j] != "s" and operation == "SET_DESTINATION":
                    if WORLD[i][j] == 1:
                        WORLD[i][j] = "d"
                        version_manager.save_version(WORLD)  # Save after setting destination
                        end = j + i * (HEIGHT // BLOCKSIZE)
                        operation = "SET_OBSTACLE"

                elif event.button == 1 and WORLD[i][j] not in ("s", "d") and operation == "SET_OBSTACLE":
                    if WORLD[i][j] == 1:
                        WORLD[i][j] = 0
                        version_manager.save_version(WORLD)  # Save after setting obstacle
                    pressed = True

            if event.type == pygame.MOUSEBUTTONUP and operation == "SET_OBSTACLE":
                if event.button == 1:
                    pressed = False

            if pressed and operation == "SET_OBSTACLE":
                current_pos = pygame.mouse.get_pos()
                j = current_pos[0] // BLOCKSIZE
                i = current_pos[1] // BLOCKSIZE
                if WORLD[i][j] not in ("s", "d"):
                    if WORLD[i][j] == 1:
                        WORLD[i][j] = 0
                        version_manager.save_version(WORLD)  # Save after dragging obstacle

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    maze = Maze(WORLD)
                    WORLD = maze.shortest_path(start, end, screen, WIDTH, HEIGHT, BLOCKSIZE)
                    version_manager.save_version(WORLD)  # Save after finding path

                if event.key == pygame.K_BACKSPACE:
                    pygame.quit()
                    game()

                if event.key == pygame.K_z:  # Undo
                    previous_world = version_manager.undo()
                    if previous_world:
                        WORLD = previous_world

                if event.key == pygame.K_y:  # Redo
                    next_world = version_manager.redo()
                    if next_world:
                        WORLD = next_world

        draw_world(screen, WORLD, WIDTH, HEIGHT, BLOCKSIZE)
        lines(screen, WIDTH, HEIGHT, BLOCKSIZE)
        pygame.display.flip()

if __name__ == "__main__":
    game()
