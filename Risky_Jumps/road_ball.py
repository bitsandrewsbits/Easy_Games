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


	def ball_jumping(self):
		print('this is function for implementation of ball jumping')