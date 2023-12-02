import pygame
import random

class Abilitybox(pygame.sprite.Sprite):
    
    def __init__(self, x=275, y=0):
        super().__init__()
        
        self.abilitybox_color = "gold"
        self.surface_obj = pygame.Surface((30,30))
        self.surface_obj.fill(self.abilitybox_color)
        self.rect = self.surface_obj.get_rect()
        self.rect.x = x
        self.rect.y = y
