import pygame
import random
from src.player import Player
from src.enemy import Enemy

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    self.screen = pygame.display.set_mode((600,600))
    self.player = Player()
    self.enemy = Enemy()
    self.clock = pygame.time.Clock()
    self.enemies = pygame.sprite.Group()
    self.font = pygame.font.Font(None, 48)
    self.text = self.font.render("press SPACE to start!", True, "white")
    self.number_of_times_2 = []
    self.number_of_times_3 = []
    self.current_time =0
    for n in range(2):
        self.enemies.add(Enemy(random.randint(0,575),-50))
    self.STATE = "MENU"
    
    
    
  def mainloop(self):
  
    while True:
      if self.STATE == "MENU":
        self.menuloop()
      elif self.STATE == "GAME":
        self.gameloop()
      # elif self.STATE == "GAMEOVER":
      #   self.gameoverloop()
    #select state loop
    
  
  ### below are some sample loop states ###
  

  def menuloop(self):
    
    while self.STATE == "MENU":
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            self.STATE = "GAME"
      
      self.screen.fill((0,0,0))
      self.screen.blit(self.text, (140,150))
      pygame.display.flip()
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
    
    while self.STATE == "GAME":
        
        current_time = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.rect.x -= self.player.speed
                if event.key == pygame.K_RIGHT:
                    self.player.rect.x += self.player.speed

        for enemy in self.enemies:
            enemy.rect.y = enemy.rect.y + 10
        
        self.screen.fill((0,0,0))  # Fill the screen with a black color

        self.screen.blit(self.player.surface_obj, self.player.rect)
        
        for enemy in self.enemies:
            self.screen.blit(enemy.surface_obj, enemy.rect) 
        
        for enemy in self.enemies:
            if enemy.rect.y == 500:
                for n in range(1):
                    self.enemies.add(Enemy(random.randint(0,575),0))
            if enemy.rect.y == 650:
                enemy.kill() 
                
        if 10000 < current_time <= 20000 and self.number_of_times_2==[] :
            for n in range(2):
                self.enemies.add(Enemy(random.randint(0,575),-50))
            self.number_of_times_2.append(1)
        
        if  20000 < current_time <= 30000 and self.number_of_times_3==[] :
            for n in range(2):
                self.enemies.add(Enemy(random.randint(0,575),-50))
            self.number_of_times_3.append(1)
                
        pygame.display.flip()
        self.clock.tick(30)  # Set the frame rate to 30 frames per second
    
      #event loop

      #update data

      #redraw
    
  # def gameoverloop(self):
  #     #event loop

  #     #update data

  #     #redraw
