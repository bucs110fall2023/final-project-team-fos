import pygame

pygame.init()
screen = pygame.display.set_mode((600,600))

a = 250

hitboxes = {
    "red" : pygame.Rect(a,0,100,100),
    "white" : pygame.Rect(a,500,100,100)
}

main_colors = {
    "white" : ("white"),
    "red": ("red")
}


running = True

while running:
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for color in hitboxes:
                    pygame.draw.rect(screen, main_colors[color], hitboxes[color])
                    pygame.display.flip()
                    pygame.time.delay(1)
            if event.key == pygame.K_LEFT:
                a = a - 20
                pygame.display.flip()
                    
    