import pygame
from src.player import Player

class Laserbeam(pygame.sprite.Sprite):
    def __init__(self, pos_x = 275, pos_y = 500, laserbeam_color = "lime"):
        super().__init__()
        
        self.player = Player()
        self.surface_obj = pygame.Surface((5,17))
        self.surface_obj.fill(laserbeam_color)
        self.rect = self.surface_obj.get_rect()
        self.rect.x = self.player.rect.x + 22
        self.rect.y = self.player.rect.y
    
    # def 나가느게():
    #     while 
    #       self.laserbeam.rect.y -= 20
    #       self.screen.blit(self.laserbeam.surface_obj, self.laserbeam.rect)
    #       if self.laserbeam.rect.y == 0 :
    #         self.laserbeam.kill()
    #         self.laserbeam.rect.x = self.player.rect.x
    #         self.laserbeam.rect.y = self.player.rect.y 
    #         self.check == False