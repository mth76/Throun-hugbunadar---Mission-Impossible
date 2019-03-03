import pygame
import sys
pygame.init()

class levelinbetween:
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 800
        self.RED = (255,0,0)
        self.player_pos = [300, 300]
        self.player_size = 20

    def run(self):
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        game_over = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    x = self.player_pos[0]
                    y = self.player_pos[1]

                    if event.key == pygame.K_LEFT:
                        x -= 10
                    elif event.key == pygame.K_RIGHT:
                        x += 10
                    elif event.key == pygame.K_UP:
                        y -= 10
                    elif event.key == pygame.K_DOWN:
                        y += 10

                    self.player_pos = [x,y]

            screen.fill((0,0,0))
            pygame.draw.rect(screen, self.RED, (self.player_pos[0],self.player_pos[1], self.player_size, self.player_size))
            pygame.display.update()
def main():
    game = levelinbetween()
    game.run()

if __name__ == '__main__':
    main()
