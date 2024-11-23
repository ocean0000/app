from setting import * 
from .character import Character 

class Game_1:
   def __init__(self,displaySurface):
      self.background = pygame.image.load(game_1_background_image)
      self.background = pygame.transform.scale(self.background, (window_width, window_height))
      self.displaySurface  = displaySurface
      self.font = pygame.font.Font(None, 36)
      self.game_mode =None

      
      
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
         if self.game_mode == None:
               self.displaySurface.fill((255, 255, 255))
               single_player_rect = pygame.Rect(100, 400, 200, 50)
               multiplayer_rect = pygame.Rect(500, 400, 200, 50)
               pygame.draw.rect(self.displaySurface, (0, 0, 0), single_player_rect)
               pygame.draw.rect(self.displaySurface, (0, 0, 0), multiplayer_rect)

               # Render text
               single_player_text = self.font.render("Single Player", True, (255, 255, 255))
               multiplayer_text = self.font.render("Multiplayer", True, (255, 255, 255))

               # Blit text
               self.displaySurface.blit(single_player_text, (single_player_rect.x + 20, single_player_rect.y + 10))
               self.displaySurface.blit(multiplayer_text, (multiplayer_rect.x + 20, multiplayer_rect.y + 10))


               for event in pygame.event.get():
                  if event.type == pygame.MOUSEBUTTONDOWN:
                     if single_player_rect.collidepoint(event.pos):
                        self.game_mode = "single"
                     elif multiplayer_rect.collidepoint(event.pos):
                        self.game_mode = "multi"
            
         else:
            self.update()
            self.draw()
            
         

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
               sys.exit()
         pygame.display.update()
