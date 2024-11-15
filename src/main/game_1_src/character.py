from setting import *
from common import common,Timer,Attack,Bullet


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
      self.hp = hp_character

      self.sprite = common()
      self.image ={
         "idle": self.sprite.sprite_sheet(self.character_image,idle_sprite,False),
         "move": self.sprite.sprite_sheet(self.character_image,moving_sprite,False),
         "attack": self.sprite.sprite_sheet(self.character_image,attack_sprite,False)
         
         
      }

      self.timer = {
         "attack": Timer(attack_time_cooldown),
         "idel": Timer(2000),
         "bullet": Timer(bullet_time_cooldown),
         "jump": Timer(500),
      }




      self.image_index = 0
      self.rect = {
         "x": position[0],
         "y": position[1],
         "width": 32,
         "height": 32
      }


      
      self.attacking = False
      self.current_state = "idle"
      self.last_state = "idle"
      self.face_right = True
     

      self.attack = Attack(self, self.target)
      self.bullet_store = []





   def update_timer(self):
      for timer in self.timer:
         self.timer[timer].update()
   

   def update(self): 
      key= pygame.key.get_pressed()

      if key[player_key[self.player]["left"]]:
         self.rect["x"] -= move_speed
         
         self.face_right = False
         self.current_state = "move"

      elif key[player_key[self.player]["right"]]:
         self.rect["x"] += move_speed
         
         self.face_right = True
         self.current_state = "move"

      elif key[player_key[self.player]["up"]] and not self.timer["jump"].active and self.rect["y"] == 400:
         self.rect["y"] -= move_speed
         
         self.timer["jump"].activate()
         self.current_state = "move"

      elif key[player_key[self.player]["down"]]:
         self.hp += 0.005
         if self.hp >= hp_character:
            self.hp = hp_character
         self.current_state = "move"

      elif key[player_key[self.player]["attack"]] and not self.timer["attack"].active :
         self.current_state = "attack"
         self.attack.attack()
         self.timer["attack"].activate()

      elif key[player_key[self.player]["shoot"]] and not self.timer["bullet"].active:
         bullet = Bullet(self,self.target) 
         self.timer["bullet"].activate()
         self.bullet_store.append(bullet)  
      
      elif key[player_key[self.player]["flash"]] :
         if self.face_right:
            self.rect["x"] += flash_speed
         else:
            self.rect["x"] -= flash_speed
         self.current_state = "move"
      
      
      else :
         self.timer["idel"].activate()
         
      
      self.update_timer()
      self.selectAnimation()
      self.update_bullet()
      self.jump()
      



   def jump(self):
      if self.timer["jump"].active:
         self.rect["y"] -= 0.5
      
      if self.timer["jump"].active == False:
         self.rect["y"] += 0.6
         if self.rect ["y"] >= 400:
            self.rect["y"] = 400
           

          




   



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
         
       


   def update_bullet(self):
      for  bullet in self.bullet_store :
         bullet.update()


   
      
   def hp_draw(self,displaySurface):
      
      current_hp = self.hp / hp_character * hp_width
      pygame.draw.rect(displaySurface, (255,0,0), (self.rect["x"] , self.rect["y"] + 16, hp_width, 5))
      pygame.draw.rect(displaySurface, (0,255,0), (self.rect["x"], self.rect["y"] + 16, current_hp, 5))

   def attack_cooldown(self,displaySurface):
      
      current_cooldown = self.timer["bullet"].time_left/bullet_time_cooldown * cooldown_width
      pygame.draw.rect(displaySurface, (255,255,255), (self.rect["x"], self.rect["y"] +10, cooldown_width, 5))
      pygame.draw.rect(displaySurface, (0,0,255), (self.rect["x"], self.rect["y"] + 10,cooldown_width- current_cooldown, 5))

   def draw(self,displaySurface):
      if self.hp <= 0: 
         return
      self.hp_draw(displaySurface)
      self.attack_cooldown(displaySurface)
      
      for bullet in self.bullet_store:
         bullet.draw(displaySurface)


      image = self.image[self.current_state][int(self.image_index)]
      if self.face_right == False:
         image = pygame.transform.flip(image, True, False)
      
      if self.rect["x"] < 0:
         self.rect["x"] = 0
      if self.rect["x"] > window_width - character_width:
         self.rect["x"] = window_width - character_width
      print(image.get_width(),image.get_height())
      displaySurface.blit( pygame.transform.scale(image,(character_width,character_height)), (self.rect["x"], self.rect["y"],self.rect["width"],self.rect["height"]))

      




