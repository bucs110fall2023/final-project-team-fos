import pygame
from player import Player

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    
  def mainloop(self):
    while True:
      if self.STATE == "MENU":
        self.menuloop()
      elif self.STATE == "GAME":
        self.gameloop()
      elif self.STATE == "GAMEOVER":
        self.gameoverloop()
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    while self.STATE == "MENU":
      for event in pygame.evnt.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            self.STATE == "GAME"
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
    player = Player()
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
    
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw