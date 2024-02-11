# file with class Ball for game

import pygame as pg

class Game_Ball:
	def __init__(self, screen_surface, radius = 10, ball_color = 'yellow'):
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

	def draw_ball(self):
		pg.draw.circle(self.screen_surface, self.ball_color, self.ball_center_coordinates, self.ball_radius)

	def ball_jump(self):
		# print('Ball coordinate center:', self.ball_center_coordinates)
		# print('Ball current speed:', self.ball_jump_speed)
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

	def get_ball_jump_status(self):
		if self.ball_move_distance + self.ball_jump_speed >= self.ball_jump_total_distance:
			# print('Current ball move distance + current speed of ball:', self.ball_move_distance + self.ball_jump_speed)
			# print('Ball has done JUMP!')
			self.ball_center_coordinates[1] = self.ball_start_center_coordinates[1]
			self.ball_jump_to_down = False
			self.ball_jump_to_up = True
			self.ball_move_distance = 0
			self.ball_jump_speed = 9
			self.ball_status = 'ball_jumped'
			return 'Ball_jumped'
		else:
			# print('Current ball jump distance:', self.ball_move_distance)
			self.ball_status = 'ball_in_jump'
			return 'Ball_in_jump'

	def get_ball_status(self):
		return self.ball_status

	def get_ball_center_coordinates(self):
		return self.ball_center_coordinates

	def ball_falling_from_road_surface(self):
		if self.ball_center_coordinates >= self.ball_start_center_coordinates[1] + 100:   # just for test
			self.ball_status = 'game_over'
		else:
			self.ball_center_coordinates[1] += self.ball_jump_speed
			self.ball_move_distance += self.ball_jump_speed
			self.ball_jump_speed += self.acceleration_of_ball_speed_to_down




























