# file with class Ball for game

import pygame as pg

class Game_Ball:
	def __init__(self, screen_surface, radius = 10, ball_color = 'yellow'):
		self.ball_radius = radius
		self.ball_color = ball_color
		self.screen_surface = screen_surface
		self.ball_center_coordinates = [20, 188]

	def draw_ball(self):
		pg.draw.circle(self.screen_surface, self.ball_color, self.ball_center_coordinates, self.ball_radius)


	def ball_jump(self):
		ball_jump_high = 60    #jump max high 
		ball_jump_start_speed = 30  #pixels/sec
		ball_jump_speed_on_top = 0
		ball_jump_speed_on_bottom = 0
		acceleration_of_ball_speed_to_up = -0.75   #pixels/sec^2
		acceleration_of_ball_speed_to_down = 0.3
		ball_jump_total_distance = 120 
		ball_jump_to_up = True
		ball_jump_to_down = False

		while not ball_jump_to_down and ball_jump_total_distance > 0:
			if ball_jump_to_up:
				pass 
