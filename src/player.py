import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))

class Player(pygame.sprite.Sprite):
    def __init__(self, x= 275, y= 500, image= "assets/starship.png"):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        
        
        
    # def update(self):
    #     for event in pygame.event.get():
    #         if event.key == pygame.K_SPACE:
    #             ship = pygame.draw.rect(screen, self.color, (self.x,self.y,50,50))
    #         if event.key == pygame.K_LEFT:
    #             self.x -= 20
    #             ship = pygame.draw.rect(screen, self.color, (self.x,self.y,50,50))
    #         if event.key == pygame.K_RIGHT:
    #             self.x += 20
    #             ship = pygame.draw.rect(screen, self.color, (self.x,self.y,50,50))
    #         if event.key == pygame.K_s:
    #             for n in range(11):
    #                 y = 450-50*n
    #                 laser = pygame.draw.rect(screen , "green", (self.x+20, self.y, 10, 50))
                    
def main():
    player = Player()
    player.image
    pygame.display.flip()

main()
    
        