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
