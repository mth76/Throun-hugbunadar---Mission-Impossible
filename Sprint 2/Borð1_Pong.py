import pygame
import random
import sys


class Paddle(pygame.Rect):
    def __init__(self, velocity, up_key,down_key, *args, **kwargs):
        self.velocity = velocity
        self.up_key = up_key
        self.down_key = down_key
        super().__init__(*args, **kwargs)

    def move_paddle(self, board_height):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.up_key]:
            if self.y - self.velocity > 0:
                self.y -= self.velocity

        if keys_pressed[self.down_key]:
            if self.y + self.velocity < board_height - self.height:
                self.y += self.velocity


class Ball(pygame.Rect):

    def __init__(self, velocity, *args, **kwargs):
        self.velocity = velocity
        self.angle = 0
        super().__init__(*args, **kwargs)

    def move_ball(self):
        self.x += self.velocity
        self.y += self.angle


class Pong:
    WIDTH = 800
    HEIGHT = 800
    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 50
    BALL_WIDTH = 10
    BALL_VELOCITY = 10
    WALL_HEIGHT = 2000


    AQUA     = (0  ,128 ,128  )
    WHITE     = (255,255,255)
    ORANGE = (255, 165,0)
    YELLOW = (255, 255, 0)

    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.clock = pygame.time.Clock()

        self.paddles = []
        self.balls = []
        self.paddles.append(Paddle(
            self.BALL_VELOCITY,
            pygame.K_w,
            pygame.K_s,
            0,
            0,
            self.PADDLE_WIDTH,
            self.WALL_HEIGHT
        ))

        self.paddles.append(Paddle(  # The right paddle
            self.BALL_VELOCITY,
            pygame.K_UP,
            pygame.K_DOWN,
            self.WIDTH - self.PADDLE_WIDTH,
            self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2,
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT
        ))

        self.balls.append(Ball( #The wall
            self.BALL_VELOCITY,
            self.WIDTH / 2 - self.BALL_WIDTH / 2,
            self.HEIGHT / 2 - self.BALL_WIDTH / 2,
            self.BALL_WIDTH,
            self.BALL_WIDTH
        ))
        #self.central_line = pygame.Rect(self.WIDTH/2, 0, 1, self.HEIGHT)

    def check_bounce_off_wall(self):
        for ball in self.balls:
            if ball.x > self.WIDTH or ball.x < 0:
                sys.exit(1)
            if ball.y > self.HEIGHT - self.BALL_WIDTH or ball.y < 0:
                ball.angle = -ball.angle

    def check_bounce_off_paddle(self):
        for ball in self.balls:
            for paddle in self.paddles:
                if ball.colliderect(paddle):
                    ball.velocity = -ball.velocity
                    ball.angle = random.randint(-10, 10)
                    break

    def game_loop(self):
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 25)
        frame_count = 0
        frame_rate = 60
        start_time = 90
        size = [800,800]
        screen = pygame.display.set_mode(size)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            # Teikna skjáinn
            self.screen.fill((0, 0, 0))

            for paddle in self.paddles:
                paddle.move_paddle(self.HEIGHT)
                pygame.draw.rect(self.screen, self.WHITE, paddle)




            for ball in self.balls:
                ball.move_ball()
                pygame.draw.rect(self.screen, self.ORANGE, ball)

            self.check_bounce_off_wall()
            self.check_bounce_off_paddle()
            #pygame.draw.rect(self.screen, self.YELLOW, self.central_line)

            total_seconds = frame_count // frame_rate

            minutes = total_seconds // 60

            seconds = total_seconds % 60

            total_seconds = start_time - (frame_count // frame_rate)
            #if total_seconds < 0:
                #total_seconds = 0
            if total_seconds ==0:
                sys.exit(1)
            seconds = total_seconds % 60

            output_string = "Time left: {0:02}".format(seconds)

            text = font.render(output_string, True, self.ORANGE)
            screen.blit(text, [350, 25])

            frame_count += 1

            clock.tick(frame_rate)


            pygame.display.flip()
            self.clock.tick(60)



if __name__=='__main__':
    pong = Pong()
    pong.game_loop()
