import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paco's Pong")
FPS = 60
BACKGROUND_COLOR = (34, 170, 103)

def draw(window):
    window.fill(BACKGROUND_COLOR)
    pygame.display.update()

def main():
    running = True
    clock = pygame.time.Clock()

    while running:

        clock.tick(FPS)
        draw(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()

if __name__ == '__main__':
    main()