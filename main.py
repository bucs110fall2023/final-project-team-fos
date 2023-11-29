import pygame
import random
from src.player import Player
from src.enemy import Enemy
#import your controller

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    player = Player()
    enemy = Enemy()
    clock = pygame.time.Clock()
    enemies = pygame.sprite.Group()
    number_of_times_2 = []
    number_of_times_3 = []
    current_time =0
    for n in range(2):
        enemies.add(Enemy(random.randint(0,575),-50))
    
    while True:
        
        current_time = pygame.time.get_ticks()
        #change
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.rect.x -= player.speed
                if event.key == pygame.K_RIGHT:
                    player.rect.x += player.speed

        for enemy in enemies:
            enemy.rect.y = enemy.rect.y + 10
        
        screen.fill((0,0,0))  # Fill the screen with a black color

        screen.blit(player.surface_obj, player.rect)
        
        for enemy in enemies:
            screen.blit(enemy.surface_obj, enemy.rect) 
        
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
    
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
# if __name__ == '__main__':
#     main()

main()