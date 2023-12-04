import pygame
import random
from pygame import mixer
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
    self.number_of_times_2 = []
    self.number_of_times_3 = []
    self.number_of_abilitybox = []
    self.shield_list = []
    self.speed_list = []
    self.shoot_list = []
    for n in range(2):
      self.enemies.add(Enemy(random.randint(0,575),-50))
    self.STATE = "MENU"
    background_image = pygame.image.load("assets/background.jpg")
    self.image = pygame.transform.scale(background_image, (600,600))
    self.rect = self.image.get_rect()
    mixer.music.load("assets/posterity.mp3")
    mixer.music.play(-1)
    
  def mainloop(self):
  
    while True:
      if self.STATE == "MENU":
        self.menuloop()
      if self.STATE == "GAME":
        self.gameloop()
      if self.STATE == "GAMEOVER":
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
            gamestart_sound = mixer.Sound("assets/gamestart_sound.wav")
            gamestart_sound.play()
            self.STATE = "GAME"
      
      self.screen.fill((0,0,0))
      self.font = pygame.font.Font("assets/Inversionz.ttf", 70)
      self.game_name = self.font.render("SPACEWAR", True, "white")
      self.font = pygame.font.Font("assets/Inversionz.ttf", 40)
      self.starting_text =self.font.render("press [space] to play", True, "white")
      self.screen.blit(self.starting_text, (30,450))
      self.screen.blit(self.game_name, (125,150))
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
    changed = False
    self.time_in_the_menuloop = pygame.time.get_ticks()
    self.speed = 10
    
    while self.STATE == "GAME":
        
        self.time_in_the_gameloop = pygame.time.get_ticks()
        
        
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
                lasershot_sound = mixer.Sound("assets/lasershot_sound.wav")
                lasershot_sound.play()
                self.laserbeam.rect.x = self.player.rect.x + 22
                self.laserbeam.rect.y = self.player.rect.y
                self.check = True
                if self.shoot_list == [1,1]:
                  self.laserbeam.rect.x = self.player.rect.x + 15
                  self.laserbeam.rect.y = self.player.rect.y
                  self.laserbeam.surface_obj =pygame.Surface((20,40)) 
                  self.laserbeam.surface_obj.fill("lime")
                
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
          
        # Fill the screen with a black color
        self.screen.blit(self.image, self.rect)
          
        #Shooting laserbeams
        if self.check and self.shoot_list == [1]: 
          
          new_laserbeam_1 = Laserbeam(pos_x = self.player.rect.x + 22 ,pos_y = self.player.rect.y)
          self.laserbeams.add(new_laserbeam_1)
          self.laserbeam.rect.y -= 50
          self.screen.blit(self.laserbeam.surface_obj, self.laserbeam.rect)
          
          if self.laserbeam.rect.y <= 0 :
            
            self.laserbeam.kill()
            self.check = False
            self.laserbeam.rect.x = self.player.rect.x + 22
            self.laserbeam.rect.y = self.player.rect.y
          
          for enemy in self.enemies:
            if pygame.sprite.collide_rect(self.laserbeam, enemy):
              explosion_sound = mixer.Sound("assets/explosion_sound.wav")
              explosion_sound.play()
              self.laserbeam.kill()
              self.check = False
              enemy.kill() 
              self.enemies.add(Enemy(random.randint(0,575),-50))
          
          for laserbeam in self.laserbeams:
            laserbeam.kill()
        
        if self.check and self.shoot_list == [1,1]: 
          
          new_laserbeam_1 = Laserbeam(pos_x = self.player.rect.x + 22 ,pos_y = self.player.rect.y)
          self.laserbeams.add(new_laserbeam_1)
          mask_surface = pygame.Surface((10, 40))
          mask_surface.fill("black")
          self.laserbeam.rect.y -= 50
          self.screen.blit(self.laserbeam.surface_obj, self.laserbeam.rect)
          self.screen.blit(mask_surface, (self.laserbeam.rect.x + 5, self.laserbeam.rect.y))
          
          if self.laserbeam.rect.y <= 0 :
            
            self.laserbeam.kill()
            self.check = False
            self.laserbeam.rect.x = self.player.rect.x + 22
            self.laserbeam.rect.y = self.player.rect.y 
          
          for enemy in self.enemies:
            if pygame.sprite.collide_rect(self.laserbeam, enemy):
              explosion_sound = mixer.Sound("assets/explosion_sound.wav")
              explosion_sound.play()
              self.laserbeam.kill()
              self.check = False
              enemy.kill() 
              self.enemies.add(Enemy(random.randint(0,575),-50))
          
          for laserbeam in self.laserbeams:
            laserbeam.kill()
        
        #update data for enemies
        for enemy in self.enemies:
          enemy.rect.y += self.speed
          if 500 < enemy.rect.y <= 512:
            for n in range(1):
              self.enemies.add(Enemy(random.randint(0,575),0))
          if enemy.rect.y >= 650:
            enemy.kill()

        if 20000 < self.time_in_the_gameloop - self.time_in_the_menuloop <= 40000 and self.number_of_times_2==[] :
          for n in range(2):
            self.enemies.add(Enemy(random.randint(0,575),-50))
          self.number_of_times_2.append(1)
          self.speed = 11
          self.abilityboxes.add(Abilitybox(random.randint(0,575),-50))
        
        if 50000 < self.time_in_the_gameloop - self.time_in_the_menuloop <= 70000 and self.number_of_times_3==[] :
          for n in range(2):
            self.enemies.add(Enemy(random.randint(0,575),-50))
          self.number_of_times_3.append(1)
          self.speed = 12
          self.abilityboxes.add(Abilitybox(random.randint(0,575),-50))
        
        for enemy in self.enemies:
          if pygame.sprite.collide_rect(self.player, enemy) and self.shield_list ==[] :
              gameover_sound = mixer.Sound("assets/gameover_sound.wav")
              gameover_sound.play()
              self.player.kill()
              self.STATE = "GAMEOVER"    
              
        for enemy in self.enemies:
          if pygame.sprite.collide_rect(self.player, enemy) and self.shield_list ==[1]:
            self.shield_list.remove(1)
            gameover_sound = mixer.Sound("assets/gameover_sound.wav")
            gameover_sound.play()
            enemy.kill()
            self.player.kill()
            self.player.image = pygame.transform.scale( pygame.image.load("assets/starship.png"), (50,80))
            self.player.add()
            for n in range(1):
              self.enemies.add(Enemy(random.randint(0,575),0))
              
        for enemy in self.enemies:
          if pygame.sprite.collide_rect(self.player, enemy) and self.shield_list ==[1,1]:
            self.shield_list.remove(1)
            gameover_sound = mixer.Sound("assets/gameover_sound.wav")
            gameover_sound.play()
            enemy.kill()
            self.player.kill()
            self.player.image = pygame.transform.scale( pygame.image.load("assets/starship_shielded.png"), (50,80))
            self.player.add()
            for n in range(1):
              self.enemies.add(Enemy(random.randint(0,575),0))
        
        # Update data for abilitybox
        for abilitybox in self.abilityboxes:
            
            abilitybox.rect.y = abilitybox.rect.y + 3
            
            if not changed:
              abilitybox.image_path = random.choice([ "assets/ability_shoot.png","assets/ability_speed.png","assets/ability_shield.png"])
              original_image = pygame.image.load(abilitybox.image_path)
              abilitybox.image = pygame.transform.scale(original_image, (30,30))
              changed = True
            
            if pygame.sprite.collide_rect(self.player, abilitybox) and abilitybox.image_path == "assets/ability_shoot.png":
              self.shoot_list.append(1)
              if self.shoot_list == [1]:
                shield_sound = mixer.Sound("assets/shield_sound.wav")
                shield_sound.play()
                self.shootinglaser = True
                abilitybox.kill()
                changed = False
              if self.shoot_list == [1,1]:
                shield_sound = mixer.Sound("assets/shield_sound.wav")
                shield_sound.play()
                self.shootinglaser = True
                abilitybox.kill()
                changed = False
                
            if pygame.sprite.collide_rect(self.player, abilitybox) and abilitybox.image_path == "assets/ability_speed.png":
              self.speed_list.append(1)
              if self.speed_list == [1]:
                shield_sound = mixer.Sound("assets/shield_sound.wav")
                shield_sound.play()
                self.player.speed = 8
                abilitybox.kill()
                changed = False
              if self.speed_list == [1,1]:
                shield_sound = mixer.Sound("assets/shield_sound.wav")
                shield_sound.play()
                self.player.speed = 10
                abilitybox.kill()
                changed = False
                
            if pygame.sprite.collide_rect(self.player, abilitybox) and abilitybox.image_path == "assets/ability_shield.png":
              self.shield_list.append(1)
              if self.shield_list == [1]:
                shield_sound = mixer.Sound("assets/shield_sound.wav")
                shield_sound.play()
                shielded_image = pygame.image.load("assets/starship_shielded.png")
                self.player.image = pygame.transform.scale(shielded_image, (50,80))
              if self.shield_list == [1,1]:
                shield_sound = mixer.Sound("assets/shield_sound.wav")
                shield_sound.play()
                shielded_image = pygame.image.load("assets/starship_shielded_2.png")
                self.player.image = pygame.transform.scale(shielded_image, (50,80))
              abilitybox.kill()
              changed = False
            if abilitybox.rect.y >= 650:
              abilitybox.kill()
              
        #Fill the screen with player
        self.screen.blit(self.player.image, self.player.rect) 
        
        #Fill the screen with enemies
        for enemy in self.enemies:
          self.screen.blit(enemy.image, enemy.rect) 
          
        #Fill the screen with abilitybox
        for abilitybox in self.abilityboxes:
          self.screen.blit(abilitybox.image,abilitybox.rect)
          
        pygame.display.flip() #redraw
        self.clock.tick(30)  # Set the frame rate to 30 frames per second


    
  def gameoverloop(self):
    
    while self.STATE == "GAMEOVER" :
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            self.STATE = "MENU"
          
          
      self.font = pygame.font.Font("assets/Inversionz.ttf", 40)
      self.screen.fill((0,0,0))
      
      if (self.time_in_the_gameloop - self.time_in_the_menuloop)/1000 <= 45:
        self.comment = "try better next time"
        self.end_comment = self.font.render(self.comment, True, "white")
        self.score = f"you survived {(self.time_in_the_gameloop - self.time_in_the_menuloop)//1000+1} seconds"
        self.end_score = self.font.render(self.score, True, "white")
        self.screen.blit(self.end_score, (9,150))
        self.screen.blit(self.end_comment, (40,450))
        pygame.display.flip()
      
      if 45 <(self.time_in_the_gameloop - self.time_in_the_menuloop)/1000 <= 90:
        self.comment = "semi pro"
        self.end_comment = self.font.render(self.comment, True, "white")
        self.score = f"you survived {(self.time_in_the_gameloop - self.time_in_the_menuloop)//1000+1} seconds"
        self.end_score = self.font.render(self.score, True, "white")
        self.screen.blit(self.end_score, (9,150))
        self.screen.blit(self.end_comment, (190,450))
        pygame.display.flip()
      
      if (self.time_in_the_gameloop - self.time_in_the_menuloop)/1000 > 90:
        self.comment = "pro level"
        self.end_comment = self.font.render(self.comment, True, "white")
        self.score = f"you survived {(self.time_in_the_gameloop - self.time_in_the_menuloop)//1000+1} seconds"
        self.end_score = self.font.render(self.score, True, "white")
        self.screen.blit(self.end_score, (9,150))
        self.screen.blit(self.end_comment, (190,450))
        pygame.display.flip()
      
      
      #event loop

      #update data

      #redraw
