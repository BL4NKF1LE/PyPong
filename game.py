import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1500, 1200
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paco's Pong")
FPS = 60
BACKGROUND_COLOR = (34, 170, 103)
PADDLE_COLOR = (255, 255, 255)
PADDLE_WIDTH, PADDLE_HEIGHT = (20, 100)

class Paddle:

    COLOR = PADDLE_COLOR
    VELOCITY = 4

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, (self.x, self.y, self.width, self.height))

    

def draw(window, paddles):
    window.fill(BACKGROUND_COLOR)

    for paddle in paddles:
        paddle.draw(window)

    pygame.display.update()

def main():
    running = True
    clock = pygame.time.Clock()

    player_one_paddle = Paddle(10, WINDOW_HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    player_two_paddle = Paddle(WINDOW_WIDTH - 10 - PADDLE_WIDTH, WINDOW_HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    while running:

        clock.tick(FPS)
        draw(WINDOW, [player_one_paddle, player_two_paddle])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()

if __name__ == '__main__':
    main()