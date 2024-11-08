from setting import *

class Window:
   def __init__(self):
         pygame.init()
         self.window = pygame.display.set_mode((window_width, window_height))
         pygame.display.set_caption("who is the winner?")
   
   def run(self):
      run = True
      while run:



         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
            
               sys.exit()
         pygame.display.update()



window =Window()
window.run()
