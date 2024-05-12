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
		self.randomly_choosed_XY_pair_for_block = self.get_random_X_coordinate_and_just_Y_in_two_choosed_XY_pairs()
		print('\nBlock coordinates:', self.randomly_choosed_XY_pair_for_block)
		self.left_math_operand = randint(10, 60)
		self.math_operator = '+'
		self.right_math_operand = randint(10, 60)
		self.width_of_block = self.get_right_block_width()
		self.height_of_block = self.get_right_block_height()
		self.block_color_in_RGB = (230, 230, 160)
		self.block_text_color_in_RGB = (30, 70, 40)
		self.block_parameters_for_drawing = [self.randomly_choosed_XY_pair_for_block[0], 
			self.randomly_choosed_XY_pair_for_block[1] - self.height_of_block, self.width_of_block, 
			self.height_of_block]
		self.font_of_text_in_block = pg.font.Font('freesansbold.ttf', 15)

	def define_road_XY_coordinates_for_block_on_road(self):
		for road_XY_pair in self.roadline_XY_pairs_of_coordinates:
			if road_XY_pair[0] >= self.main_game_window_width_height[0]:
				self.road_XY_pairs_of_coordinates_for_block.append(road_XY_pair)

	def get_random_two_XY_pairs_of_line_as_part_of_road(self):
		self.define_road_XY_coordinates_for_block_on_road()
		print('XY pairs for block: ', self.road_XY_pairs_of_coordinates_for_block)
		print('Length of XY pairs:', len(self.road_XY_pairs_of_coordinates_for_block))
		first_random_XY_pair_index_in_coordinates = randint(0, len(self.road_XY_pairs_of_coordinates_for_block) - 2)
		secound_XY_pair_index_in_coordinates = first_random_XY_pair_index_in_coordinates + 1
		return [self.road_XY_pairs_of_coordinates_for_block[first_random_XY_pair_index_in_coordinates],
				self.road_XY_pairs_of_coordinates_for_block[secound_XY_pair_index_in_coordinates]]

	def get_random_X_coordinate_and_just_Y_in_two_choosed_XY_pairs(self):
		two_random_XY_pairs = self.get_random_two_XY_pairs_of_line_as_part_of_road()
		start_X_coordinate_value_for_choosing = two_random_XY_pairs[0][0]
		end_X_coordinate_value_for_choosing = two_random_XY_pairs[1][0]
		randomly_choosed_X_coordinate_for_block = randint(start_X_coordinate_value_for_choosing, end_X_coordinate_value_for_choosing)
		Y_coordinate_for_block = two_random_XY_pairs[0][1]

		return [randomly_choosed_X_coordinate_for_block, Y_coordinate_for_block]

	def draw_block_on_game_road(self):
		self.show_arithmatic_example_on_block()

	def set_new_X_coordinate_when_block_moving(self):
		self.block_parameters_for_drawing[0] -= 1

	def get_block_parameters(self):
		return self.block_parameters_for_drawing

	def get_math_example_in_string_form(self):
		return f"{str(self.left_math_operand)} + {str(self.right_math_operand)}"

	def show_arithmatic_example_on_block(self):
		block_math_example_string = self.get_math_example_in_string_form()
		block_math_example_XY_center = (self.block_parameters_for_drawing[0] + 40, 
										self.block_parameters_for_drawing[1] + 20)
		
		block_Rect = pg.draw.rect(self.pygame_window_obj, self.block_color_in_RGB, self.block_parameters_for_drawing)
		block_math_example = self.font_of_text_in_block.render(block_math_example_string, True, 
															self.block_text_color_in_RGB, self.block_color_in_RGB)
		block_math_example_Rect = block_math_example.get_rect()
		block_math_example_Rect.center = block_math_example_XY_center
		self.pygame_window_obj.blit(block_math_example, block_math_example_Rect)

	def get_right_block_width(self):
		if self.arithmetic_block_has_small_left_math_operand_as_width_for_block():
			return self.left_math_operand * 2 + 50
		else:
			return self.left_math_operand * 2

	def get_right_block_height(self):
		if self.arithmetic_block_has_small_right_math_operand_as_height_for_block():
			return self.right_math_operand * 3
		else:
			return self.right_math_operand * 2

	def arithmetic_block_has_small_left_math_operand_as_width_for_block(self):
		if self.left_math_operand * 2 < 60:
			return True
		else:
			return False

	def arithmetic_block_has_small_right_math_operand_as_height_for_block(self):
		if self.right_math_operand * 2 < 30:
			return True
		else:
			return False
