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
		self.road_distance = 0
		self.ball = ball
		self.holes_amount = 1
		self.hole_size = 50
		self.road_holes_coordinates = []
		self.max_amount_of_hole_with_display_parameters = self.display_size[0] // (self.hole_size * 2)
		self.road_move_speed = 1
		self.roadlines_coordinates = []
		self.game_over = False
		self.exit_from_game = False
		self.game_clock = pygame.time.Clock()
		self.game_main_window = pygame.display.set_mode((self.display_size[0], self.display_size[1]))

	def init_game_parameters(self):
		pygame.init()

	def start_game(self):
		self.init_game_parameters()

		while self.game_over == False and self.exit_from_game == False:
			self.game_clock.tick(30) # 30 iterations per second
			self.game_interface()
			
			for game_event in pygame.event.get():
				if game_event.type == pygame.QUIT:
					self.exit_from_game = True

			pygame.display.flip()



	def game_interface(self):
		self.game_main_window.fill(self.display_rgb_color)
		self.game_roadline()


	def game_roadline(self):
		self.show_and_move_game_road()

	def create_lines_coordinates(self, start_road_coordinates = 1, end_road_coordinates = 1):
		result_lines_coordinates = []
		start_roadline_coordinates = [start_road_coordinates, 200]
		end_roadline_coordinates = [end_road_coordinates, 200]
		hole_end_coordinates = 50
		
		result_lines_coordinates.append(start_roadline_coordinates)
		if self.max_amount_of_hole_with_display_parameters < self.holes_amount:
			print('Warning. Achived MAX possible amount of holes in road for this display parameters.')
			print(f'Changing to MAX possible amount of holes: {max_amount_of_hole_with_display_parameters}')
			self.holes_amount = max_amount_of_hole_with_display_parameters

		self.road_holes_coordinates = [randint(start_road_coordinates, end_road_coordinates)]
		
		if self.holes_amount == 1:
			hole_random_start_coordinates = self.road_holes_coordinates[0]
			result_lines_coordinates.append([hole_random_start_coordinates, 200])
			hole_end_coordinates = hole_random_start_coordinates + self.hole_size
			result_lines_coordinates.append([hole_end_coordinates, 200])
			result_lines_coordinates.append(end_roadline_coordinates)
		elif self.holes_amount > 1:
			for i in range(self.holes_amount - 1):
				find_right_hole_coordinate = False
				while not find_right_hole_coordinate:
					hole_random_start_coordinates = randint(start_road_coordinates, end_road_coordinates)
					for hole_start_coordinate in self.road_holes_coordinates:
						if hole_random_start_coordinates > hole_start_coordinate + 2 * self.hole_size or \
						    hole_random_start_coordinates < hole_start_coordinate - 2 * self.hole_size:
							self.road_holes_coordinates.append(hole_random_start_coordinates)
							find_right_hole_coordinate = True
							break

				result_lines_coordinates.append([hole_random_start_coordinates, 200])
				hole_end_coordinates = hole_random_start_coordinates + self.hole_size
				result_lines_coordinates.append([hole_end_coordinates, 200])
			result_lines_coordinates.append(end_roadline_coordinates)

		print('Hole coordinates:', self.road_holes_coordinates)
		return result_lines_coordinates

	def show_and_move_game_road(self):
		self.manage_road_coordinates()
		
		road_rgb_color = (60, 250, 60)
		for coordinates in self.roadlines_coordinates:
			coordinates[0] = coordinates[0] - self.road_move_speed
		
		for i in range(0, len(self.roadlines_coordinates), 2):
			pygame.draw.line(self.game_main_window, road_rgb_color, 
				self.roadlines_coordinates[i], self.roadlines_coordinates[i + 1], 5)
		self.road_distance += 1
		
		if self.road_distance % self.display_size[0] == 0 and self.road_distance != 0:
			print('Distance:', self.road_distance)
			print('Removing coordinates...')
			self.remove_road_coordinates_beyond_screen()
			print('Coordinates after removing.')
			print(self.roadlines_coordinates)
			print('Adding new hole...')
			self.holes_amount += 1
			print('Amount of holes =', self.holes_amount)

	def manage_road_coordinates(self):
		if self.road_distance == 0:
			print('Start adding coordinates...(distance = 0)')
			self.set_up_start_roadline_coordinates()
			print(self.roadlines_coordinates)
		elif self.road_distance % self.display_size[0] == 0:
			print(f'Another adding coordinates...(distance = {self.road_distance})')
			tmp_road_coordinates = self.create_lines_coordinates(self.display_size[0], 2 * self.display_size[0])
			self.roadlines_coordinates += tmp_road_coordinates
			print(self.roadlines_coordinates)

	def set_up_start_roadline_coordinates(self):
		self.roadlines_coordinates = self.create_lines_coordinates(self.hole_size, self.display_size[0] - self.hole_size)
		self.roadlines_coordinates += self.create_lines_coordinates(self.display_size[0], 
																	2 * self.display_size[0] - self.hole_size)

	def remove_road_coordinates_beyond_screen(self):
		amount_of_removed_elem = 0
		print('Coordinates before removing...')
		print(self.roadlines_coordinates)
		current_roadlines_coordinates_length = len(self.roadlines_coordinates)
		if (current_roadlines_coordinates_length // 2) % 2 != 0:
			self.roadlines_coordinates = self.roadlines_coordinates[current_roadlines_coordinates_length // 2 - 1:]
		else:
			self.roadlines_coordinates = self.roadlines_coordinates[current_roadlines_coordinates_length // 2:]
		print('Coordinates after removing...')
		print(self.roadlines_coordinates)

	def game_score_rect(self):
		score_rect_width = 100
		score_rect_height = 60
		score_rect_color = 'grey'


#testing
game = Jump_Game()
game.start_game()