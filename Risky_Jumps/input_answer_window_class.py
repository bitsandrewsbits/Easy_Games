# class for create input menu for answering math examples in arithmetic block
import pygame as pg

class Input_Answer_Window:
	def __init__(self, main_game_window_obj, main_game_window_size):
		self.main_game_window_object = main_game_window_obj
		self.main_game_window_size = main_game_window_size
		self.window_width_height = (self.main_game_window_size[0] // 2.5, 50)
		self.window_XY_start_coordinates = (self.main_game_window_size[0] // 4, 
											self.main_game_window_size[1] - self.window_width_height[1])
		self.window_color_in_RGB = (10, 130, 100)
		self.input_area_color_in_RGB = (30, 30, 30)
		self.input_digits_color_in_RGB = (10, 200, 100)
		self.window_description_title = 'Enter your answer:'
		self.digit_buttons_pygame_codes = (pg.K_0, pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6,
										   pg.K_7, pg.K_8, pg.K_9, pg.K_KP0, pg.K_KP1, pg.K_KP2, pg.K_KP3,
										   pg.K_KP4, pg.K_KP5, pg.K_KP6, pg.K_KP7, pg.K_KP8, pg.K_KP9)
		self.backspace_button_code = pg.K_BACKSPACE
		self.enter_button_code = pg.K_RETURN
		self.user_input_text = ''
		self.max_length_of_user_input_string = 6

	def display_entire_input_window(self):
		pg.draw.rect(self.main_game_window_object, self.window_color_in_RGB, self.get_input_window_Rect_obj())
		pg.draw.rect(self.main_game_window_object, self.input_area_color_in_RGB, self.get_input_area_for_answer())
		
		input_digits_font = pg.font.Font('freesansbold.ttf', 20)
		input_text_area = input_digits_font.render(self.user_input_text, True, self.input_digits_color_in_RGB)
		start_X_coordinate_for_user_input = self.get_input_area_for_answer().x + 5
		start_Y_coordinate_for_user_input = self.get_input_area_for_answer().y + 15
		input_text_area_center = (start_X_coordinate_for_user_input, start_Y_coordinate_for_user_input)
		self.main_game_window_object.blit(input_text_area, input_text_area_center)

		self.display_input_window_descrition_title()

	def implement_user_input(self, user_event):
		self.add_digit_to_user_input_string(user_event)
		self.remove_last_symbol_from_user_input_string_when_backspace_pressed(user_event)

	def get_input_window_Rect_obj(self):
		window_Rect = pg.Rect(self.window_XY_start_coordinates[0], self.window_XY_start_coordinates[1], 
							self.window_width_height[0], self.window_width_height[1])

		return window_Rect

	def display_input_window_descrition_title(self):
		font_of_text_in_window = pg.font.Font('freesansbold.ttf', 20)
		window_title_XY_center = (self.window_XY_start_coordinates[0] * 1.5 , self.window_XY_start_coordinates[1] + 25)

		window_Rect = self.get_input_window_Rect_obj()
		window_title = font_of_text_in_window.render(self.window_description_title, True, (150, 200, 100), (50, 50, 50))
		window_title_Rect = window_title.get_rect()
		window_title_Rect.center = window_title_XY_center
		self.main_game_window_object.blit(window_title, window_title_Rect)

	def get_input_area_for_answer(self):
		input_rect = pg.Rect(self.window_XY_start_coordinates[0] * 2, 
							 self.window_XY_start_coordinates[1], 100, 50)
		return input_rect

	def digit_button_pressed_on_keyboard(self, user_event):
		user_button = user_event.key
		if user_button in self.digit_buttons_pygame_codes:
			return True
		else:
			return False

	def add_digit_to_user_input_string(self, user_event):
		if self.digit_button_pressed_on_keyboard(user_event):
			self.user_input_text += user_event.unicode
			if self.user_input_string_more_than_need():
				self.user_input_text = self.user_input_text[:-1]

	def backspace_button_pressed_on_keyboard(self, user_event):
		user_button = user_event.key
		if user_button == self.backspace_button_code:
			return True
		else:
			return False

	def remove_last_symbol_from_user_input_string_when_backspace_pressed(self, user_event):
		if self.backspace_button_pressed_on_keyboard(user_event):
			self.user_input_text = self.user_input_text[:-1]

	def get_user_input_answer_as_number(self):
		if self.user_input_text == '':
			return 0
		else:
			return int(self.user_input_text)

	def enter_button_pressed(self, user_event):
		user_button = user_event.key
		if user_button == self.enter_button_code:
			return True 
		else:
			return False

	def user_input_string_more_than_need(self):
		if len(self.user_input_text) > self.max_length_of_user_input_string:
			return True
		else:
			return False
