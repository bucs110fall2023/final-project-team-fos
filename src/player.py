import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))

class Player(pygame.sprite.Sprite):
    def __init__(self, x=275, y=500, width=50, height=50, image_path="assets/starship.png"):
        super().__init__()
        original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(original_image, (width, height))  # Resize the image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

def main():
    player = Player(width=70, height=70)  # Set the desired width and height
    all_sprites = pygame.sprite.Group(player)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        screen.fill('black')  
        # Draw all sprites, including the player's image
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(30)  # Limit frames per second

    pygame.quit()
    

if __name__ == "__main__":
    main()