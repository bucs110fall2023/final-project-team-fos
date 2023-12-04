import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x=275, y=500, width = 50, height = 80 ):
        super().__init__()
        
        # self.surface_obj = pygame.Surface((50,70))
        # self.surface_obj.fill("white")
        self.image_path = "assets/starship.png"
        self.original_image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.original_image, (width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.speed = 5

# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((600, 600))
#     clock = pygame.time.Clock()  # Add a clock to control the frame rate
#     player = Player()
    
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     player.rect.x -= player.speed
#                 elif event.key == pygame.K_RIGHT:
#                     player.rect.x += player.speed

#         screen.fill("black")  # Fill the screen with a black color
#         screen.blit(player.image, player.rect)  # Draw the player on the screen
        
#         pygame.display.flip()
#         clock.tick(30)  # Set the frame rate to 30 frames per second


# main()

    
        