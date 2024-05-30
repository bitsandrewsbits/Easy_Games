# class game menu - for create window
import pygame
import menu_button_class as game_btn

class Game_Menu:
	def __init__(self, pygame_window_object = 'pygame_obj', game_display_size = (10, 10), menu_title = "Test", 
					menu_window_size = (10, 10), window_color = 'black', button_names = ['Test names'],
					static_output_fields = {}, menu_annotation = ''):
		self.main_window_pygame_object = pygame_window_object
		self.main_window_size = game_display_size
		self.menu_title = menu_title
		self.menu_window_width_height = menu_window_size
		self.window_color = window_color
		self.button_names = button_names
		self.menu_buttons = self.get_buttons()
		self.output_info_fields = static_output_fields
		self.menu_annotation = menu_annotation
		self.menu_annotation_font = 20
		self.index_for_row_height_when_show_annotation_in_menu = 1
		self.menu_annotation_by_strings = self.get_right_words_list_per_string_for_menu_size()

	def menu_displaying(self):
		menu_parameters = self.get_menu_size_parameters()
		menu_title_XY_center = (menu_parameters[0] + menu_parameters[2] // 2, menu_parameters[1] + 20)

		if not self.annotation_menu_empty():
			self.set_new_Y_coordinate_for_menu_buttons()

		if not self.menu_title_empty():
			self.set_menu_button_Y_coordinate_as_shifting_for_menu_title()
		
		button_pressed = False
		while not button_pressed:

			window_Rect = pygame.draw.rect(self.main_window_pygame_object, (100, 200, 90), menu_parameters)
			self.show_menu_annotation()
			self.show_menu_title(menu_title_XY_center)

			self.output_information_fields_from_game()
			

			for i in range(len(self.menu_buttons)):
				self.menu_buttons[i].show_game_button()

			pressed_menu_button = self.menu_button_pressed()
			if pressed_menu_button[1] == True:
				button_pressed = True

			pygame.display.update()
	
		return pressed_menu_button

	def show_menu_title(self, menu_title_XY_center):
		font_of_text_in_menu = pygame.font.Font('freesansbold.ttf', 20)
		menu_title = font_of_text_in_menu.render(self.menu_title, True, (150, 200, 100), (10, 10, 10))
		menu_title_Rect = menu_title.get_rect()
		menu_title_Rect.center = menu_title_XY_center
		self.main_window_pygame_object.blit(menu_title, menu_title_Rect)

	def menu_title_empty(self):
		if self.menu_title == '':
			return True
		else:
			return False

	def annotation_menu_empty(self):
		if self.menu_annotation == '':
			return True
		else:
			return False

	def set_menu_button_Y_coordinate_as_shifting_for_menu_title(self):
		for button in self.menu_buttons:
			final_Y_coordinate_for_menu_button = button.button_XY_coordinates[1] + 25
			button.set_button_Y_coordinate(final_Y_coordinate_for_menu_button)

	def set_new_Y_coordinate_for_menu_buttons(self):
		new_Y_button_coordinate = self.get_menu_size_parameters()[1] + \
		self.get_additional_value_of_Y_coordinate_for_menu_buttons()
		for button in self.menu_buttons:
			button.set_button_Y_coordinate(new_Y_button_coordinate)

	def get_additional_value_of_Y_coordinate_for_menu_buttons(self):
		return self.index_for_row_height_when_show_annotation_in_menu * self.menu_annotation_font

	def show_menu_annotation(self):
		index_for_new_row_when_show_annotation_in_menu = 0
		for annotation_string in self.menu_annotation_by_strings:
			temp_rendered_string = self.get_rectangle_object_of_certain_annotation_words(annotation_string)
			temp_string_Rect = temp_rendered_string.get_rect()
			temp_string_Rect.center = (self.get_menu_size_parameters()[0] * 4, 
				self.get_menu_size_parameters()[1] + temp_string_Rect.height * \
				index_for_new_row_when_show_annotation_in_menu + 40)
			self.main_window_pygame_object.blit(temp_rendered_string, temp_string_Rect)
			
			index_for_new_row_when_show_annotation_in_menu += 1

	def get_right_words_list_per_string_for_menu_size(self):
		result_annotation_strings = []

		# algorigthm for defining right words string per line for menu annotation
		annotation_words = self.get_words_from_menu_annotation()
		temp_words_string = ''

		first_index_of_word_for_new_annotation_string = 0
		for i in range(1, len(annotation_words) + 1):
			part_of_annotation_words = ' '.join(annotation_words[first_index_of_word_for_new_annotation_string:i])
			Rect_obj_of_part_annotation_words = self.get_rectangle_object_of_certain_annotation_words(part_of_annotation_words).get_rect()
			if Rect_obj_of_part_annotation_words.width < self.menu_window_width_height[0]:
				temp_words_string = part_of_annotation_words
			else:
				part_of_annotation_words = ' '.join(annotation_words[first_index_of_word_for_new_annotation_string:i - 1])
				# print('Annotation string for menu:', temp_words_string)
				result_annotation_strings.append(temp_words_string)
				first_index_of_word_for_new_annotation_string = i - 1
				self.index_for_row_height_when_show_annotation_in_menu += 1

			if i == len(annotation_words):
				result_annotation_strings.append(temp_words_string)
				self.index_for_row_height_when_show_annotation_in_menu += 1


		print(result_annotation_strings)
		return result_annotation_strings

	def get_rectangle_object_of_certain_annotation_words(self, words_phrase = ''):
		pygame.init()
		font_of_annotation_text = pygame.font.Font('freesansbold.ttf', self.menu_annotation_font)

		rendered_word_object = font_of_annotation_text.render(words_phrase, True, (150, 200, 100), (10, 10, 10))

		return rendered_word_object

	def get_words_from_menu_annotation(self):
		return self.menu_annotation.split(' ')

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
		return (self.main_window_size[0] // 2 - self.menu_window_width_height[0] // 2, 50, 
				self.menu_window_width_height[0], self.menu_window_width_height[1])

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

	def output_information_fields_from_game(self):
		window_menu_parameters = self.get_menu_size_parameters()
		window_menu_start_X_coordinate = window_menu_parameters[0]
		window_menu_start_Y_coordinate = window_menu_parameters[1]

		output_info_field_block_width_height = (150, 45)
		font_of_text_in_output_info_block = pygame.font.Font('freesansbold.ttf', 15)
		
		
		temp_i = 0
		for field_name in self.output_info_fields:
			output_info_field_block_coordinates = [
				window_menu_start_X_coordinate + (output_info_field_block_width_height[0] + 15) * temp_i + 10, 
				window_menu_start_Y_coordinate + self.menu_window_width_height[1] // 2 + 30,
				output_info_field_block_width_height[0], output_info_field_block_width_height[1]]
			
			pygame.draw.rect(self.main_window_pygame_object, (0, 0, 0), output_info_field_block_coordinates)

			output_info_field_Block_title = font_of_text_in_output_info_block.render(field_name, True, 
																			(100, 250, 150), (0, 0, 0))
			output_info_field_Block_Title_Rect = output_info_field_Block_title.get_rect()
			output_info_field_Block_Title_Rect.center = (
				        output_info_field_block_coordinates[0] + output_info_field_block_width_height[0] // 2,
				    	output_info_field_block_coordinates[1] + 15)
			self.main_window_pygame_object.blit(output_info_field_Block_title, output_info_field_Block_Title_Rect)
			
			
			output_info_field_value = font_of_text_in_output_info_block.render(str(self.output_info_fields[field_name]), 
																			True, (150, 200, 100), (0, 0, 0))
			output_info_field_value_Rect = output_info_field_value.get_rect()
			output_info_field_value_Rect.center = (
						output_info_field_block_coordinates[0] + output_info_field_block_width_height[0] // 2,
						output_info_field_block_coordinates[1] + 35)

			self.main_window_pygame_object.blit(output_info_field_value, output_info_field_value_Rect)

			temp_i += 1