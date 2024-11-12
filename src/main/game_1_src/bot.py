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
   (0,192,32,32),
   (32,192,32,32),
   
]


class Bot:
   def __init__(self, position) -> None:
      botImage = pygame.image.load(character_image).convert_alpha()
      
      
      

      self.sprite = common()
      
      self.attack = self.sprite.sprite_sheet(character_image, attack_sprite, False)
      self.attack_flipped = self.sprite.sprite_sheet(character_image, attack_sprite, True)
      self.attack_index = 0
      

      self.moving = self.sprite.sprite_sheet(character_image, moving_sprite, False)
      self.moving_flipped = self.sprite.sprite_sheet(character_image, moving_sprite, True)
      self.moving_index = 0

      self.idle = self.sprite.sprite_sheet(character_image, idle_sprite, False)
      self.idle_index = 0

      self.current_animation = "idle"
      self.image = self.moving[self.moving_index]
      self.rect = self.image.get_rect(topleft=position)

      self.last_update = pygame.time.get_ticks()
      self.frame_rate = 1000 // 10  



   def update(self): 
      key = pygame.key.get_pressed()
      if key[pygame.K_SPACE]:
         
         self.current_animation = "attack"

      elif key[pygame.K_RIGHT]:
         self.rect.x += 1
         self.current_animation = "moving_right"
      
      elif key[pygame.K_LEFT]:
         self.rect.x -= 1
         self.current_animation = "moving_left"
      
      elif key[pygame.K_UP]:
         self.rect.y -= 1
         self.current_animation = "moving_up"

      elif key[pygame.K_DOWN]:
         self.rect.y += 1
         self.current_animation = "moving_down"

      else  :
         self.current_animation = "idle"
      
 
      self.selectAnimation()


   def jump(self):
      pass

   def selectAnimation(self):
      current_time = pygame.time.get_ticks()
      if current_time - self.last_update > self.frame_rate:
         self.last_update = current_time
         if self.current_animation == "attack":
            self.attack_index += 1
            if self.attack_index >= len(self.attack):
               self.attack_index = 0
            self.image = self.attack[self.attack_index]
         
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



   def draw(self,displaySurface):
      self.image = pygame.transform.scale(self.image, (64, 64))
      displaySurface.blit(self.image, self.rect)
      print(self.rect.x , self.rect.y)




