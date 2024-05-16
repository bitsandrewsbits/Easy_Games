# class for create input menu for answering math examples in arithmetic block
import pygame as pg

class Input_Answer_Window:
	def __int__(self, main_game_window_obj, main_game_window_size):
		self.main_game_window_object = main_game_window_obj
		self.main_game_window_size = main_game_window_size
		self.window_width_height = (150, 50)
		self.window_XY_start_coordinates = (self.main_game_window_size[0] // 2, 
											self.main_game_window_size[1] - self.window_width_height[1])
		self.window_color_in_RGB = (10, 10, 10)
		self.input_area_inactive_color_in_RGB = (150, 150, 150)
		self.input_area_active_color_in_RGB = (120,120, 120)
		self.input_digits_color_in_RGB = (10, 200, 100)
		self.window_description_title = 'Enter your answer:'
		self.digit_buttons_pygame_codes = (pg.K_0, pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6,
										   pg.K_7, pg.K_8, pg.K_9, pg.K_KP0, pg.K_KP1, pg.K_KP2, pg.K_KP3,
										   pg.K_KP4, pg.K_KP5, pg.K_KP6, pg.K_KP7, pg.K_KP8, pg.K_KP9)
		self.backspace_button_code = pg.K_BACKSPACE
		self.user_input_text = ''


	def get_input_window_Rect_obj(self):
		window_Rect = pg.Rect(self.window_XY_start_coordinates[0], window_XY_start_coordinates[1], 200, 70)

		return window_Rect

	def display_input_window_descrition_title(self):
		font_of_text_in_window = pygame.font.Font('freesansbold.ttf', 20)
		window_title_XY_center = (self.window_XY_start_coordinates[0] + 30 , self.window_XY_start_coordinates[1] + 10)

		window_Rect = self.get_input_window_Rect_obj()
		window_title = font_of_text_in_window.render(self.window_description_title, True, (150, 200, 100), (100, 100, 100))
		window_title_Rect = window_title.get_rect()
		window_title_Rect.center = window_title_XY_center
		self.main_game_window_object.blit(window_title, window_title_Rect)

	def display_input_area_for_answer(self):
		input_Rect = pg.Rect(self.window_XY_start_coordinates[0] + 50, 
							 self.window_XY_start_coordinates[1] + 10, 100, 50)

	def digit_button_pressed_on_keyboard(self, user_event):
		user_button = user_event.key
		if user_button in self.digit_buttons_pygame_codes:
			return True
		else:
			return False

	def add_digit_to_user_input_string(self, user_event):
		if self.digit_button_pressed_on_keyboard(user_event):
			self.user_input_text += user_event.unicode

	def backspace_button_pressed_on_keyboard(self, user_event):
		user_button = user_event.key
		if user_button == self.backspace_button_code:
			return True
		else:
			return False

	def remove_last_symbol_from_user_input_string_when_backspace_pressed(self, user_event):
		if self.backspace_button_pressed_on_keyboard(user_event):
			self.user_input_text = self.user_input_text[:-1]

	def user_input_string_more_than_need(self):
		# method for restriction for big user input string.
		# enough will be 6 symbols. for now.