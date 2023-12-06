import pygame
import random

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, x=275, y=0, width=30, height=90, image_path = "assets/enemyship.png"):
        super().__init__()
        
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10