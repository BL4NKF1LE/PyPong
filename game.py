import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1400, 1000
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paco's Pong")
FPS = 60
BACKGROUND_COLOR = (34, 170, 103)
COURT_COLOR = (255, 255, 255)
PADDLE_COLOR = (255, 255, 255)
PADDLE_WIDTH, PADDLE_HEIGHT = (40, 200)
BALL_COLOR = (204, 255, 0)
BALL_RADIUS = 14

class Paddle:

    COLOR = PADDLE_COLOR
    VELOCITY = 8

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

class Ball:

    MAX_VELOCITY = 9
    COLOR = BALL_COLOR

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_velocity = self.MAX_VELOCITY
        self.y_velocity = 0

    def draw(self, window):
        pygame.draw.circle(window, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

def draw(window, paddles, ball):
    window.fill(BACKGROUND_COLOR)

    for paddle in paddles:
        paddle.draw(window)

    pygame.draw.rect(window, COURT_COLOR, (WINDOW_WIDTH//2 - 5, 0, 10, WINDOW_HEIGHT))

    ball.draw(window)

    pygame.display.update()

def collision(ball, player_one, player_two):

    if ball.y + ball.radius >= WINDOW_HEIGHT:
        ball.y_velocity *= -1

    if ball.y - ball.radius >= 0:
        ball.y_velocity *= -1

        if ball.x_velocity < 0:
            if ball.y >= player_one.y and ball.y <= player_one.y + player_one.height:
                if ball.x - ball.radius <= player_one.x + player_one.width:
                    ball.x_velocity *= -1

        if ball.x_velocity > 0:
            if ball.y >= player_two.y and ball.y <= player_two.y + player_two.height:
                if ball.x + ball.radius >= player_two.x:
                    ball.x_velocity *= -1


def paddle_movement(keys, player_one, player_two):
    if keys[pygame.K_w] and player_one.y - player_one.VELOCITY >= 0:
        player_one.move(up = True)
    if keys[pygame.K_s] and player_one.y + player_one.VELOCITY + player_one.height <= WINDOW_HEIGHT:
        player_one.move(up = False)

    if keys[pygame.K_UP] and player_two.y - player_two.VELOCITY >= 0:
        player_two.move(up = True)
    if keys[pygame.K_DOWN] and player_two.y + player_two.VELOCITY + player_two.height <= WINDOW_HEIGHT:
        player_two.move(up = False)

def main():
    running = True
    clock = pygame.time.Clock()

    player_one_paddle = Paddle(10, WINDOW_HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    player_two_paddle = Paddle(WINDOW_WIDTH - 10 - PADDLE_WIDTH, WINDOW_HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, BALL_RADIUS)

    while running:

        clock.tick(FPS)
        draw(WINDOW, [player_one_paddle, player_two_paddle], ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        keys_pressed = pygame.key.get_pressed()
        paddle_movement(keys_pressed, player_one_paddle, player_two_paddle)
        ball.move()
        collision(ball, player_one_paddle, player_two_paddle)

    pygame.quit()

if __name__ == '__main__':
    main()