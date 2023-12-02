import pygame
import random
from src.player import Player
from src.enemy import Enemy
from src.laserbeam import Laserbeam
from src.abilitybox import Abilitybox

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    self.screen = pygame.display.set_mode((600,600))
    self.clock = pygame.time.Clock()
    self.player = Player()
    self.enemy = Enemy()
    self.laserbeam = Laserbeam()
    self.abilitybox = Abilitybox()
    self.enemies = pygame.sprite.Group()
    self.laserbeams = pygame.sprite.Group()
    self.abilityboxes = pygame.sprite.Group()
    self.font = pygame.font.Font(None, 48)
    self.starting_text = self.font.render("press SPACE to start!", True, "white")
    self.number_of_times_2 = []
    self.number_of_times_3 = []
    for n in range(2):
      self.enemies.add(Enemy(random.randint(0,575),-50))
    self.abilityboxes.add(Abilitybox(random.randint(0,575),-50))
    self.STATE = "MENU"
    
    
    
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
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            self.STATE = "GAME"
      
      self.screen.fill((0,0,0))
      self.screen.blit(self.starting_text, (140,150))
      pygame.display.flip()
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
    
    self.key_left_pressed = False
    self.key_right_pressed = False
    self.key_s_pressed = False
    self.check = False
    self.shootinglaser = False
    
    while self.STATE == "GAME":
        
        current_time = pygame.time.get_ticks()
        
        #event loop
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                self.key_left_pressed = True
              if event.key == pygame.K_RIGHT:
                self.key_right_pressed = True
              if event.key == pygame.K_s and not self.check and self.shootinglaser == True :
                self.laserbeam.rect.x = self.player.rect.x + 22
                self.laserbeam.rect.y = self.player.rect.y
                self.check = True
          if event.type == pygame.KEYUP:
              if event.key == pygame.K_LEFT:
                self.key_left_pressed = False
              if event.key == pygame.K_RIGHT:
                self.key_right_pressed = False
        
        if self.key_left_pressed:
          self.player.rect.x -= self.player.speed
        if self.key_right_pressed:
          self.player.rect.x += self.player.speed
        
        #update data for enemies
        for enemy in self.enemies:
          enemy.rect.y += 10
        
        for enemy in self.enemies:
          if enemy.rect.y >= 500:
            for n in range(1):
              self.enemies.add(Enemy(random.randint(0,575),0))
          if enemy.rect.y >= 650:
            enemy.kill()
        
        if 10000 < current_time <= 20000 and self.number_of_times_2==[] :
          for n in range(2):
            self.enemies.add(Enemy(random.randint(0,575),-50))
          self.number_of_times_2.append(1)
        
        if 20000 < current_time <= 30000 and self.number_of_times_3==[] :
          for n in range(2):
            self.enemies.add(Enemy(random.randint(0,575),-50))
          self.number_of_times_3.append(1)

        for enemy in self.enemies:
          if pygame.sprite.collide_rect(self.player, enemy):
              self.player.kill()
              self.STATE = "GAMEOVER"    
        
        # Update data for abilitybox
        for abilitybox in self.abilityboxes:
          abilitybox.rect.y += 10
          if pygame.sprite.collide_rect(self.player, abilitybox):
            self.shootinglaser = True
            # for n in range(1):
            #   self.abilityboxes.add(Abilitybox(random.randint(0,575),0))
          if abilitybox.rect.y >= 650:
              abilitybox.kill()
        
        
        # Fill the screen with a black color
        self.screen.fill((0,0,0))  
        
        #Fill the screen with abilitybox
        self.screen.blit(self.abilitybox.surface_obj,self.abilitybox.rect)
        
        #Fill the screen with enemies
        for enemy in self.enemies:
          self.screen.blit(enemy.surface_obj, enemy.rect) 
        
        #Fill the screen with player
        self.screen.blit(self.player.surface_obj, self.player.rect) 
        
        #Shooting laserbeams
        if self.check: 
          
          new_laserbeam = Laserbeam(self.player.rect.x + 22 ,self.player.rect.y)
          self.laserbeams.add(new_laserbeam)
          self.laserbeam.rect.y -= 30
          self.screen.blit(self.laserbeam.surface_obj, self.laserbeam.rect)
          
          if self.laserbeam.rect.y <= 0 :
            
            self.laserbeam.kill()
            self.check = False
            self.laserbeam.rect.x = self.player.rect.x + 22
            self.laserbeam.rect.y = self.player.rect.y 
          
          for enemy in self.enemies:
            if pygame.sprite.collide_rect(self.laserbeam, enemy):
              self.laserbeam.kill()
              self.check = False
              enemy.kill() 
              self.enemies.add(Enemy(random.randint(0,575),-50))
        
        pygame.display.flip() #redraw
        self.clock.tick(30)  # Set the frame rate to 30 frames per second


    
  def gameoverloop(self):
    
    while self.STATE == "GAMEOVER":
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
      
      
      # self.ending_text = self.font.render("Well Played!")
      
      self.screen.fill((0,0,0))
      pygame.display.flip()
          
      #event loop

      #update data

      #redraw