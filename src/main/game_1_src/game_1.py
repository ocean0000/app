from setting import * 
from .bot import Bot 

class Game_1:
   def __init__(self,displaySurface):
      self.background = pygame.image.load(game_1_background_image)
      self.background = pygame.transform.scale(self.background, (window_width, window_height))
      self.displaySurface  = displaySurface
      self.bot1= Bot((500,500),1)
      self.bot2 = Bot((100,100),2)
      self.bot1.target_bot = self.bot2
      self.bot2.target_bot = self.bot1
      self.clock = pygame.time.Clock()

   def update(self):
      self.bot1.update()
      self.bot2.update()
   

   def draw(self):
      self.displaySurface.blit(self.background, (0, 0))
      self.bot1.draw(self.displaySurface)
      self.bot2.draw(self.displaySurface)


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
