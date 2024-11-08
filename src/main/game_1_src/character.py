from setting import *


class Character:
   def __init__(self):
      
      self.health = 100
      self.damage = 10
      self.speed = 0.1
      


   def input(self):
           pass
   
   def move(self):
      pass
     


   def attack(self):
      pass


   def update(self):
      self.input()
      self.move()
      self.attack()
      
