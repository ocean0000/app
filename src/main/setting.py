import pygame
from pygame.math import Vector2
import sys

main_app_background_image = "storage/image/background/main_app_background.png"

game_1_background_image = "storage/image/background/game_1_background.png"


character_image = "storage/image/character/character"

button_start_image = "storage/image/button/button_start.png"

frame_rate = 0.008


attack_range_width = 100
attack_range_height = 100
attack_time = frame_rate * 10
attack_time_cooldown  = 1500

move_speed = 0.8
hp_character = 20


player_key = {
   1 : {
      "up": pygame.K_w,
      "down": pygame.K_s,
      "left": pygame.K_a,
      "right": pygame.K_d,
      "attack": pygame.K_j
   },
   2: {
      "up": pygame.K_UP,
      "down": pygame.K_DOWN,
      "left": pygame.K_LEFT,
      "right": pygame.K_RIGHT,
      "attack": pygame.K_KP1
   }
}


window_width , window_height = 1200, 600
fps = 250