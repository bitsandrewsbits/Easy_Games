# game about jumping ball, which
# just jump in order to avoid holes in road line.
# The holes in roadline appear randomly during your game period, until you lose.
# This is will be first version of game.

import pygame
from random import randint
import road_ball as ball

class Jump_Game:
	def __init__(self, width_height_display = (800, 300)):
		self.display_size = width_height_display
		self.display_rgb_color = (0, 0, 0)
		self.road_distance = 0
		self.holes_amount = 1
		self.hole_size = 25
		self.road_holes_coordinates = []
		self.max_amount_of_hole_with_display_parameters = self.display_size[0] // (self.hole_size * 2)
		self.road_move_speed = 1
		self.roadlines_coordinates = []
		self.game_over = False
		self.exit_from_game = False
		self.game_clock = pygame.time.Clock()
		self.game_main_window = pygame.display.set_mode((self.display_size[0], self.display_size[1]))
		self.road_ball = ball.Game_Ball(self.game_main_window)
		self.ball_in_jump = False
		self.ball_falling_cause_game_over = False
		self.iterations_per_second = 40

	def init_game_parameters(self):
		pygame.init()

	def start_game(self):
		self.init_game_parameters()
		self.start_game_menu()

		while self.game_over == False and self.exit_from_game == False:
			self.game_clock.tick(self.iterations_per_second)
			self.game_interface()
			
			for game_event in pygame.event.get():
				if game_event.type == pygame.QUIT:
					self.exit_from_game = True
				
				if game_event.type == pygame.KEYDOWN:
					if game_event.key == pygame.K_UP:
						self.ball_in_jump = True
					if game_event.key == pygame.K_ESCAPE:
						self.exit_game_menu_window()

			pressed_buttons = pygame.key.get_pressed()
			if pressed_buttons[pygame.K_RIGHT]:
				if self.road_ball.get_ball_center_coordinates()[0] < self.display_size[0]:
					self.road_ball.ball_move_right()
			if pressed_buttons[pygame.K_LEFT]:
				if self.road_ball.get_ball_center_coordinates()[0] > self.road_ball.ball_start_center_coordinates[0]:
					self.road_ball.ball_move_left()

			pygame.display.update()

	def game_interface(self):
		self.game_main_window.fill(self.display_rgb_color)
		self.check_on_ball_jump()

		if self.check_ball_coordinates_when_need_to_fall() == 'ball_falling_cause_game_over':
			self.ball_falling_cause_game_over = True
		if self.ball_falling_cause_game_over:
			self.ball_falling_when_game_over()

		self.show_road_passed_distance()
		self.game_roadline()

	def check_on_ball_jump(self):
		if not self.ball_in_jump:
			self.road_ball.draw_ball()
		elif self.ball_in_jump:
			if self.road_ball.get_ball_jump_status() == 'Ball_in_jump':
				self.road_ball.ball_jump()
			if self.road_ball.get_ball_jump_status() == 'Ball_jumped':
				self.ball_in_jump = False

	def check_ball_coordinates_when_need_to_fall(self):
		ball_succesful_jumped_and_on_the_road = True
		current_ball_X_coordinate = self.road_ball.get_ball_center_coordinates()[0]
		current_ball_Y_coordinate = self.road_ball.get_ball_center_coordinates()[1]
		road_Y_coordinate = 200

		if len(self.roadlines_coordinates) > 0:
			for i in range(1, len(self.roadlines_coordinates), 2):
				if current_ball_X_coordinate > self.roadlines_coordinates[i][0] and \
				    current_ball_X_coordinate < self.roadlines_coordinates[i + 1][0]:
				    if current_ball_Y_coordinate > road_Y_coordinate or self.road_ball.get_ball_status() in ('move_on_road', 'ball_jumped'):
				    	print('Ball is falling...Game Over')
				    	return 'ball_falling_cause_game_over'

	def ball_falling_when_game_over(self):
		if self.road_ball.get_ball_status() != 'game_over':
			self.road_ball.ball_changing_coordinates_when_falling_from_road()

	def game_roadline(self):
		self.show_and_move_game_road()

	def create_lines_coordinates(self, start_road_coordinates = 1, end_road_coordinates = 1):
		result_lines_coordinates = []
		start_roadline_coordinates = [start_road_coordinates, 200]
		end_roadline_coordinates = [end_road_coordinates, 200]
		hole_end_coordinates = 25
		self.road_holes_coordinates = [randint(start_road_coordinates, end_road_coordinates)]
		
		result_lines_coordinates.append(start_roadline_coordinates)
		if self.max_amount_of_hole_with_display_parameters < self.holes_amount:
			print('Warning. Achived MAX possible amount of holes in road for this display parameters.')
			print(f'Changing to MAX possible amount of holes: {max_amount_of_hole_with_display_parameters}')
			self.holes_amount = max_amount_of_hole_with_display_parameters

		if self.holes_amount == 1:
			hole_random_start_coordinates = self.road_holes_coordinates[0]
			result_lines_coordinates.append([hole_random_start_coordinates, 200])
			hole_end_coordinates = hole_random_start_coordinates + self.hole_size
			result_lines_coordinates.append([hole_end_coordinates, 200])
			result_lines_coordinates.append(end_roadline_coordinates)
		elif self.holes_amount > 1:
			self.generate_random_hole_start_coordinates()
			for random_hole_start_coordinates in self.road_holes_coordinates:
				result_lines_coordinates.append([random_hole_start_coordinates, 200])
				hole_end_coordinates = random_hole_start_coordinates + self.hole_size
				result_lines_coordinates.append([hole_end_coordinates, 200])
			result_lines_coordinates.append(end_roadline_coordinates)

		return result_lines_coordinates

	def generate_random_hole_start_coordinates(self):
		start_road_coordinates = self.display_size[0]
		end_road_coordinates = 2 * self.display_size[0]
		for i in range(self.holes_amount - 1):
			find_right_hole_coordinate = False
			while not find_right_hole_coordinate:
				wrong_coordinate_flag = False
				hole_random_start_coordinates = randint(start_road_coordinates, end_road_coordinates)
			
				for hole_start_coordinate in self.road_holes_coordinates:
					if hole_random_start_coordinates > hole_start_coordinate:
						if hole_random_start_coordinates > hole_start_coordinate + 2 * self.hole_size:
							wrong_coordinate_flag = False
						else:
							wrong_coordinate_flag = True
							break
						
					elif hole_random_start_coordinates < hole_start_coordinate:
						if hole_random_start_coordinates < hole_start_coordinate - 2 * self.hole_size:
							wrong_coordinate_flag = False
						else:
							wrong_coordinate_flag = True
							break

				if not wrong_coordinate_flag:
					if hole_random_start_coordinates not in self.road_holes_coordinates:
						self.road_holes_coordinates.append(hole_random_start_coordinates)
					
					self.road_holes_coordinates = sorted(self.road_holes_coordinates)
					find_right_hole_coordinate = True

		print('Hole coordinates:', self.road_holes_coordinates)

	def show_and_move_game_road(self):
		self.manage_road_coordinates()
		
		road_rgb_color = (60, 250, 60)
		for coordinates in self.roadlines_coordinates:
			coordinates[0] = coordinates[0] - self.road_move_speed
		
		for i in range(0, len(self.roadlines_coordinates), 2):
			pygame.draw.line(self.game_main_window, road_rgb_color, 
				self.roadlines_coordinates[i], self.roadlines_coordinates[i + 1], 5)
		
		if self.road_ball.get_ball_status() != 'game_over':
			self.road_distance += 1
		
		if self.road_distance % self.display_size[0] == 0 and self.road_distance != 0:
			print('Distance:', self.road_distance)
			print('Adding new hole...')
			self.holes_amount += 1
			print('Amount of holes =', self.holes_amount)
			self.iterations_per_second += 5

	def manage_road_coordinates(self):
		if self.road_distance == 0:
			print('Start adding coordinates...(distance = 0)')
			self.set_up_start_roadline_coordinates()
			print(self.roadlines_coordinates)
		elif self.road_distance % self.display_size[0] == 0:
			self.remove_road_coordinates_beyond_screen()
			print('Coordinates after removing.')
			print(self.roadlines_coordinates)
			print(f'Another adding coordinates...(distance = {self.road_distance})')
			tmp_road_coordinates = self.create_lines_coordinates(self.display_size[0], 2 * self.display_size[0])
			self.roadlines_coordinates += tmp_road_coordinates
			print(self.roadlines_coordinates)

	def set_up_start_roadline_coordinates(self):
		self.roadlines_coordinates = self.create_lines_coordinates(0, self.display_size[0] - self.hole_size)
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

	def show_road_passed_distance(self):
		passed_distance_block_width_height = (100, 45)
		passed_distance_block_coordinates = [self.display_size[0] - passed_distance_block_width_height[0] * 2, 0,
											 self.display_size[0] - passed_distance_block_width_height[0],
											 passed_distance_block_width_height[1] * 2]
		pygame.draw.rect(self.game_main_window, (100, 100, 100), passed_distance_block_coordinates)
		font_of_text_in_distance_block = pygame.font.Font('freesansbold.ttf', 20)
		
		passed_distance_as_number = font_of_text_in_distance_block.render(f'{self.road_distance}', True, (150, 200, 100), (100, 100, 100))
		passed_distance_as_number_Rect = passed_distance_as_number.get_rect()
		passed_distance_as_number_Rect.center = ((passed_distance_block_coordinates[0] + passed_distance_block_coordinates[2]) // 2 + 20,
												 (passed_distance_block_coordinates[1] + passed_distance_block_coordinates[3]) // 2 + 20)			
		self.game_main_window.blit(passed_distance_as_number, passed_distance_as_number_Rect)

		passed_distance_Block_title = font_of_text_in_distance_block.render('Passed distance:', True, (100, 250, 150), (100, 100, 100))
		passed_distance_Block_Title_Rect = passed_distance_as_number.get_rect()
		passed_distance_Block_Title_Rect.center = ((passed_distance_block_coordinates[0] + passed_distance_block_coordinates[2]) // 2 - 25,
												 (passed_distance_block_coordinates[1] + passed_distance_block_coordinates[3]) // 2 - 15)			
		self.game_main_window.blit(passed_distance_Block_title, passed_distance_Block_Title_Rect)

	def get_start_button_parameters(self):
		start_button_size = (150, 50)
		start_button_parameters = (self.display_size[0] // 2 - 70, self.display_size[1] // 2, 
									start_button_size[0], start_button_size[1])
		return start_button_parameters

	def start_game_button(self):
		start_button_size = (150, 50)
		start_button_parameters = self.get_start_button_parameters()

		pygame.draw.rect(self.game_main_window, (50, 200, 50), start_button_parameters)
		font_of_text_in_start_button = pygame.font.Font('freesansbold.ttf', 20)
		start_button_text = font_of_text_in_start_button.render('Start game', True, (10, 20, 250), (50, 200, 50))
		start_button_text_Rect = start_button_text.get_rect()
		start_button_text_Rect.center = (start_button_parameters[0] + start_button_size[0] - 70, 
			                             start_button_parameters[1] + start_button_size[1] // 2)			
		self.game_main_window.blit(start_button_text, start_button_text_Rect)

	def get_mouse_XY_coordinate(self):
		return pygame.mouse.get_pos()

	def mouse_coordinates_in_button_space(self):
		start_button_size = (150, 50)
		if self.get_mouse_XY_coordinate()[0] >= self.get_start_button_parameters()[0] and \
		        self.get_mouse_XY_coordinate()[0] <= self.get_start_button_parameters()[0] + start_button_size[0] and \
		        self.get_mouse_XY_coordinate()[1] >= self.get_start_button_parameters()[1] and \
		   		self.get_mouse_XY_coordinate()[1] <= self.get_start_button_parameters()[1] + start_button_size[1]:
		   	return True
		else:
			return False

	def start_game_menu(self):
		start_game = False
		while not start_game:
			self.start_game_button()
			for game_event in pygame.event.get():
				if game_event.type == pygame.MOUSEBUTTONDOWN:
					if self.mouse_coordinates_in_button_space():
						start_game = True

			pygame.display.update()

	def exit_game_menu_window(self):
		exit_window_size = (300, 200)
		font_of_text_in_exit_window = pygame.font.Font('freesansbold.ttf', 20)
		exit_window_parameters = (self.display_size[0] // 3, 50, exit_window_size[0], exit_window_size[1])
		exit_title_XY_center = (exit_window_parameters[0] * 1.5, exit_window_parameters[1] + 20)

		while not self.exit_from_game:
			exit_window_Rect = pygame.draw.rect(self.game_main_window, (100, 200, 90), exit_window_parameters)
			exit_window_title = font_of_text_in_exit_window.render('Pause', True, (150, 200, 100), (100, 100, 100))
			exit_title_Rect = exit_window_title.get_rect()
			exit_title_Rect.center = exit_title_XY_center
			self.game_main_window.blit(exit_window_title, exit_title_Rect)
			self.exit_game_button()

			for game_event in pygame.event.get():
				if game_event.type == pygame.MOUSEBUTTONDOWN:
					if self.exit_game_button_pressed() == True:
						self.exit_from_game = True
						break

			pygame.display.update()

	def exit_game_button(self):
		exit_button_size = (100, 50)
		exit_button_font_text = pygame.font.Font('freesansbold.ttf', 15)
		exit_button_parameters = self.get_exit_button_parameters()
		exit_button_text_XY_center = (exit_button_parameters[0] + 50, exit_button_parameters[1] + 20)
		
		exit_button_Rect = pygame.draw.rect(self.game_main_window, (10, 20, 10), exit_button_parameters)
		exit_button_text = exit_button_font_text.render('Exit', True, (10, 250, 10), (10, 20, 10))
		exit_button_text_Rect = exit_button_text.get_rect()
		exit_button_text_Rect.center = exit_button_text_XY_center
		self.game_main_window.blit(exit_button_text, exit_button_text_Rect)

	def exit_game_button_pressed(self):
		exit_button_size = (100, 50)
		if self.get_mouse_XY_coordinate()[0] >= self.get_exit_button_parameters()[0] and \
		        self.get_mouse_XY_coordinate()[0] <= self.get_exit_button_parameters()[0] + exit_button_size[0] and \
		        self.get_mouse_XY_coordinate()[1] >= self.get_exit_button_parameters()[1] and \
		   		self.get_mouse_XY_coordinate()[1] <= self.get_exit_button_parameters()[1] + exit_button_size[1]:
		   	return True
		else:
			return False

	def get_exit_button_parameters(self):
		exit_button_size = (100, 50)
		return (self.display_size[0] // 3 + 50, 100, exit_button_size[0], exit_button_size[1])


	def continue_game_button(self):
		print('resuming game...')

#testing
game = Jump_Game()
game.start_game()