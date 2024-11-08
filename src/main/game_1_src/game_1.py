from setting import * 
from .character import Character

class Game_1():
   def __init__(self):
      self.window = pygame.display.set_mode((1200, 560))  # Set the window size
      
      self.tmx_map = load_pygame("storage/image/background/back_ground.tmx")
      
      
      
   def setup_map(self):
         for layer in self.tmx_map.visible_layers:
            
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.tmx_map.get_tile_image_by_gid(gid)
                    if tile:
                        self.window.blit(tile, (x * self.tmx_map.tilewidth , y * self.tmx_map.tileheight ))
         

   
   def run(self):
      run = True
      while run:
         self.setup_map()
        

        
         
         

         for event in pygame.event.get():
            

            if event.type == pygame.QUIT:
               run = False
               sys.exit()
         pygame.display.update()   




      