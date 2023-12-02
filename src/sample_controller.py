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
    self.number_of_abilitybox = []
    self.shield =[]
    for n in range(2):
      self.enemies.add(Enemy(random.randint(0,575),-50))
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
    color_changed = False
    time_in_the_menuloop = pygame.time.get_ticks()
    self.speed = 10
    
    while self.STATE == "GAME":
        
        time_in_the_gameloop = pygame.time.get_ticks()
        
        
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
          self.player.rect.x = max(self.player.rect.x,0)
        if self.key_right_pressed:
          self.player.rect.x += self.player.speed
          self.player.rect.x = min(self.player.rect.x,600 - 50)
        
        #update data for enemies
        for enemy in self.enemies:
          enemy.rect.y += self.speed
          if 500 < enemy.rect.y <= 512:
            for n in range(1):
              self.enemies.add(Enemy(random.randint(0,575),0))
          if enemy.rect.y >= 650:
            enemy.kill()
        
        
        
        if 20000 < time_in_the_gameloop - time_in_the_menuloop <= 40000 and self.number_of_times_2==[] :
          for n in range(2):
            self.enemies.add(Enemy(random.randint(0,575),-50))
          self.number_of_times_2.append(1)
          self.speed = 11
          self.abilityboxes.add(Abilitybox(random.randint(0,575),-50))
        
        if 50000 < time_in_the_gameloop - time_in_the_menuloop <= 70000 and self.number_of_times_3==[] :
          for n in range(2):
            self.enemies.add(Enemy(random.randint(0,575),-50))
          self.number_of_times_3.append(1)
          self.speed = 12
          self.abilityboxes.add(Abilitybox(random.randint(0,575),-50))
        
        for enemy in self.enemies:
          if pygame.sprite.collide_rect(self.player, enemy) and self.shield ==[] :
              self.player.kill()
              self.STATE = "GAMEOVER"    
        
        for enemy in self.enemies:
          if pygame.sprite.collide_rect(self.player, enemy) and self.shield ==[1]:
            self.shield.remove(1)
            enemy.kill()
            self.player.kill()
            self.player.surface_obj.fill("white")
            self.player.add()
            for n in range(1):
              self.enemies.add(Enemy(random.randint(0,575),0))
              
        for enemy in self.enemies:
          if pygame.sprite.collide_rect(self.player, enemy) and self.shield ==[1,1]:
            self.shield.remove(1)
            enemy.kill()
            self.player.kill()
            self.player.surface_obj.fill("gold")
            self.player.add()
            for n in range(1):
              self.enemies.add(Enemy(random.randint(0,575),0))
        
        # Update data for abilitybox
        for abilitybox in self.abilityboxes:
            
            abilitybox.rect.y = abilitybox.rect.y + 3
            
            if not color_changed:
              abilitybox.abilitybox_color = random.choice(["lime","gold"])
              abilitybox.surface_obj.fill(abilitybox.abilitybox_color)
              color_changed = True
            
            if pygame.sprite.collide_rect(self.player, abilitybox) and abilitybox.abilitybox_color == "lime":
              self.shootinglaser = True
              self.player.surface_obj.fill("lime")
              abilitybox.kill()
            if pygame.sprite.collide_rect(self.player, abilitybox) and abilitybox.abilitybox_color == "darkorchid":
              self.player.speed = 10
              self.player.surface_obj.fill("darkorchid")
              abilitybox.kill()
            if pygame.sprite.collide_rect(self.player, abilitybox) and abilitybox.abilitybox_color == "gold":
              self.shield.append(1)
              self.player.surface_obj.fill("gold")
              abilitybox.kill()
            if abilitybox.rect.y >= 650:
              abilitybox.kill()
              
        
            
        
        
        # Fill the screen with a black color
        self.screen.fill((0,0,0))  
        
        # #Fill the screen with abilitybox
        # for abilitybox in self.abilityboxes:
        #   self.screen.blit(abilitybox.surface_obj,abilitybox.rect)
        
        #Fill the screen with enemies
        for enemy in self.enemies:
          self.screen.blit(enemy.surface_obj, enemy.rect) 
          
        #Fill the screen with abilitybox
        for abilitybox in self.abilityboxes:
          self.screen.blit(abilitybox.surface_obj,abilitybox.rect)
        
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
