import pygame
from pygame.math import Vector2
import sys


main_app_background_image = "storage/image/background/main_app_background.png"

game_1_background_image = "storage/image/background/game_1_background.png"


character_image = "storage/image/character/character"


bullet_image = "storage/image/character/bullet"

button_start_image = "storage/image/button/button_start.png"





frame_rate = 0.008


attack_range_width = 10
attack_range_height = 10
attack_time = frame_rate * 5

attack_time_cooldown  = 500
attack_damage = 15


bullet_speed = 0.8
bullet_time_cooldown = 500
bullet_damage = 8

gravity = 0.6
jump_time = 200 

hp_character = 100
hp_width = 100
mana_character = 100
mana_width = 100

character_width = 100
character_height = 100
move_speed = 0.4
flash_speed = 1
idle_time =5000




player_key = {
   1 : {
      "up": pygame.K_w,
      "down": pygame.K_s,
      "left": pygame.K_a,
      "right": pygame.K_d,
      "attack": pygame.K_j,
      "shoot": pygame.K_k,
      "flash": pygame.K_l,
   },
   2: {
      "up": pygame.K_UP,
      "down": pygame.K_DOWN,
      "left": pygame.K_LEFT,
      "right": pygame.K_RIGHT,
      "attack": pygame.K_KP1,
      "shoot": pygame.K_KP2,
      "flash": pygame.K_KP3,
   }
}


window_width , window_height = 1200, 600
cooldown_width = 100
fps = 250