import pygame

pygame.init()
screen = pygame.display.set_mode((600,600))

a = 275

hitboxes = {
    "red" : pygame.Rect(a,0,50,50),
    "white" : pygame.Rect(a,500,50,50)
}

main_colors = {
    "white" : ("white"),
    "red": ("red")
}


running = True
times_used=[]

while running:
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                screen.fill("black")
                a = a - 20
                pygame.draw.rect(screen, "white", (a,500, 50,50))
                pygame.draw.rect(screen, "red", hitboxes["red"])
                pygame.display.flip()
            if event.key == pygame.K_RIGHT:
                screen.fill("black")
                a = a + 20
                pygame.draw.rect(screen, "white", (a,500, 50,50))
                pygame.draw.rect(screen, "red", hitboxes["red"])
                pygame.display.flip()
            if event.key == pygame.K_SPACE and times_used==[]:
                for color in hitboxes:
                    pygame.draw.rect(screen, main_colors[color], hitboxes[color])
                    pygame.display.flip()
                    pygame.time.delay(1)
                times_used.append(1)
            if event.key == pygame.K_SPACE:
                for n in range(9 ):
                    b = 450-50*n
                    screen.fill("black")
                    pygame.draw.rect(screen, "white", (a,500, 50,50))
                    pygame.draw.rect(screen, "red", hitboxes["red"])
                    pygame.draw.rect(screen , "green", (a+20, b, 10, 50))
                    pygame.display.flip()
                    pygame.time.delay(70)
                    if b == 50:
                        screen.fill("black")
                        pygame.draw.rect(screen, "white", (a,500, 50,50))
                        pygame.display.flip()
                        
                
                
                
                
                
    