from setting import *
from common import common

class Window (common):
   def __init__(self):
         pygame.init()
         super().__init__()
         self.window = pygame.display.set_mode((window_width, window_height))
         pygame.display.set_caption("who is the winner?")
         self.background = pygame.image.load("storage/image/background/background_main_app.jpg")
         self.background = pygame.transform.scale(self.background, (window_width, window_height))
         


   def run(self):
      run = True
      while run:

         self.window.blit(self.background, (0, 0))
         self.draw_button("storage/image/button/button_start.png", window_width/2-100, window_height/2, 50, 50)
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
            
               sys.exit()
         pygame.display.update()



window = Window()
window.run()
