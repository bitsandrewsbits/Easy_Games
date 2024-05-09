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
		# self.ball_jump_total_distance = 120        # in pixels
		# self.ball_move_distance = 0
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
		self.ball_jump_speed = 5   # pixels/frame
		
		self.acceleration_of_ball_speed_to_up = -0.2    # pixels/frame^2
		self.acceleration_of_ball_speed_to_down = 0.0625   # a in pixels/frame^2

		self.all_arithmetic_blocks_on_road = []
		self.arithmetic_block = ''
		self.ball_jump_status_func_executions = [False, False, False]
		self.index_of_current_block_for_overjumping = 0

	def draw_ball(self):
		pg.draw.circle(self.screen_surface, self.ball_color, self.ball_center_coordinates, self.ball_radius)

	def ball_jump(self):
		if self.ball_jump_to_up:
			self.ball_center_coordinates[1] -= self.ball_jump_speed
			# self.ball_move_distance += self.ball_jump_speed
			self.ball_jump_speed += self.acceleration_of_ball_speed_to_up
			print('Ball speed[UP]:', self.ball_jump_speed)
			
		if round(self.ball_jump_speed) == 0.0:
			print('Ball changing move vector do DOWN!')
			self.ball_jump_to_up = False
			self.ball_jump_to_down = True

		if self.ball_jump_to_down:
			self.ball_center_coordinates[1] += self.ball_jump_speed
			# self.ball_move_distance += self.ball_jump_speed
			self.ball_jump_speed += self.acceleration_of_ball_speed_to_down
			print('Ball speed[DOWN]:', self.ball_jump_speed)

		self.draw_ball()

	def ball_move_right(self):
		self.ball_center_coordinates[0] += 1

	def ball_move_left(self):
		self.ball_center_coordinates[0] -= 1

	def set_ball_jump_status_in_different_cases(self):
		if self.arithmetic_block != '':

			self.set_ball_status_when_jump_from_road_to_road()
			
			self.set_ball_status_when_jump_from_road_to_block()
			
			self.set_ball_status_when_jump_from_block_to_road()				
	
	def set_ball_status_when_jump_from_road_to_block(self):
		if self.ball_over_arithmetic_block_surface(self.arithmetic_block) and self.ball_jump_to_down and \
		self.ball_on_the_block_surface(self.arithmetic_block):
			print('Ball on the block surface!')
			# print('Ball start XY coordinates(before jump on block):', self.ball_start_center_coordinates)
			# print('Block XY coordinates:', arithm_block_parameters[:2])
			self.set_new_start_ball_XY_coordinates_when_collision_with_block_surface(self.arithmetic_block, self.ball_center_coordinates[0])
			self.set_new_current_ball_Y_coordinate_when_collision_with_block_surface()
			# print('Ball start XY coordinates(after jump on block):', self.ball_start_center_coordinates)
			self.set_initial_ball_parameters_for_jump()
			self.ball_status = 'ball_jumped_to_block'
			print('Ball status:', self.ball_status)
		elif self.ball_over_arithmetic_block_surface(self.arithmetic_block) and self.ball_jump_to_down:
			# print('Ball in jump OVER Block!!!')
			self.ball_status = 'ball_in_jump_to[over]_block'
			# print('Ball status:', self.ball_status)
	
	def set_ball_status_when_jump_from_block_to_road(self):
		if self.arithmetic_block_behind_ball() and self.get_arithmetic_block_that_closest_to_ball():
			if self.ball_center_coordinates[1] + self.ball_radius >= self.height_of_road:
				self.set_initial_ball_parameters_for_jump()
				self.ball_status = 'ball_jumped_from_block_to_road'
				print('Ball jumped FROM BLOCK TO ROAD!')
				self.set_new_block_status_for_current_block_behind_ball()
				self.set_new_start_ball_Y_coordinate_when_ball_jumped_from_block_to_road()
				self.set_new_current_ball_Y_center_coordinate_when_ball_jumped_from_block_to_road()
				print('Ball start Y coordinate for jump =', self.ball_start_center_coordinates[1])
				print('Road height =', self.height_of_road)
				print('Ball status =', self.ball_status)
				if not self.block_for_ball_overjumping_index_number_more_then_block_max_index():
					self.index_of_current_block_for_overjumping += 1
				print('INDEX of current block =', self.index_of_current_block_for_overjumping)
			else:
				self.ball_status = 'ball_in_jump_from_block_to_road'
				# print('Ball acceleration to UP:', self.acceleration_of_ball_speed_to_up)
				# print('Ball speed to UP:', self.ball_jump_speed)
				# print('Ball status:', self.ball_status)
				# print('Ball Y coordinate =', self.ball_center_coordinates[1])
				# print('Road height =', self.height_of_road)

	def set_ball_status_when_jump_from_road_to_road(self):
		if self.ball_status not in ('ball_in_jump_to[over]_block', 'ball_in_jump_from_block_to_road'):
			if self.ball_center_coordinates[1] + self.ball_radius >= self.height_of_road:
				print('Ball center coordinates after jump:', self.ball_center_coordinates)
				self.set_new_start_ball_Y_center_coordinate_when_road_height_changed()
				self.set_new_current_ball_Y_center_coordinate_when_road_height_changed()
				if self.any_block_behind_ball():
					self.set_new_ball_Y_coordinate_as_correction()
				self.set_initial_ball_parameters_for_jump()
				print('Ball start Y coordinate for jump =', self.ball_start_center_coordinates[1])
				print('Road height =', self.height_of_road)
				print('Ball Jumped FROM ROAD to ROAD')
				print('Ball status =', self.ball_status)
				self.ball_status = 'ball_jumped_from_road_to_road'
			else:
				self.ball_status = 'ball_in_jump_from_road_to_road'

	def block_for_ball_overjumping_index_number_more_then_block_max_index(self):
		if self.index_of_current_block_for_overjumping + 1 > len(self.all_arithmetic_blocks_on_road) - 1:
			return True
		else:
			return False

	def ball_on_the_block_surface(self, arithm_block):
		arithm_block_parameters = arithm_block.get_block_parameters()
		if self.ball_center_coordinates[1] + self.ball_radius >= arithm_block_parameters[1]:
			return True
		else:
			return False

	def set_initial_ball_parameters_for_jump(self):
		self.ball_jump_to_down = False
		self.ball_jump_to_up = True
		self.ball_jump_speed = self.start_ball_jump_speed
		self.ball_status = 'move_on_road'
		self.need_to_change_ball_Y_coordinate = True
		self.start_height_of_road = self.height_of_road

	def get_all_arithmetic_blocks_and_status_for_ball(self, arithmetic_blocks):
		self.all_arithmetic_blocks_on_road = arithmetic_blocks

	def get_arithmetic_block_that_closest_to_ball(self):
		if self.all_arithmetic_blocks_on_road != []:
			for block in self.all_arithmetic_blocks_on_road:
				if block[1] == 'Ahead':
					self.arithmetic_block = block[0]
					break
		else:
			return False

	def any_block_behind_ball(self):
		for block in self.all_arithmetic_blocks_on_road:
			if block[1] == 'Behind':
				return True
		return False

	def set_new_block_status_for_current_block_behind_ball(self):
		if len(self.all_arithmetic_blocks_on_road) == 1:
			print('Ball OVERJUMPED Block. SET new block status - Behind')
			self.all_arithmetic_blocks_on_road[0][1] = 'Behind'

		for i in range(len(self.all_arithmetic_blocks_on_road) - 1):
			if self.all_arithmetic_blocks_on_road[i][1] == 'Behind' and \
			self.all_arithmetic_blocks_on_road[i + 1][1] == 'Ahead':
				self.all_arithmetic_blocks_on_road[i + 1][1] = 'Behind'
				print('Ball OVERJUMPED Block. SET new block status - Behind')
				break
			elif self.all_arithmetic_blocks_on_road[i][1] == 'Ahead' and \
			self.all_arithmetic_blocks_on_road[i + 1][1] == 'Ahead':
				self.all_arithmetic_blocks_on_road[i][1] = 'Behind'
				print('Ball OVERJUMPED Block. SET new block status - Behind')
				break

	def update_blocks_status_after_ball_jumping(self):
		return self.all_arithmetic_blocks_on_road

	def get_ball_status(self):
		return self.ball_status

	def get_ball_center_coordinates(self):
		return self.ball_center_coordinates

	def set_new_game_FPS(self, game_fps = 40):
		self.new_ball_jump_FPS = game_fps

	def check_game_FPS_changing(self):
		if self.start_ball_jump_FPS != self.new_ball_jump_FPS:
			self.set_new_ball_accelerations_for_jump_in_diff_FPS_for_same_moving()
			self.set_new_start_game_FPS(self.new_ball_jump_FPS)
			return True
		else:
			return False

	def set_new_start_game_FPS(self, new_fps = 10):
		self.start_ball_jump_FPS = new_fps

	def set_new_ball_accelerations_for_jump_in_diff_FPS_for_same_moving(self):
		temp_up_jump_parameters = opt_jump.get_acceleration_v0_steps_for_S_and_FPS_up_jump(self.new_ball_jump_FPS)
		self.start_ball_jump_speed = temp_up_jump_parameters[0]
		self.ball_jump_speed = self.start_ball_jump_speed
		print('New ball jump speed(up) =', self.start_ball_jump_speed)
		self.acceleration_of_ball_speed_to_up = temp_up_jump_parameters[1]
		temp_down_jump_parameters = opt_jump.get_new_acceleration_for_new_FPS_down_jump(self.new_ball_jump_FPS)
		self.acceleration_of_ball_speed_to_down = temp_down_jump_parameters[0]
		print('New ball acceleration_of_ball_speed_to_up =', self.acceleration_of_ball_speed_to_up)
		print('New ball acceleration_of_ball_speed_to_down =', self.acceleration_of_ball_speed_to_down)

	def set_road_height(self, road_Y_coordinate):
		self.height_of_road = road_Y_coordinate

	def set_new_ball_Y_coordinate_as_correction(self):
		self.ball_center_coordinates[1] = self.height_of_road - self.ball_radius - 2
		self.ball_start_center_coordinates[1] = self.height_of_road - self.ball_radius - 2

	def set_new_start_ball_Y_center_coordinate_when_road_height_changed(self):
		new_start_ball_Y_center_coordinate = self.ball_start_center_coordinates[1] + (self.height_of_road - self.start_height_of_road)
		self.ball_start_center_coordinates[1] = new_start_ball_Y_center_coordinate

	def set_new_current_ball_Y_center_coordinate_when_road_height_changed(self):
		self.ball_center_coordinates[1] = self.ball_start_center_coordinates[1]

	def ball_changing_coordinates_when_falling_from_road(self):
		if self.ball_center_coordinates[1] >= self.height_of_road + 50:
			self.ball_status = 'game_over'
		else:
			self.ball_center_coordinates[1] += self.ball_jump_speed
			# self.ball_move_distance += self.ball_jump_speed
			self.ball_jump_speed += self.acceleration_of_ball_speed_to_down

	def is_changed_road_height(self):
		if self.start_height_of_road != self.height_of_road:
			return True
		else:
			return False

	def set_new_ball_jump_total_distance_when_road_height_changed(self):
		self.ball_jump_total_distance += (self.height_of_road - self.start_height_of_road)

	def set_new_current_ball_Y_center_coordinate_when_ball_jumped_from_block_to_road(self):
		self.ball_center_coordinates[1] = self.ball_start_center_coordinates[1]

	def set_new_start_ball_Y_coordinate_when_ball_jumped_from_block_to_road(self):
		new_start_ball_Y_center_coordinate = self.height_of_road - self.ball_radius - 2
		self.ball_start_center_coordinates[1] = new_start_ball_Y_center_coordinate

	def check_ball_collision_with_arithmetic_block_and_set_new_ball_XY(self, arithmetic_block_obj):
		arithmetic_block_parameters = arithmetic_block_obj.get_block_parameters()
		aritmetic_block_width = arithmetic_block_parameters[2]
		
		if self.ball_center_coordinates[0] + self.ball_radius > arithmetic_block_parameters[0] and \
		self.ball_center_coordinates[1] + self.ball_radius > arithmetic_block_parameters[1] and \
		not self.ball_over_arithmetic_block_surface(arithmetic_block_obj) and \
		not self.arithmetic_block_behind_ball():
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

	def set_new_current_ball_Y_coordinate_when_collision_with_block_surface(self):
		self.ball_center_coordinates = self.ball_start_center_coordinates

	def set_new_start_ball_XY_coordinates_when_collision_with_block_surface(self, arithmetic_block_obj, new_ball_X_coordinate):
		arithmetic_block_parameters = arithmetic_block_obj.get_block_parameters()
		self.ball_start_center_coordinates[1] = arithmetic_block_parameters[1] - self.ball_radius
		self.ball_start_center_coordinates[0] = new_ball_X_coordinate

	def ball_over_arithmetic_block_surface(self, arithmetic_block_obj):
		if arithmetic_block_obj == False:
			return False

		arithmetic_block_parameters = arithmetic_block_obj.get_block_parameters()
		aritmetic_block_width = arithmetic_block_parameters[2]
		
		if self.ball_center_coordinates[0] >= arithmetic_block_parameters[0] and \
		(self.ball_center_coordinates[0] <= arithmetic_block_parameters[0] + aritmetic_block_width):
			return True
		else:
			return False

	def arithmetic_block_behind_ball(self):
		arithmetic_block_parameters = self.arithmetic_block.get_block_parameters()
		block_start_coordinate = arithmetic_block_parameters[0]
		block_width = arithmetic_block_parameters[2]
		if self.ball_center_coordinates[0] > block_start_coordinate + block_width:
			return True
		else:
			return False

	def ball_overjumped_or_fell_from_arithmetic_block(self):
		if self.ball_status in ('ball_jumped_from_block_to_road', 'ball_fell_from_block_to_road'):
			return True
		else:
			return False

	def change_ball_coordinates_when_falling_from_block(self):
		if self.ball_center_coordinates[1] + self.ball_radius >= self.height_of_road:
			self.ball_status = 'ball_fell_from_block_to_road'
		else:
			self.ball_center_coordinates[1] += self.ball_jump_speed
			self.ball_jump_speed += self.acceleration_of_ball_speed_to_down
			self.ball_status = 'ball_falling_from_block'

	def ball_fell_from_block_to_road(self):
		if self.ball_status == 'ball_fell_from_block_to_road':
			self.ball_start_center_coordinates[1] = self.height_of_road - self.ball_radius - 2
			self.ball_center_coordinates[1] = self.height_of_road - self.ball_radius - 2
			print('WARNING! Ball FELL from BLOCK to ROAD!')
			self.set_initial_ball_parameters_for_jump()
			if not self.block_for_ball_overjumping_index_number_more_then_block_max_index():
				self.index_of_current_block_for_overjumping += 1
			self.set_new_block_status_for_current_block_behind_ball()
			print('INDEX of current block =', self.index_of_current_block_for_overjumping)
			return True
		else:
			self.change_ball_coordinates_when_falling_from_block()
			return False

	def ball_beyond_game_screen(self):
		if self.ball_center_coordinates[0] <= 0:
			return True
		else:
			return False




