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
    number_of_times_2 = []
    number_of_times_3 = []
    current_time =0
    for n in range(2):
        enemies.add(Enemy(random.randint(0,575),-50))

    
    while True:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        for enemy in enemies:
            enemy.rect.y = enemy.rect.y + 10
        screen.fill("black")  # Fill the screen with a black color
        for enemy in enemies:
            screen.blit(enemy.surface_obj, enemy.rect)  # Draw the player on the screen
        for enemy in enemies:
            if enemy.rect.y == 500:
                for n in range(1):
                    enemies.add(Enemy(random.randint(0,575),0))
            if enemy.rect.y == 650:
                enemy.kill() 
                
        if 10000 < current_time <= 20000 and number_of_times_2==[] :
            for n in range(2):
                enemies.add(Enemy(random.randint(0,575),-50))
            number_of_times_2.append(1)
        
        if  20000 < current_time <= 30000 and number_of_times_3==[] :
            for n in range(2):
                enemies.add(Enemy(random.randint(0,575),-50))
            number_of_times_3.append(1)
                
        pygame.display.flip()
        clock.tick(10)  # Set the frame rate to 30 frames per second


main()