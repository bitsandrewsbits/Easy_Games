# game about jumping ball, which
# just jump in order to avoid holes in road line.
# The holes in roadline appear randomly during your game period, until you lose.
# This is will be first version of game.

import pygame
from random import randint
import road_ball as ball
import game_menu_class as menu
import menu_button_class as button
import arithmetic_block_obstacle_class as block_obsticle
import input_answer_window_class as input_ans

class Jump_Game:
	def __init__(self, width_height_display = (800, 300)):
		self.display_size = width_height_display
		self.display_rgb_color = (0, 0, 0)
		self.road_distance = 0
		self.holes_amount = 1
		self.hole_size = 45
		self.road_holes_coordinates = []
		self.max_amount_of_hole_with_display_parameters = self.display_size[0] // (self.hole_size * 2)
		self.road_move_speed = 1
		self.roadlines_coordinates = []
		self.road_height = 200
		self.temporary_random_road_height = 200
		self.game_over = False
		self.exit_from_game = False
		self.game_parameters_reseted = False
		self.game_clock = pygame.time.Clock()
		self.game_main_window = pygame.display.set_mode((self.display_size[0], self.display_size[1]))
		self.road_ball = ball.Game_Ball(self.game_main_window, self.road_height)
		self.ball_in_jump = False
		self.ball_falling_cause_game_over = False
		self.check_for_fall_from_block_to_road = False
		self.amount_of_jumps = 0
		self.iterations_per_second = 40
		self.start_menu_executed = False
		self.start_menu_annotation = """Hello. Glad you see here! It's fanny game for developing your math skill, as known as arithmetics with numbers. You need to overjump holes that appear on road and try to resolve math example and input right answer for it or you are able to overjump some blocks but do it carefuly. Good Luck!"""
		self.start_menu = menu.Game_Menu(self.game_main_window, self.display_size, "Start", 
					                     (600, 200), (100, 100, 100), ['Start', 'Exit'], {}, self.start_menu_annotation)
		self.exit_menu = menu.Game_Menu(self.game_main_window, self.display_size, "Pause", 
					                     (300, 200), (100, 100, 100), ['Exit', 'Continue', "New Game"])
		self.icon_image = "risky_jumps_game_icon.png"
		self.arithmetic_blocks_and_status_for_ball = []
		self.change_road_block_parameters_friequency_by_passed_distance = 800
		self.user_input_window = input_ans.Input_Answer_Window(self.game_main_window, self.display_size)
		self.block_index_for_deleting_when_user_answer_is_right = 0

	def init_game_parameters(self):
		pygame.display.set_caption('Risky Jumps')
		game_icon = pygame.image.load(self.icon_image)
		pygame.display.set_icon(game_icon)
		pygame.init()

	def start_game(self):
		self.init_game_parameters()

		while self.game_over == False and self.exit_from_game == False:
			self.game_clock.tick(self.iterations_per_second)
			self.game_interface()
			
			for game_event in pygame.event.get():
				if game_event.type == pygame.QUIT:
					self.exit_from_game = True
				
				if game_event.type == pygame.KEYDOWN:
					self.user_input_window.implement_user_input(game_event)
					if self.user_answer_and_right_answer_for_any_blocks_matched(game_event):
						self.remove_block_when_user_answer_is_right()
					if game_event.key == pygame.K_UP and self.road_ball.get_ball_status() != 'game_over':
						self.ball_in_jump = True
						# self.ball_start_jumping_sound()
					if game_event.key == pygame.K_ESCAPE:
						menu_button_name_and_status = self.exit_menu.menu_displaying()
						if menu_button_name_and_status[1] == True and menu_button_name_and_status[0] == 'Exit':
							print('Exitting from game...', menu_button_name_and_status)
							self.exit_from_game = True
						elif menu_button_name_and_status[1] == True and menu_button_name_and_status[0] == 'New Game':
							print('Starting a new game...', menu_button_name_and_status)
							print('Reseting game parameters...')
							self.reset_game_parameters_to_start()
							self.game_parameters_reseted = True


			pressed_buttons = pygame.key.get_pressed()
			if pressed_buttons[pygame.K_RIGHT]:
				if self.road_ball.get_ball_center_coordinates()[0] < self.display_size[0]:
					self.road_ball.ball_move_right()
			if pressed_buttons[pygame.K_LEFT]:
				if self.road_ball.get_ball_center_coordinates()[0] > self.road_ball.ball_start_center_coordinates[0]:
					self.road_ball.ball_move_left()

			pygame.display.update()

	def remove_block_when_user_answer_is_right(self):
		self.arithmetic_blocks_and_status_for_ball.pop(self.block_index_for_deleting_when_user_answer_is_right)

	def user_answer_and_right_answer_for_any_blocks_matched(self, user_event):
		if self.user_input_window.enter_button_pressed(user_event):
			user_answer = self.user_input_window.get_user_input_answer_as_number()

			for i in range(len(self.arithmetic_blocks_and_status_for_ball)):
				if self.arithmetic_blocks_and_status_for_ball[i][0].right_answer_for_block_math_example == user_answer:
					self.block_index_for_deleting_when_user_answer_is_right = i
					return True

			return False

	def reset_game_parameters_to_start(self):
		self.road_distance = 0
		self.holes_amount = 1
		self.road_holes_coordinates = []
		self.road_move_speed = 1
		self.roadlines_coordinates = []
		self.start_road_height = 200
		self.temporary_random_road_height = 200
		self.game_over = False
		self.exit_from_game = False
		self.game_parameters_reseted = True
		self.game_clock = pygame.time.Clock()
		self.road_ball = ball.Game_Ball(self.game_main_window, self.road_height)
		self.ball_in_jump = False
		self.ball_falling_cause_game_over = False
		self.check_for_fall_from_block_to_road = False
		self.road_ball.ball_status = 'move_on_road'
		self.iterations_per_second = 40
		self.amount_of_jumps = 0
		self.arithmetic_blocks_and_status_for_ball = []
		self.user_input_window = input_ans.Input_Answer_Window(self.game_main_window, self.display_size)

	def game_interface(self):
		self.game_main_window.fill(self.display_rgb_color)
		if not self.start_menu_executed:
			self.start_game_menu()

		self.user_input_window.display_entire_input_window()

		self.check_on_ball_jump()
		self.check_ball_coordinates_when_need_to_fall_from_road_into_hole()
		
		self.check_ball_fell_from_block_to_road()

		self.show_road_passed_distance()
		self.game_roadline()
		self.arithmetic_blocks_obstacle_on_road()

	def start_game_menu(self):
		menu_button_name_and_status = self.start_menu.menu_displaying()
		if menu_button_name_and_status[1] == True and menu_button_name_and_status[0] == 'Exit':
			print('Exitting from game...', menu_button_name_and_status)
			self.exit_from_game = True
		elif menu_button_name_and_status[1] == True and menu_button_name_and_status[0] == 'Start':
			print('Starting first game...')
			self.start_menu_executed = True

	def check_ball_coordinates_when_need_to_fall_from_road_into_hole(self):
		if not self.ball_falling_cause_game_over:
			
			if self.road_ball.get_ball_status() == 'ball_falling_into_hole':
				self.ball_falling_cause_game_over = True
			else:
				self.set_ball_game_over_status_need_to_fall_into_hole()
		
		else:
			self.ball_falling_when_game_over()

	def check_ball_fell_from_block_to_road(self):
		if self.check_for_fall_from_block_to_road:
			if self.road_ball.ball_fell_from_block_to_road():
				self.check_for_fall_from_block_to_road = False

	def set_new_ball_XY_coordinates_when_collision_with_arithmetic_block(self):
		if self.arithmetic_blocks_and_status_for_ball != []:
			self.road_ball.check_ball_collision_with_arithmetic_block_and_set_new_ball_XY(self.road_ball.arithmetic_block)

	def check_on_ball_jump(self):
		# print('Ball status:', self.road_ball.get_ball_status())
		if self.road_ball.ball_beyond_game_screen():
			self.show_game_over_menu()

		self.road_ball.set_new_game_FPS(self.iterations_per_second)
		self.road_ball.check_game_FPS_changing()
		self.road_ball.get_all_arithmetic_blocks_and_status_for_ball(self.arithmetic_blocks_and_status_for_ball)
		self.arithmetic_blocks_and_status_for_ball = self.road_ball.update_blocks_status_after_ball_jumping()
		self.road_ball.get_arithmetic_block_that_closest_to_ball()
		
		if self.arithmetic_blocks_and_status_for_ball != []:
			if self.road_ball.arithmetic_block_behind_ball() and self.ball_in_jump:
				# print('Ball jump status:', self.road_ball.get_ball_status())
				self.check_for_fall_from_block_to_road = False

			elif self.road_ball.arithmetic_block_behind_ball() and not self.ball_in_jump and \
			self.road_ball.get_ball_status() not in ('ball_fell_from_block_to_road', 'move_on_road'):
				self.check_for_fall_from_block_to_road = True

		self.set_new_ball_XY_coordinates_when_collision_with_arithmetic_block()
		if not self.ball_in_jump:
			self.road_ball.draw_ball()
		elif self.ball_in_jump:
			self.check_is_road_height_changed()
			self.road_ball.ball_jump()
			self.road_ball.set_ball_jump_status_in_different_cases()
			
			current_ball_status = self.road_ball.get_ball_status()
			# print('Ball jump status:', current_ball_status)

			if current_ball_status in ('ball_jumped_from_road_to_road', 'ball_jumped_to_block', 'ball_jumped_from_block_to_road'):
				print('WARNING! Ball jumped!')
				# print('Current ball status:', current_ball_status)
				self.ball_in_jump = False
				self.amount_of_jumps += 1

	def set_ball_game_over_status_need_to_fall_into_hole(self):
		ball_XY_coordinates = self.road_ball.get_ball_center_coordinates()
		current_ball_X_coordinate = ball_XY_coordinates[0]
		current_ball_Y_coordinate = ball_XY_coordinates[1]

		if len(self.roadlines_coordinates) > 0:
			for i in range(1, len(self.roadlines_coordinates), 2):
				if current_ball_X_coordinate > self.roadlines_coordinates[i][0] and \
				    current_ball_X_coordinate < self.roadlines_coordinates[i + 1][0]:
				    # print('Ball in hole area!!!')
				    # print('Ball status:', self.road_ball.get_ball_status())
				    if self.road_ball.get_ball_status() in ('move_on_road', 'ball_jumped_from_road_to_road', 
				    'ball_jumped_from_block_to_road', 'ball_on_road_level') or \
				    (self.road_ball.get_ball_status() in ('ball_in_jump_from_road_to_road', 
				    'ball_in_jump_from_block_to_road') and self.road_ball.ball_jump_to_down):
				    	print('Ball is falling...Game Over')
				    	self.road_ball.ball_status = 'ball_falling_into_hole'

	def ball_falling_when_game_over(self):
		if self.road_ball.get_ball_status() != 'game_over':
			self.road_ball.ball_changing_coordinates_when_falling_from_road()
		else:
			self.show_game_over_menu()

	def show_game_over_menu(self):
		game_over_menu = menu.Game_Menu(self.game_main_window, self.display_size, "Game Over", 
								(350, 200), (120, 140, 130), ['New Game', 'Exit'], 
								{"Passed Distance:": self.road_distance, "Jumps amount:": self.amount_of_jumps})
		pressed_button_in_game_over_menu = game_over_menu.menu_displaying()[0]
		if pressed_button_in_game_over_menu == 'Exit':
			self.exit_from_game = True
		if pressed_button_in_game_over_menu == 'New Game':
			self.reset_game_parameters_to_start()

	def ball_start_jumping_sound(self):
		ball_jumping_sound = pygame.mixer.Sound("ball_jumped.wav")
		pygame.mixer.Sound.play(ball_jumping_sound)
		pygame.mixer.music.stop()

	def game_roadline(self):
		self.show_and_move_game_road()

	def get_first_arithmetic_block(self):
		if self.arithmetic_blocks_and_status_for_ball != []:
			return self.arithmetic_blocks_and_status_for_ball[0][0]
		else:
			return False

	def arithmetic_blocks_obstacle_on_road(self):
		if self.arithmetic_blocks_and_status_for_ball != []:
			if self.arithmetic_block_beyond_game_screen():
				self.delete_arithmetic_block_beyond_game_screen()
			
			for arithmetic_block in self.arithmetic_blocks_and_status_for_ball:
				arithmetic_block[0].draw_block_on_game_road()
				arithmetic_block[0].set_new_X_coordinate_when_block_moving()

	def arithmetic_block_beyond_game_screen(self):
		for arithmetic_block in self.arithmetic_blocks_and_status_for_ball:
			block_width = arithmetic_block[0].get_block_parameters()[2]
			if arithmetic_block[0].get_block_parameters()[0] + block_width < 0:
				return True

		return False

	def delete_arithmetic_block_beyond_game_screen(self):
		print('Block is BEYOND game screen. deleting block...')
		self.arithmetic_blocks_and_status_for_ball.remove(self.arithmetic_blocks_and_status_for_ball[0])
		self.road_ball.index_of_current_block_for_overjumping -= 1

	def create_lines_coordinates(self, start_road_coordinates = 1, end_road_coordinates = 1):
		result_lines_coordinates = []
		temp_random_road_height = self.temporary_random_road_height
		
		start_roadline_coordinates = [start_road_coordinates, self.temporary_random_road_height]
		result_lines_coordinates.append(start_roadline_coordinates)

		self.generate_random_hole_start_coordinates(start_road_coordinates, end_road_coordinates)
		
		for i in range(len(self.road_holes_coordinates)):
			result_lines_coordinates.append([self.road_holes_coordinates[i], temp_random_road_height])
			hole_end_coordinates = self.road_holes_coordinates[i] + self.hole_size
			
			if i % 2 == 0:
				temp_random_road_height = randint(180, 250)

			result_lines_coordinates.append([hole_end_coordinates, temp_random_road_height])
		
		result_lines_coordinates.append([end_road_coordinates, temp_random_road_height])
		print(result_lines_coordinates)

		self.temporary_random_road_height = temp_random_road_height

		return result_lines_coordinates

	def generate_random_hole_start_coordinates(self, start_road_coordinates, end_road_coordinates):
		end_road_coordinates = end_road_coordinates - 2 * self.hole_size
		self.road_holes_coordinates = []
		for i in range(self.holes_amount):
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
		
		if self.road_distance % self.change_road_block_parameters_friequency_by_passed_distance == 0 and \
		self.road_distance != 0:
			print('Distance:', self.road_distance)
			print('Adding new hole...')
			self.holes_amount += 1
			print('Amount of holes =', self.holes_amount)
		if self.road_ball.get_ball_status() in ('move_on_road', 'ball_jumped_from_road_to_road', 'ball_on_block', 
		'ball_jumped_from_block_to_road'):
			if self.road_distance % 200 == 0 and self.road_distance != 0:
				self.iterations_per_second += 2

	def manage_road_coordinates(self):
		if self.road_distance == 0:
			print('Start adding coordinates...(distance = 0)')
			self.set_up_start_roadline_coordinates()
			print(self.roadlines_coordinates)
		elif self.road_distance % self.change_road_block_parameters_friequency_by_passed_distance == 0:
			self.remove_road_coordinates_beyond_screen()
			print('Coordinates after removing.')
			print(self.roadlines_coordinates)
			print(f'Another adding coordinates...(distance = {self.road_distance})')
			tmp_road_coordinates = self.create_lines_coordinates(self.display_size[0], 2 * self.display_size[0])
			self.roadlines_coordinates += tmp_road_coordinates
			print(self.roadlines_coordinates)
		
		if self.road_distance % self.change_road_block_parameters_friequency_by_passed_distance == 0:
			new_block_obstacle = block_obsticle.Arithmetic_Obstacle_Block(self.game_main_window, 
																self.display_size, self.roadlines_coordinates)
			self.arithmetic_blocks_and_status_for_ball.append([new_block_obstacle, 'Ahead'])

		if self.road_distance % 100 == 0:
			print('arithmetic_blocks_and_status_for_ball:', self.arithmetic_blocks_and_status_for_ball)

	def set_up_start_roadline_coordinates(self):
		self.roadlines_coordinates = self.create_lines_coordinates(0, self.display_size[0] - self.hole_size)
		self.roadlines_coordinates += self.create_lines_coordinates(self.display_size[0], 
																	2 * self.display_size[0] - self.hole_size)

	def check_is_road_height_changed(self):
		current_ball_X_coordinate = self.road_ball.get_ball_center_coordinates()[0]

		for i in range(0, len(self.roadlines_coordinates), 2):
			if self.roadlines_coordinates[i][0] <= current_ball_X_coordinate and \
			  self.roadlines_coordinates[i + 1][0] >= current_ball_X_coordinate:
			   self.road_ball.set_road_height(self.roadlines_coordinates[i][1])
			   break

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


#testing
game = Jump_Game()
game.start_game()