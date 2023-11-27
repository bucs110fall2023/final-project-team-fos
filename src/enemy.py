import pygame
class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, x=275, y=0):
        super().__init__()
        
        self.surface_obj = pygame.Surface((50,50))
        self.surface_obj.fill("red")
        self.rect = self.surface_obj.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        