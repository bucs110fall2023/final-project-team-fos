import pygame

class Player:
    
    def __init__(self, x=275, y=500, image="assets/starship.png"):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.speed = 20 
    
    def move(self, direction):
        if direction == "left":
            self.rect.x -= self.speed
        elif direction == "right":
            self.rect.x += self.speed

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()  # Add a clock to control the frame rate
    player = Player(image="assets/starship.png")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move("left")
                elif event.key == pygame.K_RIGHT:
                    player.move("right")

        screen.fill((0, 0, 0))  # Fill the screen with a black color
        screen.blit(player.image, player.rect)  # Draw the player on the screen
        
        pygame.display.flip()
        clock.tick(30)  # Set the frame rate to 30 frames per second

if __name__ == "__main__":
    main()

    
        