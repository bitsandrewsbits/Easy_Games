# game about jumping ball, which
# just jump in order to avoid holes in road line.
# The holes in roadline appear randomly during your game period, until you lose.
# This is will be first version of game.

import pygame
from random import randint

class Jump_Game:
	def __init__(self, width_height_display = (800, 300), ball = 'ball_obj'):
		self.display_size = width_height_display
		self.display_rgb_color = (0, 0, 0)
		self.score = 0
		self.ball = ball
		self.holes_amount = 1
		self.game_over = False
		self.exit_from_game = False
		self.game_clock = pygame.time.Clock()
		self.game_main_window = pygame.display.set_mode((self.display_size[0], self.display_size[1]))

	def init_game_parameters(self):
		pygame.init()

	def start_game(self):
		self.init_game_parameters()

		while self.game_over == False and self.exit_from_game == False:
			self.game_clock.tick(10) # 2 iterations per second
			self.game_interface()
			
			for game_event in pygame.event.get():
				if game_event.type == pygame.QUIT:
					self.exit_from_game = True

			pygame.display.flip()



	def game_interface(self):
		self.game_main_window.fill(self.display_rgb_color)
		self.game_roadline()


	def game_roadline(self):
		road_rgb_color = (60, 250, 60)
		roadline_coordinates = self.get_lines_coordinates()
		pygame.draw.lines(self.game_main_window, road_rgb_color, False, roadline_coordinates, 5)

	def get_lines_coordinates(self):
		result_lines_coordinates = []
		hole_size = 50
		start_road_coordinates = [0, 200]
		end_road_coordinates = [self.display_size[0], 200]
		hole_end_coordinates = 50
		lines_start_end_coordinates = []
		
		result_lines_coordinates.append(start_road_coordinates)
		for i in range(self.holes_amount):
			hole_random_start_coordinates = randint(hole_end_coordinates + hole_size, self.display_size[0] // 2)
			result_lines_coordinates.append([hole_random_start_coordinates, 200])
			hole_end_coordinates = hole_random_start_coordinates + hole_size
			result_lines_coordinates.append([hole_end_coordinates, 200])	
		result_lines_coordinates.append(end_road_coordinates)

		# print(result_lines_coordinates)
		return result_lines_coordinates

	def move_game_road(self):
		pass

	def game_score_rect(self):
		score_rect_width = 100
		score_rect_height = 60
		score_rect_color = 'grey'


#testing
game = Jump_Game()
game.start_game()