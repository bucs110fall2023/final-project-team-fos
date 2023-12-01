import pygame
from src.player import Player

class Laserbeam(pygame.sprite.Sprite):
    def __init__(self, x= 5, y = 17, laserbeamcolor = "lime", laserbeamspeed = 11):
        super().__init__()
        
        self.player = Player()
        self.surface_obj = pygame.Surface((5,17))
        self.surface_obj.fill(laserbeamcolor)
        self.rect = self.surface_obj.get_rect()
        self.rect.x = self.player.rect.x + 20
        self.rect.y = self.player.rect.y + y
        self.speed = laserbeamspeed
    