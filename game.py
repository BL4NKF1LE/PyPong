import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1400, 1000
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("PyPong!")
FPS = 60
BACKGROUND_COLOR = (63, 82, 109)
COURT_COLOR = (255, 255, 255)
NET_COLOR = (34, 45, 94)
PLAYER_ONE_COLOR = (189, 57, 81)
PLAYER_TWO_COLOR = (46, 46, 46)
PADDLE_WIDTH, PADDLE_HEIGHT = (40, 200)
BALL_COLOR = (204, 255, 0)
BALL_RADIUS = 14
SCORE_FONT = pygame.font.SysFont('arial', 100)
SCORE_COLOR = (186, 147, 71)
WINNING_SCORE = 5
VICORY_TEXT_COLOR = (186, 147, 71)


class Paddle:

    VELOCITY = 10

    def __init__(self, x, y, width, height, color):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VELOCITY

        if not up:
            self.y += self.VELOCITY

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y


class Ball:

    MAX_VELOCITY = 12
    COLOR = BALL_COLOR

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_velocity = self.MAX_VELOCITY
        self.y_velocity = 0

    def draw(self, window):
        pygame.draw.circle(window, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_velocity = 0
        self.x_velocity *= -1


def draw(window, paddles, ball, player_one_score, player_two_score):

    window.fill(BACKGROUND_COLOR)

    # X Top Line
    pygame.draw.rect(window, COURT_COLOR,
                     (0, (WINDOW_HEIGHT // 6) - 5, WINDOW_WIDTH, 10))

    # X Middle Line
    pygame.draw.rect(window, COURT_COLOR, (WINDOW_WIDTH * (1 / 4) - 5,
                     (WINDOW_HEIGHT // 2) - 5, WINDOW_WIDTH * (2 / 4), 10))

    # X Bottom Line
    pygame.draw.rect(window, COURT_COLOR,
                     (0, (WINDOW_HEIGHT * (5 / 6)) - 5, WINDOW_WIDTH, 10))

    # Left Lane Line
    pygame.draw.rect(window, COURT_COLOR, (WINDOW_WIDTH * (1 / 4) - 5,
                     (WINDOW_HEIGHT // 6) - 5, 10, WINDOW_HEIGHT - (WINDOW_HEIGHT // 3)))

    # Right Lane Line
    pygame.draw.rect(window, COURT_COLOR, (WINDOW_WIDTH * (3 / 4) - 5,
                     (WINDOW_HEIGHT // 6) - 5, 10, WINDOW_HEIGHT - (WINDOW_HEIGHT // 3)))

    # Net line
    pygame.draw.rect(window, NET_COLOR, (WINDOW_WIDTH //
                     2 - 5, 60, 10, WINDOW_HEIGHT - 130))

    for paddle in paddles:
        paddle.draw(window)

    player_one_score = SCORE_FONT.render(f'{player_one_score}', 1, SCORE_COLOR)
    player_two_score = SCORE_FONT.render(f'{player_two_score}', 1, SCORE_COLOR)
    window.blit(player_one_score, (WINDOW_WIDTH // 4 -
                player_one_score.get_width() // 2, 20))
    window.blit(player_two_score, (WINDOW_WIDTH * (3 / 4) -
                player_two_score.get_width() // 2, 20))

    ball.draw(window)

    pygame.display.update()


def collision(ball, player_one, player_two):

    # Ceiling collision
    if ball.y + ball.radius >= WINDOW_HEIGHT:
        ball.y_velocity *= -1

    if ball.y - ball.radius <= 0:
        ball.y_velocity *= -1

    # X collision
    if ball.x_velocity < 0:
        if ball.y >= player_one.y and ball.y <= player_one.y + player_one.height:
            if ball.x - ball.radius <= player_one.x + player_one.width:
                ball.x_velocity *= -1

                paddle_middle_y = player_one.y + player_one.height / 2
                y_difference = paddle_middle_y - ball.y
                reduction_factor = (player_one.height / 2) / ball.MAX_VELOCITY
                y_velocity = y_difference / reduction_factor
                ball.y_velocity = y_velocity * -1

    else:
        if ball.y >= player_two.y and ball.y <= player_two.y + player_two.height:
            if ball.x + ball.radius >= player_two.x:
                ball.x_velocity *= -1

                paddle_middle_y = player_two.y + player_two.height / 2
                y_difference = paddle_middle_y - ball.y
                reduction_factor = (player_two.height / 2) / ball.MAX_VELOCITY
                y_velocity = y_difference / reduction_factor
                ball.y_velocity = y_velocity * -1


def paddle_movement(keys, player_one, player_two):
    if keys[pygame.K_w] and player_one.y - player_one.VELOCITY >= 0:
        player_one.move(up=True)
    if keys[pygame.K_s] and player_one.y + player_one.VELOCITY + player_one.height <= WINDOW_HEIGHT:
        player_one.move(up=False)

    if keys[pygame.K_UP] and player_two.y - player_two.VELOCITY >= 0:
        player_two.move(up=True)
    if keys[pygame.K_DOWN] and player_two.y + player_two.VELOCITY + player_two.height <= WINDOW_HEIGHT:
        player_two.move(up=False)


def main():

    running = True
    clock = pygame.time.Clock()

    player_one_paddle = Paddle(10, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT //
                               2, PADDLE_WIDTH, PADDLE_HEIGHT, PLAYER_ONE_COLOR)
    player_two_paddle = Paddle(WINDOW_WIDTH - 10 - PADDLE_WIDTH, WINDOW_HEIGHT //
                               2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT, PLAYER_TWO_COLOR)
    ball = Ball(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, BALL_RADIUS)
    player_one_score = 0
    player_two_score = 0
    win = False

    while running:

        clock.tick(FPS)
        draw(WINDOW, [player_one_paddle, player_two_paddle],
             ball, player_one_score, player_two_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        keys_pressed = pygame.key.get_pressed()
        paddle_movement(keys_pressed, player_one_paddle, player_two_paddle)
        ball.move()
        collision(ball, player_one_paddle, player_two_paddle)

        if ball.x < 0:
            player_two_score += 1
            ball.reset()
        if ball.x > WINDOW_WIDTH:
            player_one_score += 1
            ball.reset()

        if player_one_score == WINNING_SCORE:
            win = True
            victory_text = 'PLAYER ONE WINS!'

        if player_two_score == WINNING_SCORE:
            win = True
            victory_text = 'PLAYER TWO WINS!'

        if win:
            WINDOW.fill(BACKGROUND_COLOR)
            win_text = SCORE_FONT.render(victory_text, 1, VICORY_TEXT_COLOR)
            WINDOW.blit(win_text, (WINDOW_WIDTH // 2 - win_text.get_width() //
                        2, WINDOW_HEIGHT // 2 - win_text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(3000)
            win = False
            ball.reset()
            player_one_paddle.reset()
            player_two_paddle.reset()
            player_one_score = 0
            player_two_score = 0

    pygame.quit()


if __name__ == '__main__':
    main()
