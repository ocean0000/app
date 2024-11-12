from setting import * 
from .bot import Bot 

class Game_1:
   def __init__(self,displaySurface):
      self.background = pygame.image.load(game_1_background_image)
      self.background = pygame.transform.scale(self.background, (window_width, window_height))
      self.displaySurface  = displaySurface
      self.bot1= Bot((500,500))
      self.clock = pygame.time.Clock()

   def update(self):
      self.bot1.update()
   

   def draw(self):
      self.displaySurface.blit(self.background, (0, 0))
      self.bot1.draw(self.displaySurface)


   def run(self):
      run = True
      while run:
         self.update()
         self.draw()
         self.clock.tick(fps)

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
               sys.exit()
         pygame.display.update()
