import pygame

class Abilitybox(pygame.sprite.Sprite):
    
    def __init__(self, x=275, y=0, width = 30, height = 30):
        super().__init__()
        
        self.image_path = "assets/ability_shoot.png"
        self.original_image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.original_image, (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
