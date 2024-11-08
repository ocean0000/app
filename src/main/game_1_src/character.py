from setting import *


class Character:
   def __init__(self):
      self.health = 100
      self.damage = 10
      self.speed = 5
      self.image = pygame.Surface((50, 50))


   def draw(self):
      pygame.draw.rect(self.image, (255, 0, 0), (self.image.x, self.image.y, 50, 50))
     
      
   
   def move(self):
      key = pygame.key.get_pressed()
      if key[pygame.K_LEFT]:
         self.image.x -= self.speed
      if key[pygame.K_RIGHT]:
         self.image.x += self.speed
     


   def attack(self):
      pass
   
   def update(self):
      self.move()
      self.draw()
