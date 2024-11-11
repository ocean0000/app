from setting import *


class Bot:
   def __init__(self, position) -> None:
      self.botImage = pygame.image.load("storage/image/button/button_start.png").convert_alpha()
      self.botImage = pygame.transform.scale(self.botImage, (100, 100))
      self.rect = self.botImage.get_rect(topleft=position)
      self.gravity = 1
      self.isJumping = False
      self.jumpCount = 10

   def update(self): 
      pass



   def jump(self):
      pass


   
   def draw(self,displaySurface):
      displaySurface.blit(self.botImage, self.rect)




