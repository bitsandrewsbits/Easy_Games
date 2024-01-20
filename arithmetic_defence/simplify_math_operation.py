# In this file, I will create, a simplifier button.
# Simplifier button - is a button, when you click on this button,
# it simplifies the most bottom example, only one time.
# What it means?
# If math operation - '+' - it just gets right answer;
# For example: Block |18 + 57| => press button => Block |75|

# If math operation - '*' - it converts to '+' operation:
# For instance: Block |48 * 29| => pressing button Simplifier =>
# => converting to |48 * 9 + 48 * 20| or simpler Block |432 + 960|
# For not misusing this feature in this game, only every 500 score points you earn 1 using of this button
# Maybe, it will be hard to resolving, but when you solve examples with answer more than 1000, you will have
# 1000 // 500 = 2 using of this feature! It is only first version of this feature and ability in this game.
# ===============================================================

import pygame
# from game import screen

window_size = (700, 600)

# executing simplifying operation - simplifying the most bottom block(first concept of this ability)
# block_list arg - (block_obj, rect_obj)
def example_simplifying(block_obj):
    if block_obj.math_operation == '+':
        block_obj.num1 = block_obj.num1 + block_obj.num2
        block_obj.num2 = 0
    elif block_obj.math_operation == '*':
        # temporary saving original numbers in block
        num1 = block_obj.num1
        num2 = block_obj.num2
        # updating block numbers
        if len(str(num1)) == 2 and len(str(num2)) == 2:
            block_obj.num1 = num1 * int(str(num2)[-1])
            block_obj.num2 = num1 * int(str(num2)[0]) * 10
        else:
            block_obj.num1 = num1 * num2
            block_obj.num2 = 0
        block_obj.math_operation = '+'

# func(screen_surface, ability_amount)
# screen_surface - pygame Surface object
# ability_amount - amount of simplifying
def simplifier_button(screen_surface, ability_amount: int = 1):
    # rect of button
    simp_rect = pygame.Rect(window_size[0] - 150, window_size[1] - 50, 100, 40)
    # inactive color of button
    inactive_butt_color = (40, 10, 50)
    # active color of button
    active_butt_color = (10, 10, 10)
    button_text = 'Simplify'
    text_butt_color = (250, 40, 0)
    # color of simplifying ability amount
    amount_text_color = (250, 220, 50)
    font = pygame.font.Font("freesansbold.ttf", 15)

    mouse_position = pygame.mouse.get_pos()  # (X, Y) coordinates of mouse on window

    # if mouse hovering on button rectangle - changing button color
    # function return True - if button is pressed
    # return False - if is not pressed
    if mouse_position[0] >= simp_rect.left and \
            mouse_position[0] <= simp_rect.left + simp_rect.width and \
            mouse_position[1] >= simp_rect.top and \
            mouse_position[1] <= simp_rect.top + simp_rect.height:
        pygame.draw.rect(screen_surface, active_butt_color, simp_rect)
        simpl_text_rect = font.render(button_text, True, text_butt_color, active_butt_color)
        screen_surface.blit(simpl_text_rect, (simp_rect.left + 10, simp_rect.top + 10))

        # displaying amount of simplifying ability
        ability_amount_text = font.render(f"x{str(ability_amount)}", True, amount_text_color, active_butt_color)
        screen_surface.blit(ability_amount_text, (simp_rect.left + 80, simp_rect.top + 10))
        return True
    else:
        # Simplifying button - inactive
        pygame.draw.rect(screen_surface, inactive_butt_color, simp_rect)
        simpl_text_button = font.render(button_text, True, text_butt_color, inactive_butt_color)
        # text on button
        screen_surface.blit(simpl_text_button, (simp_rect.left + 10, simp_rect.top + 10))

        # displaying amount of simplifying ability
        ability_amount_text = font.render(f"x{str(ability_amount)}", True, amount_text_color, inactive_butt_color)
        screen_surface.blit(ability_amount_text, (simp_rect.left + 80, simp_rect.top + 10))
        return False

# To Do: integrate into main game file.







