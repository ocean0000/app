from setting import * 
from .bot import Bot 

class Game_1:
   def __init__(self,displaySurface):
      self.background = pygame.image.load("storage/image/background/back_ground_game2.jpg")
      self.background = pygame.transform.scale(self.background, (window_width, window_height))
      self.displaySurface  = displaySurface
      self.bot1= Bot((100,100))

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

         for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_RIGHT:
                  self.bot1.rect.x += 10
               if event.key == pygame.K_LEFT:
                  self.bot1.rect.x -= 10
               if event.key == pygame.K_UP:
                  self.bot1.rect.y -= 10
               if event.key == pygame.K_DOWN:
                  self.bot1.rect.y += 10
               if event.key == pygame.K_SPACE:
                  self.bot1.jump()




            if event.type == pygame.QUIT:
               run = False
               sys.exit()
            pygame.display.update()
