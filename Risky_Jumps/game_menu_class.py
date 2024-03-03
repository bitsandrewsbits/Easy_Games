# class game menu - for create window
import pygame
import menu_button_class as game_btn

class Game_Menu:
	def __init__(self, pygame_window_object = 'pygame_obj', game_display_size = (10, 10), window_title = "Test", 
					menu_window_size = (10, 10), window_color = 'black', button_names = ['Test names']):
		self.main_window_pygame_object = pygame_window_object
		self.main_window_size = game_display_size
		self.window_title = window_title
		self.menu_window_width_height = menu_window_size
		self.window_color = window_color
		self.button_names = button_names
		self.menu_buttons = self.get_buttons()

	def menu_displaying(self):
		font_of_text_in_window = pygame.font.Font('freesansbold.ttf', 20)
		window_parameters = self.get_menu_size_parameters()
		window_title_XY_center = (window_parameters[0] * 1.5, window_parameters[1] + 20)

		button_pressed = False
		while not button_pressed:
			window_Rect = pygame.draw.rect(self.main_window_pygame_object, (100, 200, 90), window_parameters)
			window_title = font_of_text_in_window.render(self.window_title, True, (150, 200, 100), (100, 100, 100))
			window_title_Rect = window_title.get_rect()
			window_title_Rect.center = window_title_XY_center
			self.main_window_pygame_object.blit(window_title, window_title_Rect)

			for i in range(len(self.menu_buttons)):
				self.menu_buttons[i].show_game_button()

			pressed_menu_button = self.menu_button_pressed()
			if pressed_menu_button[1] == True:
				button_pressed = True

			pygame.display.update()
	
		return pressed_menu_button

	def menu_button_pressed(self):
		for game_event in pygame.event.get():
			if game_event.type == pygame.MOUSEBUTTONDOWN:
				for button in self.menu_buttons:
					button_name_pressed_status = button.button_pressed()
					print(button_name_pressed_status)
					if button_name_pressed_status[1] == True:
						print('Exitting from menu...')
						return button_name_pressed_status

		return (False, False)

	def get_menu_size_parameters(self):
		return (self.main_window_size[0] // 3, 50, self.menu_window_width_height[0], self.menu_window_width_height[1])

	def get_button_names(self):
		return self.button_names

	def get_buttons(self):
		button_size = (100, 50)
		print('Creating buttons for menu...')
		menu_parameters = self.get_menu_size_parameters()
		first_XY_button_coordinates = [menu_parameters[0] + 20, menu_parameters[1] + 50]
		
		max_button_amount_per_menu_width = self.menu_window_width_height[0] // 150
		print('Max amount of buttons per menu width:', max_button_amount_per_menu_width)

		XY_buttons_coordinates = []
		for i in range(len(self.button_names)):
			if i % max_button_amount_per_menu_width == 0 and i != 0:
				XY_buttons_coordinates.append([first_XY_button_coordinates[0], 
											   first_XY_button_coordinates[1] + (button_size[1] + 20) * (i - 1)])
			else:
				XY_buttons_coordinates.append([first_XY_button_coordinates[0] + (button_size[0] + 50) * i, 
											   first_XY_button_coordinates[1]])

		print(XY_buttons_coordinates)
		menu_buttons = []
		for i in range(len(self.button_names)):
			menu_buttons.append(game_btn.Button(self.main_window_pygame_object, self.main_window_size, button_size, 
							XY_buttons_coordinates[i], (10, 20, 10), (10, 250, 10), self.button_names[i]))

		print('FINISH of creation menu buttons...')
		print([btn.get_button_parameters() for btn in menu_buttons])
		return menu_buttons