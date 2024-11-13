from setting import *
from common import common


attack_sprite =[
   
   (32,96,32,32),
   (64,96,32,32),
   (96,96,32,32),
]

moving_sprite = [
   (0,32,32,32),
   (32,32,32,32),
   (64,32,32,32),
   (96,32,32,32),
]

idle_sprite = [
   (256,32,32,32),
   (288,32,32,32),
   
]



class Bot:
   def __init__(self, position,player) -> None:
      
      self.character_image = character_image+"_"+ str(player) + ".png"
      
      
      self.player = player
      self.hp = 100

      self.sprite = common()
      # attack
      self.attack = self.sprite.sprite_sheet(self.character_image, attack_sprite, False)
      self.attack_flipped = self.sprite.sprite_sheet(self.character_image, attack_sprite, True)
      self.attack_index = -1
      self.target_bot = None
      self.attack_cooldown = 1000
      self.last_attack =0
      
      
      # moving
      self.moving = self.sprite.sprite_sheet(self.character_image, moving_sprite, False)
      self.moving_flipped = self.sprite.sprite_sheet(self.character_image, moving_sprite, True)
      self.moving_index = -1

      # idle
      self.idle = self.sprite.sprite_sheet(self.character_image, idle_sprite, False)
      self.idle_index = -1

      # default
      self.current_animation = "idle"
      self.image = self.moving[self.moving_index]
      self.rect = self.image.get_rect(topleft=position)

      # frame rate
      self.last_update = pygame.time.get_ticks()
      self.frame_rate = 100

      # direction
      self.direction = "idle"


   def attack_target(self):
      if ((self.rect.x - self.target_bot.rect.x) ** 2 + (self.rect.y - self.target_bot.rect.y) ** 2) ** 0.5 <attack_range :
         
         if self.target_bot.hp > 0:
            self.target_bot.hp -= 10

   def update(self): 
      key = pygame.key.get_pressed()
      current_time = pygame.time.get_ticks()
      if self.player == 1:
         
         
         if key[pygame.K_KP1] :
            if current_time - self.last_attack > self.attack_cooldown:
               self.last_attack = current_time
               self.current_animation = "attack"
               self.attack_target()
            

         elif key[pygame.K_RIGHT]:
            self.rect.x += 1
            self.current_animation = "moving_right"
            self.direction = "right"
            self.attack_index = -1
         
         elif key[pygame.K_LEFT]:
            self.rect.x -= 1
            self.current_animation = "moving_left"
            self.direction = "left"
            self.attack_index = -1
         
         elif key[pygame.K_UP]:
            self.rect.y -= 1
            self.current_animation = "moving_up"
            self.attack_index = -1

         elif key[pygame.K_DOWN]:
            self.rect.y += 1
            self.current_animation = "moving_down"
            self.attack_index = -1

         else :
               self.current_animation = "idle"
               self.attack_index = -1
      
   
         self.selectAnimation()

      elif self.player == 2:
         key = pygame.key.get_pressed()
        
         if key[pygame.K_j] :
            if current_time - self.last_attack > self.attack_cooldown:
               self.last_attack = current_time
               self.current_animation = "attack"
               self.attack_target()

         elif key[pygame.K_d]:
            self.rect.x += 1
            self.current_animation = "moving_right"
            self.direction = "right"
            self.attack_index = -1
         
         elif key[pygame.K_a]:
            self.rect.x -= 1
            self.current_animation = "moving_left"
            self.direction = "left"
            self.attack_index = -1
         
         elif key[pygame.K_w]:
            self.rect.y -= 1
            self.current_animation = "moving_up"
            self.attack_index = -1

         elif key[pygame.K_s]:
            self.rect.y += 1
            self.current_animation = "moving_down"
            self.attack_index = -1

         else :
               self.current_animation = "idle"
               self.attack_index = -1
      
   
         self.selectAnimation()


   def jump(self):
      pass

   def selectAnimation(self):
      current_time = pygame.time.get_ticks()
      if current_time - self.last_update > self.frame_rate:
         
         self.last_update = current_time
         if self.current_animation == "attack":
            self.attack_index += 1
            if self.direction == "right":
               if self.attack_index >= len(self.attack):
                  self.attack_index = 0
               self.image = self.attack[self.attack_index]
            else :
               if self.attack_index >= len(self.attack_flipped):
                  self.attack_index = 0
               self.image = self.attack_flipped[self.attack_index]
         
         elif self.current_animation == "moving_right":
            self.moving_index += 1
            if self.moving_index >= len(self.moving):
               self.moving_index = 0
            self.image = self.moving[self.moving_index]
         
         elif self.current_animation == "moving_left":
            self.moving_index += 1
            if self.moving_index >= len(self.moving_flipped):
               self.moving_index = 0
            self.image = self.moving_flipped[self.moving_index]
         
         elif self.current_animation == "idle":
            self.idle_index += 1
            if self.idle_index >= len(self.idle):
               self.idle_index = 0
            self.image = self.idle[self.idle_index]
            
   


       
   def hp_draw(self,displaySurface):
      hp_width = 120
      current_hp = self.hp/100 * hp_width
      pygame.draw.rect(displaySurface, (255,0,0), (self.rect.x , self.rect.y + 16, hp_width, 5))
      pygame.draw.rect(displaySurface, (0,255,0), (self.rect.x, self.rect.y + 16, current_hp, 5))


   def draw(self,displaySurface):
      self.image = pygame.transform.scale(self.image, (128, 128))
      displaySurface.blit(self.image, self.rect)
      self.hp_draw(displaySurface)
      




