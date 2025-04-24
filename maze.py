from priorityqueue import PriorityQueue, PriorityQueueItem
import pygame

class Maze:
    """
    Interprets the maze as an undirected graph.

    Attributes:
        world: A 2D list representing the maze layout with 0 for walls and 1 for open paths.
        adjacency_list: A dictionary to store the adjacency list representation of the graph.
    """
    def __init__(self, world):
        """
        Initializes the Maze object with the given matrix layout.
        """
        self.world = world
        self.adjacency_list = {}
        rows = len(world)
        cols = len(world[0])
        for i in range(rows):
            for j in range(cols):
                node_index = cols * i + j

                if j + 1 < cols and world[i][j] != 0 and world[i][j+1] != 0:
                    self.adjacency_list.setdefault(node_index, []).append((node_index + 1, 1))
                if j - 1 >= 0 and world[i][j] != 0 and world[i][j-1] != 0:
                    self.adjacency_list.setdefault(node_index, []).append((node_index - 1, 1))
                if i + 1 < rows and world[i][j] != 0 and world[i+1][j] != 0:
                    self.adjacency_list.setdefault(node_index, []).append((node_index + cols, 1))
                if i - 1 >= 0 and world[i][j] != 0 and world[i-1][j] != 0:
                    self.adjacency_list.setdefault(node_index, []).append((node_index - cols, 1))

    def dijkstra(self, start, end, screen=None, WORLD=None, WIDTH=None, HEIGHT=None, BLOCKSIZE=None):
        """
        Dijkstra's algorithm with optional visualization of traversal.
        """
        costs = {v: float('inf') for v in self.adjacency_list}
        settled = {}
        costs[start] = 0
        pq = PriorityQueue()
        pq.insert(PriorityQueueItem(0, start))

        while pq.size() > 0:
            min_node = pq.get_min()
            pq.delete_min()

            i = min_node.value // len(self.world[0])
            j = min_node.value % len(self.world[0])

            if WORLD and screen:
                if WORLD[i][j] != "s" and WORLD[i][j] != "d":
                    WORLD[i][j] = "*"  # mark as visited
                from main import draw_world, lines  # imported here to avoid circular import
                draw_world(screen, WORLD, WIDTH, HEIGHT, BLOCKSIZE)
                lines(screen, WIDTH, HEIGHT, BLOCKSIZE)
                pygame.display.update()
               #pygame.time.wait(1)  # Small delay so human eye can see traversal

            if min_node.value == end:
                break

            for u, cost in self.adjacency_list[min_node.value]:
                new_cost = min_node.key + cost
                if costs[u] > new_cost:
                    costs[u] = new_cost
                    settled[u] = min_node.value
                    pq.insert(PriorityQueueItem(new_cost, u))

        if end not in settled:
            return []

        path = []
        path.append(end)
        current_node = end
        while current_node != start:
            current_node = settled[current_node]
            path.append(current_node)
        path.reverse()

        return path

    def shortest_path(self, start, end, screen, WIDTH, HEIGHT, BLOCKSIZE):
        """
        Computes and draws the shortest path from node start to end using
        Dijkstra's algorithm.
        """
        path = sorted(self.dijkstra(start, end, screen, self.world, WIDTH, HEIGHT, BLOCKSIZE))
        if path == []:
            self.show_no_solution_popup(screen, WIDTH, HEIGHT)
            return self.world  # Just return the current world without modifying
        new_world = self.world
        rows = len(self.world)
        cols = len(self.world[0])
        pointer_path = 0
        for i in range(rows):
            for j in range(cols):
                current_node = cols * i + j
                if pointer_path < len(path):
                    if current_node == path[pointer_path]:
                        if new_world[i][j] not in ("s", "d"): 
                            new_world[i][j] = "#"
                        pointer_path += 1

        return new_world
    
    def show_no_solution_popup(self, screen, WIDTH, HEIGHT):
        """
        Displays a pop-up rectangle with a message on the existing GUI screen.
        """
        pygame.font.init()
        popup_width, popup_height = 400, 200
        popup_x = (WIDTH - popup_width) // 2
        popup_y = (HEIGHT - popup_height) // 2

        font = pygame.font.SysFont(None, 36)
        text = font.render('There is no solution available!', True, (255, 0, 0))
        text_rect = text.get_rect(center=(popup_x + popup_width // 2, popup_y + popup_height // 2))

        # Draw semi-transparent background
        popup_surface = pygame.Surface((popup_width, popup_height))
        popup_surface.set_alpha(230)  # Slight transparency
        popup_surface.fill((255, 255, 255))  # White box
        screen.blit(popup_surface, (popup_x, popup_y))

        # Draw border
        pygame.draw.rect(screen, (0, 0, 0), (popup_x, popup_y, popup_width, popup_height), 2)

        # Draw the text
        screen.blit(text, text_rect)
        pygame.display.update()

        # Wait for user to close popup (press any key or click)
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False



    def __repr__(self):
        lst = []
        for u, adj_lst in self.adjacency_list.items():
            for v in adj_lst:
                lst.append(f"{u}->{v[0]}|{v[1]}")
        return "[" + ", ".join(lst) + "]"
