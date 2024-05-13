# class for create input menu for answering math examples in arithmetic block

class Input_Answer_Window:
	def __int__(self, main_game_window_obj, main_game_window_size):
		self.main_game_window_object = main_game_window_obj
		self.main_game_window_size = main_game_window_size
		self.window_width_height = (150, 50)
		self.window_XY_start_coordinates = (self.main_game_window_size[0] // 2, 
											self.main_game_window_size[1] - self.window_width_height[1])
		self.window_color_in_RGB = (10, 10, 10)
		self.input_area_color_in_RGB = (50, 50, 50)
		self.input_digits_color_in_RGB = (10, 200, 100)