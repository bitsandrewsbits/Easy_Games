# class Button - for game menu button
import pygame

class Button:
	def __init__(self, game_main_window_object,  game_display_size = (300, 100), button_width_height = (20, 10), 
				button_XY_coordinates = [0, 0], button_RGB_color = (0, 50, 100), button_text_RGB_color = (150, 200, 50), 
				button_name = 'Test'):
		self.main_game_window = game_main_window_object
		self.game_display_size = game_display_size
		self.button_size = button_width_height
		self.button_XY_coordinates = button_XY_coordinates
		self.button_color = button_RGB_color
		self.button_text_color = button_text_RGB_color
		self.button_name = button_name

	def show_game_button(self):
		button_text_font = pygame.font.Font('freesansbold.ttf', 15)
		button_parameters = self.get_button_parameters()
		button_text_XY_center = (button_parameters[0] + 50, button_parameters[1] + 20)
		
		button_Rect = pygame.draw.rect(self.main_game_window, self.button_color, button_parameters)
		button_text = button_text_font.render(self.button_name, True, self.button_text_color, self.button_color)
		button_text_Rect = button_text.get_rect()
		button_text_Rect.center = button_text_XY_center
		self.main_game_window.blit(button_text, button_text_Rect)

	def button_pressed(self):
		if self.get_mouse_XY_coordinate()[0] >= self.get_button_parameters()[0] and \
		        self.get_mouse_XY_coordinate()[0] <= self.get_button_parameters()[0] + self.button_size[0] and \
		        self.get_mouse_XY_coordinate()[1] >= self.get_button_parameters()[1] and \
		   		self.get_mouse_XY_coordinate()[1] <= self.get_button_parameters()[1] + self.button_size[1]:
		   	return (self.button_name, True)
		else:
			return (self.button_name, False)

	def get_mouse_XY_coordinate(self):
		return pygame.mouse.get_pos()

	def get_button_parameters(self):
		return (self.button_XY_coordinates[0], self.button_XY_coordinates[1], self.button_size[0], self.button_size[1])

	def set_button_XY_coordinates(self, X_coordinate = 0, Y_coordinate = 0):
		self.button_XY_coordinates[0] = X_coordinate
		self.button_XY_coordinates[1] = Y_coordinate

	def get_button_name(self):
		return self.button_name
