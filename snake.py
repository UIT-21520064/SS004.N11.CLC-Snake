import pygame
import sys
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]

    def draw_score(self):
        score_text = str(len(self.body) - 3)
        score_surface = game_font.render(score_text, True, (33, 146, 255))

        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))

        apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))

        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6, apple_rect.height)

        pygame.draw.rect(screen, (253, 255, 0), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (161, 73, 250), bg_rect, 2)

pygame.init()

cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)
apple = pygame.image.load('Graphics/apple.png').convert_alpha()
clock = pygame.time.Clock()

snake = Snake()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    # draw all our element
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((214, 150, 187))
    snake.draw_score()
    pygame.display.update()
    clock.tick(60)




