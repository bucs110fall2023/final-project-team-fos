import pygame

pygame.init()
screen = pygame.display.set_mode((600,600))

a = 275
x = 275

hitboxes = {
    "white" : pygame.Rect(x,500,50,50),
    "red" : pygame.Rect(a,0,50,50)
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
            if event.key == pygame.K_LEFT:
                screen.fill("black")
                x = x-20
                hitboxes["white"]= pygame.Rect(x,500,50,50)
                pygame.draw.rect(screen, main_colors["white"], hitboxes["white"])
                pygame.draw.rect(screen, main_colors["red"], hitboxes["red"])
                pygame.display.flip()
            if event.key == pygame.K_RIGHT:
                screen.fill("black")
                x = x+20
                hitboxes["white"]= pygame.Rect(x,500,50,50)
                pygame.draw.rect(screen, main_colors["white"], hitboxes["white"])
                pygame.draw.rect(screen, main_colors["red"], hitboxes["red"])
                pygame.display.flip()
            if event.key == pygame.K_s:
                for n in range(11):
                    y = 450-50*n
                    screen.fill("black")
                    pygame.draw.rect(screen, main_colors["white"], hitboxes["white"])
                    pygame.draw.rect(screen, main_colors["red"], hitboxes["red"])
                    pygame.draw.rect(screen , "green", (x+20, y, 10, 50))
                    pygame.display.flip()
                    pygame.time.delay(70)
                    if a <= x+20 <= a+50 and y == 50:
                        screen.fill("black")
                        main_colors["red"]="black"
                        pygame.draw.rect(screen, main_colors["white"], hitboxes["white"])
                        pygame.draw.rect(screen, main_colors["red"], hitboxes["red"])
                        pygame.display.flip()
                        
                
                
                
                
                
    