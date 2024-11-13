import pygame
from pygame.math import Vector2
import sys

main_app_background_image = "storage/image/background/main_app_background.png"

game_1_background_image = "storage/image/background/game_1_background.png"


character_image = "storage/image/character/character"
attack_range = 120

button_start_image = "storage/image/button/button_start.png"

frame_rate = 0.008

attack_time_cooldown  = 2000

attack_time = frame_rate * 10

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