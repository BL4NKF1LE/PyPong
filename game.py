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

    def move(self, up = True):
        if up:
            self.y -= self.VELOCITY
        
        if not up:
            self.y += self.VELOCITY
        

def draw(window, paddles):
    window.fill(BACKGROUND_COLOR)

    for paddle in paddles:
        paddle.draw(window)

    pygame.display.update()

def paddle_movement(keys, player_one, player_two):
    if keys[pygame.K_w]:
        player_one.move(up = True)
    if keys[pygame.K_s]:
        player_one.move(up = False)

    if keys[pygame.K_UP]:
        player_two.move(up = True)
    if keys[pygame.K_DOWN]:
        player_two.move(up = False)

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

        keys_pressed = pygame.key.get_pressed()
        paddle_movement(keys_pressed, player_one_paddle, player_two_paddle)

    pygame.quit()

if __name__ == '__main__':
    main()