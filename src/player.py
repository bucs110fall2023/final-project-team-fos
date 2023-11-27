import pygame

class Player:
    
    def __init__(self, x= 275, y= 500, image= "assets/starship.png"):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.speed = 20 
    
    def shootinglaser(self, width, height):
        self.width = width
        self.height = height
        
    
    
                
def main():
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    player = Player(image="assets/starship.png")
    screen.blit(player)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.rect.x -= player.speed
                
                if event.key == pygame.K_RIGHT:
                    player.rect.x += player.speed
                
        pygame.display.flip()

main()
    
        