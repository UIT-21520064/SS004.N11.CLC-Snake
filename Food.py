from random import randrange
from pygame.math import Vector2
from pygame.image import load
from pygame import Surface, Rect

class Food:
    def __init__(self,  width_border: int, hight_border: int, cell_size: int):
        self.hight_border = hight_border
        self.width_border = width_border
        self.cell_size = cell_size
        self.coor = None
        self.food_graphic = load('Graphics/apple.png').convert_alpha()
        
    def Generate_new_food(self, body: list[Vector2]) -> Vector2:
        while True:
            new_coor = Vector2(randrange(0, self.width_border), randrange(0, self.hight_border))  
            if self.coor is None or (new_coor != self.coor and new_coor not in body):
                self.coor = new_coor
                return new_coor
    
    def Draw(self, screen: Surface) -> None:
        x, y = self.coor[0] * self.cell_size, self.coor[1] * self.cell_size
        block_rect = Rect(x, y, self.cell_size, self.cell_size)
        screen.blit(self.food_graphic, block_rect)
    
    def Eat_food(self, head: Vector2) -> bool:
        # if head not on the food return false
        if self.coor != head: return False
        # or else eat food return true
        return True
    
    def Update(self, body: list[Vector2]) -> bool:
        if body[0] == self.coor:
            self.coor = self.Generate_new_food(body)
            return True
        
        return False