# feature of game - adding random arithmatic block obstacle on game road.
# if you resolve right - block will escape and you can move next. 
# But if not - your ball will be shift by this block. 
# And when coordinate on the road of ball will be less then 0 - then game over.

from random import randint

class Arithmetic_Obstacle_Block:
	def __init__(self, road_XY_coordinates = []):
		self.roadline_XY_coordinates = road_XY_coordinates
		self.left_math_operand = randint(10, 60)
		self.math_operator = '+'
		self.right_math_operand = randint(10, 60)
		self.width_of_block = self.left_math_operand * 2 
		self.height_of_block = self.right_math_operand * 2
		self.block_color_in_RGB = (10, 20, 90)
		self.block_text_color_in_RGB = (200, 200, 200)
		