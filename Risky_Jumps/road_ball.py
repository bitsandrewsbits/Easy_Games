# file with class Ball for game

import pygame as pg
import defining_optimal_speed_jump as opt_jump
import arithmetic_block_obstacle_class as arith_block

class Game_Ball:
	def __init__(self, screen_surface, start_road_height = 0, radius = 10, ball_color = 'yellow'):
		self.ball_radius = radius
		self.ball_color = ball_color
		self.screen_surface = screen_surface
		self.ball_start_center_coordinates = [20, 188]
		self.ball_center_coordinates = [20, 188]
		self.ball_jump_high = 60                 #jump max high (in pixels)
		self.ball_jump_speed_on_top = 0
		self.ball_jump_speed_on_bottom = 0
		self.ball_jump_total_distance = 120        # in pixels
		self.ball_move_distance = 0
		self.ball_jump_to_up = True
		self.ball_jump_to_down = False
		self.ball_status = 'move_on_road'
		self.start_height_of_road = start_road_height
		self.height_of_road = start_road_height
		self.need_to_change_ball_Y_coordinate = True
		self.start_ball_jump_FPS = 40
		self.new_ball_jump_FPS = 40

		self.time_for_1_frame_in_game = 1 / self.new_ball_jump_FPS
		self.start_ball_jump_speed = 5
		self.ball_jump_speed = 5   # pixels/frame (-0.5 from return func)
		
		self.acceleration_of_ball_speed_to_up = -0.2    #pixels/frame^2
		self.acceleration_of_ball_speed_to_down = 0.075   # only a = g in pixels/frame^2, g = 10 pixels/c^2

		self.arithmetic_block = ''

	def draw_ball(self):
		pg.draw.circle(self.screen_surface, self.ball_color, self.ball_center_coordinates, self.ball_radius)

	def ball_jump(self):
		if self.game_FPS_changed():
			self.set_new_ball_accelerations_when_jumping_for_same_moving()

		if self.is_changed_road_height() and self.need_to_change_ball_Y_coordinate:
			# print('Road height was changed... Road height =', self.height_of_road)
			self.set_new_ball_jump_total_distance_when_road_height_changed()
			# print('Changed Jump total distance =', self.ball_jump_total_distance)
			self.need_to_change_ball_Y_coordinate = False

		if self.ball_jump_to_up:
			self.ball_center_coordinates[1] -= self.ball_jump_speed
			self.ball_move_distance += self.ball_jump_speed
			self.ball_jump_speed += self.acceleration_of_ball_speed_to_up
			
		if round(self.ball_jump_speed) == 0.0 or self.ball_move_distance >= self.ball_jump_high:
			# print('Max height in jump =', self.ball_center_coordinates)
			# print('Ball move distance =', self.ball_move_distance)
			self.ball_jump_to_up = False
			self.ball_jump_to_down = True

		if self.ball_jump_to_down:
			self.ball_center_coordinates[1] += self.ball_jump_speed
			self.ball_move_distance += self.ball_jump_speed
			self.ball_jump_speed += self.acceleration_of_ball_speed_to_down

		# print('Ball jump speed =', self.ball_jump_speed)
		# print('Ball move distance =', self.ball_move_distance)

		self.draw_ball()

	def ball_move_right(self):
		self.ball_center_coordinates[0] += 1

	def ball_move_left(self):
		self.ball_center_coordinates[0] -= 1

	def get_ball_jump_status(self):
		if self.arithmetic_block != '' and not self.arithmetic_block_behind_ball(self.arithmetic_block):
			self.check_ball_collision_with_arithmetic_block_and_set_new_ball_XY(self.arithmetic_block)
			arithm_block_parameters = self.arithmetic_block.get_block_parameters()
			# if self.ball_jump_to_down:
				# print('~' * 30)
				# print('Ball jump down!')
				# print('Block exist. Parameters:')
				# print('Block XY coordinates(start):', arithm_block_parameters[:2])
				# print('Block XY coordinates(end):', [arithm_block_parameters[0] + arithm_block_parameters[2], arithm_block_parameters[1]])
				# print('Ball XY coordinates(current):', self.ball_center_coordinates)
				# print('Ball XY coordinates(start when jump):', self.ball_start_center_coordinates)
				# print('Condition for new ball XY coordinates:')
				# print(f"if {self.ball_over_arithmetic_block_surface(self.arithmetic_block)} and {self.ball_jump_to_down} and ({arithm_block_parameters[1]} <= {self.ball_center_coordinates[1] + self.ball_radius})")
				# print('#' * 30)

			if self.ball_over_arithmetic_block_surface(self.arithmetic_block) and self.ball_jump_to_down and \
			(arithm_block_parameters[1] <= self.ball_center_coordinates[1] + self.ball_radius):
				print('Ball on the block surface!')
				print('Ball start XY coordinates(before jump on block):', self.ball_start_center_coordinates)
				print('Block XY coordinates:', arithm_block_parameters[:2])
				self.set_new_start_ball_XY_coordinates_when_collision_with_arithmetic_block(self.arithmetic_block, self.ball_center_coordinates[0])
				self.set_new_current_ball_Y_coordinate_when_collision_with_arithmetic_block()
				print('Ball start XY coordinates(after jump on block):', self.ball_start_center_coordinates)
				self.set_initial_ball_parameters_for_jump()
				self.ball_status = 'ball_on_block'
				return 'Ball_jumped_on_block'
			elif self.ball_over_arithmetic_block_surface(self.arithmetic_block) and self.ball_jump_to_down:
				self.ball_status = 'ball_in_jump_over_block'
				return 'Ball_in_jump_over_block'
		else:
			self.set_new_ball_jump_total_distance_when_block_behind_ball(self.arithmetic_block)
			print('Block behind Ball!')
			print('Ball XY coordinates(current):', self.ball_center_coordinates)
			print('Ball XY coordinates(start after jump):', self.ball_start_center_coordinates)
			print('Road height =', self.height_of_road)
			print('Ball status =', self.ball_status)

		if self.ball_move_distance + self.ball_jump_speed >= self.ball_jump_total_distance or \
		self.height_of_road <= self.ball_center_coordinates[1] + self.ball_radius:
			print('Ball center coordinates after jump:', self.ball_center_coordinates)
			self.set_new_current_ball_Y_center_coordinate_when_road_height_changed()
			self.set_new_start_ball_Y_center_coordinate_when_road_height_changed()
			self.set_initial_ball_parameters_for_jump()
			print('Ball start Y coordinate for jump =', self.ball_start_center_coordinates[1])
			print('Road height =', self.height_of_road)
			print('===Ball Jumped!===')
			return 'Ball_jumped'
		else:
			self.ball_status = 'ball_in_jump'
			return 'Ball_in_jump'

	def set_initial_ball_parameters_for_jump(self):
		self.ball_jump_to_down = False
		self.ball_jump_to_up = True
		self.ball_move_distance = 0
		self.ball_jump_speed = self.start_ball_jump_speed
		self.ball_status = 'ball_jumped'
		self.need_to_change_ball_Y_coordinate = True
		self.start_height_of_road = self.height_of_road
		self.ball_jump_total_distance = 120

	def get_arithmetic_block_object(self, arithmetic_blocks):
		if arithmetic_blocks != []:
			self.arithmetic_block = arithmetic_blocks[0]
		else:
			return 'blocks dont exist yet'

	def get_ball_status(self):
		return self.ball_status

	def get_ball_center_coordinates(self):
		return self.ball_center_coordinates

	def set_new_game_FPS(self, game_fps = 40):
		self.new_ball_jump_FPS = game_fps

	def game_FPS_changed(self):
		if self.start_ball_jump_FPS != self.new_ball_jump_FPS:
			return True
		else:
			return False

	def set_new_ball_accelerations_when_jumping_for_same_moving(self):
		temp_up_jump_parameters = opt_jump.get_acceleration_v0_steps_for_S_and_FPS_up_jump(self.new_ball_jump_FPS)
		self.start_ball_jump_speed = temp_up_jump_parameters[0] - 0.5
		print('New ball jump speed(up) =', self.start_ball_jump_speed)
		self.acceleration_of_ball_speed_to_up = temp_up_jump_parameters[1]
		temp_down_jump_parameters = opt_jump.get_acceleration_steps_for_S_and_FPS_down_jump(self.new_ball_jump_FPS)
		self.acceleration_of_ball_speed_to_down = temp_down_jump_parameters[0]
		print('New ball acceleration_of_ball_speed_to_up =', self.acceleration_of_ball_speed_to_up)
		print('New ball acceleration_of_ball_speed_to_down =', self.acceleration_of_ball_speed_to_down)
		self.start_ball_jump_FPS = self.new_ball_jump_FPS

	def set_road_height(self, road_Y_coordinate):
		self.height_of_road = road_Y_coordinate

	def set_new_start_ball_Y_center_coordinate_when_road_height_changed(self):
		new_start_ball_Y_coordinate = self.ball_start_center_coordinates[1] + (self.height_of_road - self.start_height_of_road)
		self.ball_start_center_coordinates[1] = new_start_ball_Y_coordinate

	def set_new_current_ball_Y_center_coordinate_when_road_height_changed(self):
		self.ball_center_coordinates[1] = self.ball_start_center_coordinates[1]

	def ball_changing_coordinates_when_falling_from_road(self):
		if self.ball_center_coordinates[1] - 100 > self.ball_start_center_coordinates[1]:
			self.ball_status = 'game_over'
		else:
			self.ball_center_coordinates[1] += self.ball_jump_speed
			self.ball_move_distance += self.ball_jump_speed
			self.ball_jump_speed += self.acceleration_of_ball_speed_to_down

	def is_changed_road_height(self):
		if self.start_height_of_road != self.height_of_road:
			return True
		else:
			return False

	def set_new_ball_jump_total_distance_when_road_height_changed(self):
		self.ball_jump_total_distance += (self.height_of_road - self.start_height_of_road)

	def set_new_ball_jump_total_distance_when_block_behind_ball(self, arithmetic_block_obj):
		block_parameters = arithmetic_block_obj.get_block_parameters()
		block_Y_coordinate = block_parameters[1]
		self.ball_jump_total_distance += (self.height_of_road - block_Y_coordinate)

	def arithmetic_block_behind_ball(self, arithmetic_block_obj):
		block_parameters = arithmetic_block_obj.get_block_parameters()
		if self.ball_center_coordinates[0] + self.ball_radius > block_parameters[0] + block_parameters[2]:
			return True
		else:
			return False

	def check_ball_collision_with_arithmetic_block_and_set_new_ball_XY(self, arithmetic_block_obj):
		arithmetic_block_parameters = arithmetic_block_obj.get_block_parameters()
		aritmetic_block_width = arithmetic_block_parameters[2]
		
		if self.ball_center_coordinates[0] + self.ball_radius > arithmetic_block_parameters[0] and \
		self.ball_center_coordinates[1] + self.ball_radius > arithmetic_block_parameters[1] and \
		not self.ball_over_arithmetic_block_surface(arithmetic_block_obj) and \
		not self.arithmetic_block_behind_ball(arithmetic_block_obj):
			# print('*' * 20)
			# print('Ball encounter with block wall. Changing ball X coordinate...')
			# print('Setting up ball X coordinate =', arithmetic_block_parameters[0] - self.ball_radius)
			# print('*' * 20)
			self.collision_with_block_set_new_ball_coordinates(arithmetic_block_parameters[0] - self.ball_radius)
		else:
			self.collision_with_block_set_new_ball_coordinates()

	def collision_with_block_set_new_ball_coordinates(self, new_ball_X_coordinate = 'no_changes', 
															new_ball_Y_coordinate = 'no_changes'):
		if new_ball_X_coordinate != 'no_changes' or new_ball_Y_coordinate != 'no_changes':
			if new_ball_X_coordinate == 'no_changes':
				self.ball_center_coordinates[1] = new_ball_Y_coordinate
			elif new_ball_Y_coordinate == 'no_changes':
				self.ball_center_coordinates[0] = new_ball_X_coordinate
			else:
				self.ball_center_coordinates[0] = new_ball_X_coordinate
				self.ball_center_coordinates[1] = new_ball_Y_coordinate

	def set_new_current_ball_Y_coordinate_when_collision_with_arithmetic_block(self):
		self.ball_center_coordinates = self.ball_start_center_coordinates

	def set_new_start_ball_XY_coordinates_when_collision_with_arithmetic_block(self, arithmetic_block_obj, new_X_ball_coordinate = 0):
		arithmetic_block_parameters = arithmetic_block_obj.get_block_parameters()
		self.ball_start_center_coordinates[1] = arithmetic_block_parameters[1] - self.ball_radius
		self.ball_start_center_coordinates[0] = new_X_ball_coordinate

	def ball_over_arithmetic_block_surface(self, arithmetic_block_obj):
		if arithmetic_block_obj == False:
			return False

		arithmetic_block_parameters = arithmetic_block_obj.get_block_parameters()
		aritmetic_block_width = arithmetic_block_parameters[2]
		# if self.ball_jump_to_down:
		# 	print('Condition(is ball over block surface):')
		# 	print(f"if {self.ball_center_coordinates[0]} >= {arithmetic_block_parameters[0]} and {self.ball_center_coordinates[0]} <= {arithmetic_block_parameters[0]} + {aritmetic_block_width}")
		
		if self.ball_center_coordinates[0] >= arithmetic_block_parameters[0] and \
		(self.ball_center_coordinates[0] <= arithmetic_block_parameters[0] + aritmetic_block_width):
			return True
		else:
			return False


























