# game about jumping ball, which
# just jump in order to avoid holes in road line.
# The holes in roadline appear randomly during your game period, until you lose.
# This is will be first version of game.

import pygame
from random import randint

class Jump_Game:
	def __init__(self, width_height_display = (800, 300), ball = 'ball_obj'):
		self.display_size = width_height_display
		self.display_rgb_color = (50, 50, 50)
		self.score = 0
		self.ball = ball
		self.game_over = False
		self.exit_from_game = False 

	def init_game_parameters(self):
		pygame.init()
		self.create_game_screen()

	def start_game(self):
		self.init_game_parameters()

		while self.game_over == False and self.exit_from_game == False:
			for game_event in pygame.event.get():
				if game_event.type == pygame.QUIT:
					self.exit_from_game = True

			pygame.display.flip()


	def create_game_screen(self):
		pygame.display.set_mode((self.display_size[0], self.display_size[1]))

	def create_game_score_rect(self):
		score_rect_width = 100
		score_rect_height = 60
		score_rect_color = 'grey'


#testing
game = Jump_Game()
game.start_game()