import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 700, 500
WINDOW = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)
pygame.display.set_caption("Paco's Pong")

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = True
                break

    quit()