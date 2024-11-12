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
   
      

      
