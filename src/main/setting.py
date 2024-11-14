import pygame
from pygame.math import Vector2
import sys
import copy

main_app_background_image = "storage/image/background/main_app_background.png"

game_1_background_image = "storage/image/background/game_1_background.png"


character_image = "storage/image/character/character"


bullet_image = "storage/image/character/bullet"

button_start_image = "storage/image/button/button_start.png"





frame_rate = 0.008


attack_range_width = 100
attack_range_height = 100
attack_time = frame_rate * 10

attack_time_cooldown  = 1500


bullet_speed = 0.5
move_speed = 0.2


hp_character = 50


player_key = {
   1 : {
      "up": pygame.K_w,
      "down": pygame.K_s,
      "left": pygame.K_a,
      "right": pygame.K_d,
      "attack": pygame.K_j,
      "shoot": pygame.K_k,
   },
   2: {
      "up": pygame.K_UP,
      "down": pygame.K_DOWN,
      "left": pygame.K_LEFT,
      "right": pygame.K_RIGHT,
      "attack": pygame.K_KP1,
      "shoot": pygame.K_KP2,
   }
}


window_width , window_height = 1200, 600
fps = 250