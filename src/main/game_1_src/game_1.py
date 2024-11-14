from setting import * 
from .character import Character 

class Game_1:
   def __init__(self,displaySurface):
      self.background = pygame.image.load(game_1_background_image)
      self.background = pygame.transform.scale(self.background, (window_width, window_height))
      self.displaySurface  = displaySurface

      
      
      self.player1 = Character((100, 100),1)
      self.player2 = Character((500, 100),2)
      
      self.player1.target.append(self.player2)
      self.player2.target.append(self.player1)

   def update(self):
      self.player1.update()
      self.player2.update()

   def draw(self):
      self.displaySurface.blit(self.background, (0, 0))
      self.player1.draw(self.displaySurface)
      self.player2.draw(self.displaySurface)

   def run(self):
      run = True
      while run:
         self.update()
         self.draw()
        

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
               sys.exit()
         pygame.display.update()
