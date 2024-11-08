from setting import *

class common: 
   def __init__(self):
      pass 

   def draw_button(self, image_path, x, y, width, height):
      button = pygame.image.load(image_path)
      
      button_rect = button.get_rect(topleft=(x, y))
      self.window.blit(button, (x, y))
      return button_rect



      
