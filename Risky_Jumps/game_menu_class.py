# class game menu - for create window
import menu_button_class as button

class Game_Menu:
	def __init__(self, pygame_window_object = 'pygame_obj', game_display_size = (10, 10), window_title = "Test", 
					window_size = (10, 10), window_color = 'black', button_amount = 1):
		self.main_window_pygame_object = pygame_window_object
		self.menu_window_size = game_display_size
		self.window_title = window_title
		self.window_width_height = window_size
		self.window_color = window_color
		self.button_amount = button_amount
		self.buttons = self.get_buttons(self.button_amount)

	def menu_window(self):
		font_of_text_in_window = pygame.font.Font('freesansbold.ttf', 20)
		window_parameters = (self.game_display_size[0] // 3, 50, self.window_width_height[0], self.window_width_height[1])
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
						# button.display() # realization in Button class(in future)
						if self.button_pressed() == True:
							return True

			pygame.display.update()

	def get_buttons(self):
		buttons = []
		for _ in range(button_amount):
			# buttons.append(button.Button())
		return buttons