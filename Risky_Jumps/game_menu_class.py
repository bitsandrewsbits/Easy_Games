# class game menu - for create window
import menu_button_class as button

class Game_Menu:
	def __init__(self, pygame_window_object = 'pygame_obj', game_display_size = (10, 10), window_title = "Test", 
					window_size = (10, 10), window_color = 'black', button_names = ['Test names']):
		self.main_window_pygame_object = pygame_window_object
		self.menu_window_size = game_display_size
		self.window_title = window_title
		self.window_width_height = window_size
		self.window_color = window_color
		self.button_names = button_names
		self.menu_buttons = self.get_buttons(len(self.button_names))

	def menu_displaying(self):
		font_of_text_in_window = pygame.font.Font('freesansbold.ttf', 20)
		window_parameters = self.get_menu_size_parameters()
		window_title_XY_center = (window_parameters[0] * 1.5, window_parameters[1] + 20)

		while True:
			window_Rect = pygame.draw.rect(main_pygame_window_object, (100, 200, 90), window_parameters)
			window_title = font_of_text_in_window.render(self.window_title, True, (150, 200, 100), (100, 100, 100))
			window_title_Rect = window_title.get_rect()
			window_title_Rect.center = window_title_XY_center
			self.main_window_pygame_object.blit(window_title, window_title_Rect)

			for game_event in pygame.event.get():
				if game_event.type == pygame.MOUSEBUTTONDOWN:
					for button in menu_buttons:
						button.show_game_button()
						if button.button_pressed() == True:
							return True

			pygame.display.update()

	def get_menu_size_parameters(self):
		return (self.game_display_size[0] // 3, 50, self.window_width_height[0], self.window_width_height[1])

	def get_buttons(self):
		menu_parameters = self.get_menu_size_parameters()
		XY_button_coordinates = [self.menu_parameters[0] + 20, self.menu_parameters[1] + 50]
		buttons = []
		# TODO: define by menu size - what amount of buttons can contain game menu per row(automatically)
		additional_XY_coordinate = (0, 0)
		for i in range(len(self.button_names)):
			button = button.Button(self.main_window_pygame_object, self.game_display_size, (100, 50), 
										XY_button_coordinates, (10, 20, 10), (10, 250, 10), self.button_names[i])
			button_parameters = button.get_button_parameters()
			button.set_button_XY_coordinates(button_parameters[0] + additional_XY_coordinate[0],
											 button_parameters[1] + additional_XY_coordinate[1])
			buttons.append()
			additional_XY_coordinate = button_parameters[2]
		return buttons