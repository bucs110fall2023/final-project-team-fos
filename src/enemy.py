import pygame
import random

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, x=275, y=0):
        super().__init__()
        
        self.surface_obj = pygame.Surface((50,50))
        self.surface_obj.fill("red")
        self.rect = self.surface_obj.get_rect()
        self.rect.x = x
        self.rect.y = y

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()  # Add a clock to control the frame rate
    enemy = Enemy()
    enemies = pygame.sprite.Group()
    for n in range(random.randint(1,5)):
        enemies.add(Enemy(random.randint(0,575),random.randint(-400,-50)))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        for enemy in enemies:
            enemy.rect.y = enemy.rect.y + 10
        screen.fill("black")  # Fill the screen with a black color
        for enemy in enemies:
            screen.blit(enemy.surface_obj, enemy.rect)  # Draw the player on the screen
        
        pygame.display.flip()
        clock.tick(30)  # Set the frame rate to 30 frames per second


main()