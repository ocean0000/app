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
      self.attack_range = attack_range
      self.damage = 10
      self.timer = Timer(attack_time)
      self.space = None


   def attack(self):
      self.timer.update()
      if self.player.face_right:
         self.space = pygame.Rect(self.player.rect.x + self.player.rect.width, self.player.rect.y, self.attack_range, self.player.rect.height)
      else:
         self.space = pygame.Rect(self.player.rect.x - self.attack_range, self.player.rect.y, self.attack_range, self.player.rect.height)
      for target in self.target:
         print(self.timer.active)
         if self.space.colliderect(target.rect) and not self.timer.active:
            target.hp -= self.damage
            print(f"Player {self.player.player} Attack Player {target.player} Health {target.hp}")
            self.timer.activate()
           
      
