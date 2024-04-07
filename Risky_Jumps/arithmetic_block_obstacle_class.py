# feature of game - adding random arithmetic block obstacle on game road.
# if you resolve right - block will escape and you can move next. 
# But if not - your ball will be shift by this block. 
# And when coordinate on the road of ball will be less then 0 - then game over.

import pygame as pg
from random import randint

class Arithmetic_Obstacle_Block:
	def __init__(self, pygame_window_object = 'pygame_obj', main_game_window_size = (300, 200), 
				road_XY_coordinates = []):
		self.pygame_window_obj = pygame_window_object
		self.main_game_window_width_height = main_game_window_size
		self.roadline_XY_pairs_of_coordinates = road_XY_coordinates
		self.road_XY_pairs_of_coordinates_for_block = []
		self.randomly_choosed_XY_pair_for_block = self.get_randomly_choosed_XY_pair_of_roadline_for_block()
		print('\nBlock coordinates:', self.randomly_choosed_XY_pair_for_block)
		self.left_math_operand = randint(10, 60)
		self.math_operator = '+'
		self.right_math_operand = randint(10, 30)
		self.width_of_block = self.left_math_operand * 3
		self.height_of_block = self.right_math_operand
		self.block_color_in_RGB = (140, 190, 200)
		self.block_text_color_in_RGB = (200, 200, 200)
		self.block_parameters_for_drawing = [self.randomly_choosed_XY_pair_for_block[0], 
			self.randomly_choosed_XY_pair_for_block[1] - self.height_of_block, self.width_of_block, 
			self.height_of_block]

	def define_road_XY_coordinates_for_block_on_road(self):
		for road_XY_pair in self.roadline_XY_pairs_of_coordinates:
			if road_XY_pair[0] > self.main_game_window_width_height[0] + 130:
				self.road_XY_pairs_of_coordinates_for_block.append(road_XY_pair)

	def get_randomly_choosed_XY_pair_of_roadline_for_block(self):
		self.define_road_XY_coordinates_for_block_on_road()
		return self.road_XY_pairs_of_coordinates_for_block[randint(0, len(self.road_XY_pairs_of_coordinates_for_block) - 1)]

	def draw_block_on_game_road(self):
		pg.draw.rect(self.pygame_window_obj, self.block_color_in_RGB, self.block_parameters_for_drawing)

	def set_new_X_coordinate_when_block_moving(self):
		self.block_parameters_for_drawing[0] -= 1

	def get_block_parameters(self):
		return self.block_parameters_for_drawing
