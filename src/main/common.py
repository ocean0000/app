from setting import *





class common: 
   def __init__(self):
      pass 

   def draw_button(self, image_path, x, y,displaySurface):
      button = pygame.image.load(image_path)
      button_rect = button.get_rect(topleft=(x, y))
      displaySurface.blit(button, (x, y))
      return button_rect

   def sprite_sheet(self, image_path, sprite_position, flipped):
      sprite_image = pygame.image.load(image_path).convert_alpha()
      sprites =[]
      sprites_flipped = []
      for position in sprite_position:
         sprite = sprite_image.subsurface(position)
         sprites.append(sprite)
         sprite_flipped = pygame.transform.flip(sprite, True, False)
         sprites_flipped.append(sprite_flipped)
      if flipped:
         return sprites_flipped
      else:
         return sprites
   
   



class Timer():
   def __init__(self,duration):
      self.duration = duration
      self.start_time =0 
      self.active = False
      self.time_left = 0

   def activate(self):
      self.active = True
      self.start_time = pygame.time.get_ticks()

   def deactivate(self):
      self.active = False
      self.start_time = pygame.time.get_ticks()

   def update(self):
      current_time = pygame.time.get_ticks()

      if self.active:
         self.time_left = self.duration - (current_time - self.start_time)
         if self.time_left <=0:
            self.deactivate()
            self.time_left = 0
      else:
         self.time_left = 0

class Attack():
   def __init__(self, player, target) -> None:
      self.player = player
      self.target = target
      
      self.damage = 10
      self.timer = Timer(attack_time)
      self.space = None


   def attack(self):
      self.timer.update()
      if self.player.face_right:
         self.space = pygame.Rect(self.player.rect["x"] + self.player.rect["width"], self.player.rect["y"]-16, attack_range_width, attack_range_height)
      else:
         self.space = pygame.Rect(self.player.rect["x"] - attack_range_width, self.player.rect["y"] -16, attack_range_width, attack_range_height)
      for obj in self.target:
         print(self.timer.active)
         if self.space.colliderect(obj.rect["x"], obj.rect["y"],obj.rect["width"],obj.rect["height"]) and not self.timer.active:
            obj.hp -= self.damage
            if obj.hp <=0:
               self.target.remove(obj)
               return

            print(f"Player {self.player.player} Attack Player {obj.player} Health {obj.hp}")
            self.timer.activate()

class Bullet():
   def __init__(self,player,target) :
      self.player= player
      self.target = target
      self.bullet_image =bullet_image +"_" +str(player.player) + ".png"
      
      self.face_right = self.player.face_right

      
      if self.face_right:
         self.x = self.player.rect["x"] + 100
         self.y = self.player.rect["y"] + 100//2 
      else:
         self.x = self.player.rect["x"]
         self.y = self.player.rect["y"] + 100//2 
      
      
      self.width = 32
      self.height = 32
      self.space = None

      
      self.image = pygame.image.load(self.bullet_image)
      
   
   def update(self):
      if self.face_right:
         self.x+= bullet_speed
      else:
         self.x-= bullet_speed

      self.space = pygame.Rect(self.x, self.y, self.width, self.height)

      for obj in self.target:
        print(self.space)
        print((obj.rect["x"], obj.rect["y"],character_width,character_height))
        if self.space.colliderect(obj.rect["x"], obj.rect["y"],character_width,character_height):
            obj.hp -= 10
            if obj.hp <=0:
               self.target.remove(obj)
               self.player.bullet_store.remove(self)
               return
           
           
            print(f"Player {self.player.player} Attack Player {obj.player} Health {obj.hp}")
            self.player.bullet_store.remove(self)
            return

      if self.x >= window_width or self.x <=0 : 
         self.player.bullet_store.remove(self)

   def draw(self,displaySurface):
      displaySurface.blit(self.image, (self.x, self.y))
      

