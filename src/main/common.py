from setting import *

class common: 
   def __init__(self):
      pass 
   def draw_button(self, image_path, x, y, width, height):
      button = pygame.Rect(x, y, width, height)
      self.window.blit(pygame.image.load(image_path), (x, y))
      
