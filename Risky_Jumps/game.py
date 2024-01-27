# game about jumping ball, which
# just jump in order to avoid holes in road line.
# The holes in roadline appear randomly during your game period, until you lose.
# This is will be first version of game.

import pygame
from random import randint

class Jump_Game:
	def __init__(self, width_height_display = (500, 100), ball = 'ball_obj'):
		self.display_size = width_height_display
		self.score = 0
		self.ball = ball

	def start_game(self):
		