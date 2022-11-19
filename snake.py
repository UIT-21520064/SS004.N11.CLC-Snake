import pygame , sys
from pygame.math import Vector2
from Food import Food

class Snake:
    def __init__(self):
        # first index is a head
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)] 
        self.direction = Vector2(1, 0) # move right
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
		
        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
    
        self.food = Food(cell_number, cell_number, cell_size)
        self.food.Generate_new_food(self.body)
    
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for idx, block in enumerate(self.body):
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # pygame.draw.rect(screen, (0, 255, 0), block_rect)
            
            # First element
            if idx == 0:
                screen.blit(self.head, block_rect)
            elif idx == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                pre_block = self.body[idx + 1] - block
                nxt_block = self.body[idx - 1] - block
                if pre_block.x == nxt_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif pre_block.y == nxt_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                elif (pre_block.x == -1 and nxt_block.y == -1) or (nxt_block.x == -1 and pre_block.y == -1):
                    screen.blit(self.body_tl, block_rect)
                elif (pre_block.x == -1 and nxt_block.y == 1) or (nxt_block.x == -1 and pre_block.y == 1):
                    screen.blit(self.body_bl, block_rect)
                elif (pre_block.x == 1 and nxt_block.y == -1) or (nxt_block.x == 1 and pre_block.y == -1):
                    screen.blit(self.body_tr, block_rect)
                elif (pre_block.x == 1 and nxt_block.y == 1) or (nxt_block.x == 1 and pre_block.y == 1):
                    screen.blit(self.body_br, block_rect)


    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        else: self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        else: self.tail = self.tail_down

    def move_snake(self):
        # handle eat food
        if self.food.Eat_food(self.body[0]):
            self.add_block()
            self.food.Generate_new_food(self.body)
        
        # handle movement
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            

    def add_block(self):
        self.new_block = True
        

pygame.init()

cell_size = 30
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
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

        if event.type == SCREEN_UPDATE:
            snake.move_snake()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            
            if event.key == pygame.K_UP:
                if snake.direction.y != 1:
                    snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN:
                if snake.direction.y != -1:
                    snake.direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT:
                if snake.direction.x != 1:
                    snake.direction = Vector2(-1, 0)
            else: 
                if event.key == pygame.K_RIGHT:
                    if snake.direction.x != -1:
                        snake.direction = Vector2(1, 0)

    screen.fill((214, 150, 187))
    snake.draw_snake()
    snake.food.Update_food_graphics(screen)
    pygame.display.update()
    clock.tick(60)
