import pygame
import random
window_size = (700, 600)

class ArithBlock:
    def __init__(self, width = 100, height = 50, num1 = 1, num2 = 1,
                 math_operation = "*", block_color = (100, 100, 100),
                 current_left_position = 0,
                 current_top_position = 0):  # color in RGB-format
        self.width = width
        self.height = height
        self.num1 = num1
        self.num2 = num2
        self.math_operation = math_operation
        self.current_left_position = current_left_position
        self.current_top_position = current_top_position
        self.block_color = block_color

    def calc_answer(self):
        if self.math_operation == "*":
            return self.num1 * self.num2
        elif self.math_operation == "+":
            return self.num1 + self.num2

    def create_block(self):
        self.current_left_position = random.randint(0, window_size[0] - 100)
        self.current_top_position = 0
        return pygame.Rect(self.current_left_position, self.current_top_position,
                           self.width, self.height)















