from setting import *
from common import common,Timer,Attack


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
   (320,32,32,32),
   (352,32,32,32),
   
]



class Character:
   def __init__(self, position,player) -> None:
      
      self.character_image = character_image+"_"+ str(player) + ".png"
      
      self.target = []
      self.player = player
      self.hp = 100

      self.sprite = common()
      self.image ={
         "idle": self.sprite.sprite_sheet(self.character_image,idle_sprite,False),
         "move": self.sprite.sprite_sheet(self.character_image,moving_sprite,False),
         "attack": self.sprite.sprite_sheet(self.character_image,attack_sprite,False)
         
         
      }

      self.timer = {
         "attack": Timer(attack_time_cooldown),
         "idel": Timer(2000),
         
      }

      self.attack = Attack(self, self.target)



      self.image_index = 0
      self.rect = self.image["idle"][self.image_index].get_rect(topleft=position)
      self.attacking = False
      self.current_state = "idle"
      self.last_state = "idle"
      self.face_right = True





   def update_timer(self):
      for timer in self.timer:
         self.timer[timer].update()
   

   def update(self): 
      key= pygame.key.get_pressed()

      if key[player_key[self.player]["left"]]:
         self.rect.x -= 1
         self.face_right = False
         self.current_state = "move"
      elif key[player_key[self.player]["right"]]:
         self.rect.x += 1
         self.face_right = True
         self.current_state = "move"
      elif key[player_key[self.player]["up"]]:
         self.rect.y -= 1
         self.current_state = "move"
      elif key[player_key[self.player]["down"]]:
         self.rect.y += 1
         self.current_state = "idle"

      elif key[player_key[self.player]["attack"]] and not self.timer["attack"].active :
         self.current_state = "attack"
         self.attack.attack()
         self.timer["attack"].activate()
      
      else :
         self.timer["idel"].activate()
      
      self.update_timer()
      self.selectAnimation()



   def jump(self):
      pass




   



   def selectAnimation(self):
      if self.current_state =="attack": 
            if self.last_state != "attack":
               self.image_index = 0
               self.last_state = "attack"
         
            self.image_index += 0.004
            if self.image_index >= len(self.image["attack"]):
               self.image_index = 0
               self.current_state = "idle"
               
      
      elif self.current_state == "move":
         if self.last_state != "move":
            self.image_index = 0
            self.last_state = "move"
         self.image_index += frame_rate
         if self.image_index >= len(self.image["move"]):
            self.image_index = 0
      
      elif self.current_state == "idle":
         if self.last_state != "idle":
            self.image_index = 0
            self.last_state = "idle"
         if  self.timer["idel"].active:
            self.image_index += frame_rate
            if self.image_index >= len(self.image["idle"]):
               self.image_index = 0
         
       
   def hp_draw(self,displaySurface):
      hp_width = 120
      current_hp = self.hp/100 * hp_width
      pygame.draw.rect(displaySurface, (255,0,0), (self.rect.x , self.rect.y + 16, hp_width, 5))
      pygame.draw.rect(displaySurface, (0,255,0), (self.rect.x, self.rect.y + 16, current_hp, 5))

   def attack_cooldown(self,displaySurface):
      cooldown_width = 120
      current_cooldown = self.timer["attack"].time_left/attack_time_cooldown * cooldown_width
      pygame.draw.rect(displaySurface, (0,0,255), (self.rect.x, self.rect.y +10, cooldown_width, 5))
      pygame.draw.rect(displaySurface, (255,255,0), (self.rect.x, self.rect.y + 10,cooldown_width- current_cooldown, 5))

   def draw(self,displaySurface):
      self.hp_draw(displaySurface)
      self.attack_cooldown(displaySurface)
      image = self.image[self.current_state][int(self.image_index)]
      if self.face_right == False:
         image = pygame.transform.flip(image, True, False)
      
      displaySurface.blit(pygame.transform.scale( image, (128,128)), self.rect)

      




