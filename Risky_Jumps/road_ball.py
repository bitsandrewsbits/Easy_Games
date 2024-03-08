# file with class Ball for game

import pygame as pg

class Game_Ball:
	def __init__(self, screen_surface, start_road_height = 0, radius = 10, ball_color = 'yellow'):
		self.ball_radius = radius
		self.ball_color = ball_color
		self.screen_surface = screen_surface
		self.ball_start_center_coordinates = [20, 188]
		self.ball_center_coordinates = [20, 188]
		self.ball_jump_high = 60                    #jump max high (in pixels)
		self.ball_jump_speed = 9                    #pixels/frame (30 pixels/sec)
		self.ball_jump_speed_on_top = 0
		self.ball_jump_speed_on_bottom = 0
		self.acceleration_of_ball_speed_to_up = -0.75   #pixels/frame^2 (-25pixels/c^2)
		self.acceleration_of_ball_speed_to_down = 0.3   # only a = g in pixels/frame^2, g = 10 pixels/c^2
		self.ball_jump_total_distance = 120             # in pixels
		self.ball_move_distance = 0
		self.ball_jump_to_up = True
		self.ball_jump_to_down = False
		self.ball_status = 'move_on_road'
		self.start_height_of_road = start_road_height
		self.height_of_road = start_road_height
		self.need_to_change_ball_Y_coordinate = True

	def draw_ball(self):
		pg.draw.circle(self.screen_surface, self.ball_color, self.ball_center_coordinates, self.ball_radius)

	def ball_jump(self):
		if self.is_changed_road_height() and self.need_to_change_ball_Y_coordinate:
			self.set_new_start_ball_Y_center_coordinate()
			print('Road height was changed... Road height =', self.height_of_road)
			self.changing_ball_jump_total_distance()
			print('Changed Jump total distance =', self.ball_jump_total_distance)
			print('Change Start ball Y coordinate =', self.ball_start_center_coordinates[1])
			self.need_to_change_ball_Y_coordinate = False

		if self.ball_jump_to_up:
			self.ball_center_coordinates[1] -= self.ball_jump_speed
			self.ball_move_distance += self.ball_jump_speed
			self.ball_jump_speed += self.acceleration_of_ball_speed_to_up
			
		if self.ball_jump_speed == 0:
			self.ball_jump_to_up = False
			self.ball_jump_to_down = True

		if self.ball_jump_to_down:
			self.ball_center_coordinates[1] += self.ball_jump_speed
			self.ball_move_distance += self.ball_jump_speed
			self.ball_jump_speed += self.acceleration_of_ball_speed_to_down

		self.draw_ball()

	def ball_move_right(self):
		self.ball_center_coordinates[0] += 1

	def ball_move_left(self):
		self.ball_center_coordinates[0] -= 1

	def get_ball_jump_status(self):
		if self.ball_move_distance + self.ball_jump_speed >= self.ball_jump_total_distance:
			self.ball_center_coordinates[1] = self.ball_start_center_coordinates[1]
			self.ball_jump_to_down = False
			self.ball_jump_to_up = True
			self.ball_move_distance = 0
			self.ball_jump_speed = 9
			self.ball_status = 'ball_jumped'
			self.need_to_change_ball_Y_coordinate = True
			return 'Ball_jumped'
		else:
			self.ball_status = 'ball_in_jump'
			return 'Ball_in_jump'

	def get_ball_status(self):
		return self.ball_status

	def get_ball_center_coordinates(self):
		return self.ball_center_coordinates

	def set_road_height(self, road_Y_coordinate):
		self.height_of_road = road_Y_coordinate

	def set_new_start_ball_Y_center_coordinate(self):
		new_start_ball_Y_coordinate = self.ball_start_center_coordinates[1] + (self.height_of_road - self.start_height_of_road)
		self.ball_start_center_coordinates[1] = new_start_ball_Y_coordinate

	def set_new_current_ball_Y_center_coordinate(self):
		self.ball_center_coordinates[1] = self.ball_start_center_coordinates[1]

	def ball_changing_coordinates_when_falling_from_road(self):
		if self.ball_center_coordinates[1] - 100 > self.ball_start_center_coordinates[1]:   # just for test
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

	def changing_ball_jump_total_distance(self):
		self.ball_jump_total_distance += (self.height_of_road - self.start_height_of_road)




























