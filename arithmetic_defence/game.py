import pygame
import random
import arith_blocks as blck
import simplify_math_operation as simpl


pygame.init()
clock = pygame.time.Clock()
window_size = (700, 600)
screen = pygame.display.set_mode(window_size) # game screen size
done = False

def block_dropping(rect: pygame.Rect, block_obj: blck.ArithBlock):
    # print("Block rect: ", rect)
    pygame.draw.rect(screen, block_obj.block_color, rect)
    block_text(block_obj, rect)

# defence zone:
def defence_zone():
    pygame.draw.rect(screen, (200, 160, 100), (0, window_size[1] - 60, window_size[0], window_size[1]))
    return

def block_text(block_obj: blck.ArithBlock, rect_obj: pygame.Rect):
    number_1 = block_obj.num1
    number_2 = block_obj.num2
    math_oper = block_obj.math_operation
    # adding text to dropping block
    font = pygame.font.Font("freesansbold.ttf", 20)
    block_text = font.render(f'{number_1} {math_oper} {number_2}', True, (255, 0, 0), (0, 50, 0))
    textRect = block_text.get_rect()
    textRect.left = rect_obj.left
    textRect.top = rect_obj.top
    # blit(text_block, (x, y of current position of rect on window))
    screen.blit(block_text, (rect_obj.left + textRect.width // 3,
                             rect_obj.top + textRect.height // 1.5))

def health_field(health_count = 100, game_blocks = [], scores = 0):
    health_text = ''
    health_block = pygame.Rect(60, window_size[1] - 50, 70, 30)
    font = pygame.font.Font("freesansbold.ttf", 20)

    if health_count >= 70:
        health_text = font.render(f'{health_count}', True, (0, 255, 0), (0, 0, 0))  # high HP
    elif health_count < 70 and health_count >= 30:
        health_text = font.render(f'{health_count}', True, (255, 255, 0), (0, 0, 0)) # medium HP
    elif health_count < 30 and health_count > 0:
        health_text = font.render(f'{health_count}', True, (255, 0, 0), (0, 0, 0))   # low HP!
    else:
        # if health points == 0 or < 0 - return False
        return False

    pygame.draw.rect(screen, (0, 0, 0), health_block)  #main block for health points
    screen.blit(health_text, (health_block.left + 20, health_block.top + 5))
    return True

def game_over_process(blocks, score):
    new_game = False
    one_update_flag = True
    score_list = 0
    print("Game Over Process...")
    font_GO = pygame.font.Font("freesansbold.ttf", 20)
    text1 = 'Game Over.'
    text2 = 'Press Enter to New Game'
    score_text = f"Your Score: {score}"

    # deleting all blocks in game
    while len(blocks) != 0:
        blocks.pop(-1)

    while not new_game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    new_game = True
                    print('NEW GAME!')
            if event.type == pygame.MOUSEBUTTONDOWN and press_exit_button:
                print("Exiting from game...")
                pygame.quit()

        text1_block = font_GO.render(text1, True, (255, 200, 150), (0, 0, 0))
        text2_block = font_GO.render(text2, True, (255, 200, 150), (0, 0, 0))
        score_block = font_GO.render(score_text, True, (255, 200, 150), (0, 0, 0))
        game_over_rect = pygame.Rect(20, window_size[1] // 4, 300, 250)

        pygame.draw.rect(screen, (50, 150, 200), game_over_rect)
        screen.blit(text1_block, (30, window_size[1] // 3))
        screen.blit(text2_block, (30, window_size[1] // 3 + 40))
        screen.blit(score_block, (30, window_size[1] // 3.5))

        #display exit button
        exit_butt_color_inactive = (140, 200, 20)
        exit_butt_color_active = (0, 0, 0)
        text_exit_butt_color = (50, 0, 200)
        exit_button_rect = pygame.Rect(game_over_rect.width // 3, game_over_rect.height + 50, 100, 40)
        press_exit_button = menu_buttons(exit_butt_color_inactive, exit_butt_color_active,
                                         text_exit_butt_color, 'Exit', exit_button_rect, 30)

        # ===displaying score table=== #
        #adding current score
        if one_update_flag:
            score_list = update_scores_table(score)
            one_update_flag = False
        text_score_table = 'Most High Scores:'
        # display table block
        score_table_block = pygame.Rect(window_size[0] // 2, 30, 300, 500)
        pygame.draw.rect(screen, (50, 50, 50), score_table_block)

        #display title of score table
        score_title_rect = font_GO.render(text_score_table, True, (255, 240, 150), (0, 0, 0))
        screen.blit(score_title_rect, (window_size[0] // 2 + 20, 40))

        # display five most high score
        top_score_position = 70
        for score in score_list:
            score_rect = font_GO.render(f'Score: {score}', True, (50, 250, 30), (0, 0, 0))
            screen.blit(score_rect, (window_size[0] // 2 + 20, top_score_position))
            top_score_position += 30

        # game screen updating(!)
        pygame.display.flip()


# input arg - list of blck.ArithBlock that on the game and already dropping
def health_reducing(blocks: list, health = 100):
    defence_line = window_size[1] - 60 # points where defence zone starts and health points will reduce!
    for i in range(len(blocks)):
        # when block crossing defence zone - it reduces health point of defence zone!
        if blocks[i][1].top > defence_line:
            deleted_block = blocks.pop(i)  # return block object that will be deleted!
            # print("Answer =", deleted_block[0].calc_answer())
            return health - deleted_block[0].calc_answer() // 100
    return health

def health_adding(health_amount = 0, scores = 0):
    health_amount += scores // 10
    return health_amount

def health_title():
    font = pygame.font.Font("freesansbold.ttf", 15)
    text = 'Health'
    text_block = font.render(text, True, (255, 200, 150), (0, 0, 0))
    screen.blit(text_block, (10, window_size[1] - 40))

def input_answer_title():
    font = pygame.font.Font("freesansbold.ttf", 15)
    text = 'Your Answer'
    text_block = font.render(text, True, (255, 200, 150), (0, 0, 0))
    screen.blit(text_block, (150, window_size[1] - 40))

# func for showing input field for answer inputting
def input_field(user_text = '0'):
    font = pygame.font.Font("freesansbold.ttf", 20)
    field_rect = pygame.Rect(245, window_size[1] - 50, 70, 30)

    pygame.draw.rect(screen, (10, 10, 10), field_rect)  # input answer field rect
    text_rect = font.render(user_text, True, (245, 114, 20))  # surface object

    # render at position stated in arguments
    screen.blit(text_rect, (245, field_rect.top + 5))

    # set width of textfield so that text cannot get outside of user's text input
    field_rect.width = max(field_rect.width, text_rect.get_width() + 10)

def score_title():
    font = pygame.font.Font("freesansbold.ttf", 15)
    text = 'Score'
    text_block = font.render(text, True, (255, 200, 150), (0, 0, 0))
    screen.blit(text_block, (350, window_size[1] - 40))

def score_field(scores = 0):
    score_block = pygame.Rect(395, window_size[1] - 50, 100, 30)
    font = pygame.font.Font("freesansbold.ttf", 20)
    score_text = font.render(f'{scores}', True, (40, 240, 100), (0, 0, 0))

    pygame.draw.rect(screen, (0, 0, 0), score_block)  # main block for health points
    screen.blit(score_text, (score_block.left + 10, score_block.top + 5))

    return scores

def increase_complexity(time_cnt = 0, fps = 1, speed_drop_blk = 30):
    if speed_drop_blk <= 5:
        return (15, 7)
    if time_cnt % 150 == 0 and time_cnt != 0:
        fps += 1
        speed_drop_blk -= 1
        return (fps, speed_drop_blk)
    # if less than 100 - just return current values
    return (fps, speed_drop_blk)


# creating and updating file with the most high scores
def update_scores_table(scores = 10):
    print("Updating Score Table...")
    scores_file = 'highest_scores.txt'
    # adding a new scores into file
    with open(scores_file, 'at') as w_scores:
        # reading all scores from file
        with open(scores_file, 'rt') as r_scores:
            # reading string and convert into integer value only score part(slice without Scores: )
            # and sorting values from max to min
            score_lst = sorted([int(score[7:]) for score in r_scores])[::-1]
            print(score_lst)
            if len(score_lst) > 5:
                high_scores = score_lst[:5]
                print(high_scores)
                # rewriting file with scores; only five the most high scores in the file!
                with open(scores_file, 'wt') as new_scores_f:
                    for score in high_scores:
                        new_scores_f.write(f'Scores: {score}\n')
                return high_scores

        # if amount scores less than 5, just return current scores as list
        w_scores.write(f'Scores: {scores}\n')
        if len(score_lst) == 0:
            return [scores]
        else:
            score_lst.append(scores)         # adding last score to table
            return sorted(score_lst)[::-1]   # reversed sorting for further right displaying

# button key for pygame.event
key_digits = (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
              pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9)
# buttons key of NumLock for pygame.event
key_NumLock_digits = (pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4,
                      pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9)


# func for display buttons on main window
def menu_buttons(button_color_inactive = (100, 40, 100), button_color_active = (0, 0, 0),
                 text_button_color = (0, 250, 40), button_text = 'Text',
                 rect_object = pygame.Rect(0, 0, 10, 10), text_X_position = 10):

    font = pygame.font.Font("freesansbold.ttf", 20)
    button_rect = rect_object

    mouse_position = pygame.mouse.get_pos()  # (X, Y) coordinates of mouse on window

    # if mouse hovering on button rectangle - changing button color
    # function return True - if button is pressed
    # return False - if is not pressed
    if mouse_position[0] >= button_rect.left and \
            mouse_position[0] <= button_rect.left + button_rect.width and \
            mouse_position[1] >= button_rect.top and \
            mouse_position[1] <= button_rect.top + button_rect.height:
        pygame.draw.rect(screen, button_color_active, button_rect)
        start_text_button = font.render(button_text, True, text_button_color, button_color_active)
        screen.blit(start_text_button, (button_rect.left + text_X_position, button_rect.top + 10))
        return True
    else:
        # Start game button - inactive
        pygame.draw.rect(screen, button_color_inactive, button_rect)
        start_text_button = font.render(button_text, True, text_button_color, button_color_inactive)
        # text on button
        screen.blit(start_text_button, (button_rect.left + 10, button_rect.top + 10))
        return False


# func of main window in the game
def menu_window():
    title_text = "Welcome to Arithmetic Dropping Blocks!"
    describe_text = ["You need to answer right so as to destroying dropping blocks.",
                    "If block cross the bottom interface line, that reducing your health!",
                    "If your health is 0 - Game Over!",
                    "Fortunately, when you destroying block your health often increasing.",
                    "A value of increasing health points depends on how difficult example",
                    "you are resolving.",
                    "Good Luck!"]

    font = pygame.font.Font("freesansbold.ttf", 20)

    # To Do:
    # 1) Button - Start New Game -> DONE
    # 2) Button - Exit -> DONE
    # 3) Add text to main menu with buttons -> DONE
    # 4) To integrate 1, 2, 3 into game process -> DONE

    main_menu_rect = pygame.Rect(50, 100, window_size[0] - 150, window_size[1] - 300)
    title_text_rect = font.render(title_text, True, (100, 250, 20), (0, 0, 0))

    #1) Button - Start New Game
    start_butt_color_inactive = (100, 40, 100)
    start_butt_color_active = (0, 0, 0)
    text_start_butt_color = (0, 250, 40)  # inactive color of rect of text
    start_button_rect = pygame.Rect(main_menu_rect.width // 3 + 30, main_menu_rect.height + 50, 180, 40)

    #2) Button - Exit from Game
    exit_butt_color_inactive = (50, 60, 20)
    exit_butt_color_active = (0, 0, 0)
    text_exit_butt_color = (50, 0, 200)
    exit_button_rect = pygame.Rect(main_menu_rect.width - 100, main_menu_rect.height + 50, 100, 40)

    # A main cycle of displaying game menu
    press_start_button = False
    start_game = False
    while not start_game:
        for event in pygame.event.get():
            # event.key == pressing button to Start New Game(1)
            if event.type == pygame.MOUSEBUTTONDOWN and press_start_button:
                print("Starting a new game...")
                start_game = True
            # if press Exit - then we are just exiting from game
            elif event.type == pygame.MOUSEBUTTONDOWN and press_exit_button:
                print("Exiting from game")
                pygame.quit()

        screen.fill((0, 0, 0))

        # a menu of game rect on game screen
        pygame.draw.rect(screen, (70, 70, 100), main_menu_rect)
        # display a title of game menu
        screen.blit(title_text_rect, (main_menu_rect.left + 50, main_menu_rect.top + 10))

        # displaying menu text
        next_line_height = main_menu_rect.top + 40
        font_describe_text = pygame.font.Font("freesansbold.ttf", 15)
        for line in describe_text:
            describe_game_rect = font_describe_text.render(line, True, (70, 70, 100), (100, 250, 100))
            screen.blit(describe_game_rect, (70, next_line_height))
            next_line_height += 40

        # display buttons on menu
        press_start_button = menu_buttons(start_butt_color_inactive, start_butt_color_active,
                                          text_start_butt_color, 'Start New Game', start_button_rect)

        press_exit_button = menu_buttons(exit_butt_color_inactive, exit_butt_color_active,
                                          text_exit_butt_color, 'Exit', exit_button_rect, 30)
        # updating screen
        pygame.display.flip()


# pause window with Continue, Exit buttons(for first version)
def pause_window():
    game_pause = True
    exit_flag = False
    continue_game = False
    font = pygame.font.Font("freesansbold.ttf", 20)

    # Pause window parameters
    pause_title_text = 'Game Pause'
    pause_window_rect = pygame.Rect(100, 100, 400, 200)
    title_text_rect = font.render(pause_title_text, True, (100, 250, 20), (0, 0, 0))

    # Exit button parameters
    exit_butt_color_inactive = (50, 60, 20)
    exit_butt_color_active = (0, 0, 0)
    text_exit_butt_color = (50, 0, 200)
    exit_button_rect = pygame.Rect(pause_window_rect.width - 50, pause_window_rect.height + 50, 100, 40)

    # Continue button parameters
    continue_butt_color_inactive = (50, 60, 20)
    continue_butt_color_active = (0, 0, 0)
    text_continue_butt_color = (50, 0, 200)
    continue_button_rect = pygame.Rect(130, pause_window_rect.height + 50, 200, 40)

    while game_pause:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and exit_flag:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and continue_game:
                print("Continue game...")
                game_pause = False

        screen.fill('black')

        # a menu of game rect on game screen
        pygame.draw.rect(screen, (50, 100, 100), pause_window_rect)
        # display a title of game menu
        screen.blit(title_text_rect, (pause_window_rect.left + 50, pause_window_rect.top + 10))

        exit_flag = menu_buttons(exit_butt_color_inactive, exit_butt_color_active, text_exit_butt_color,
                                 'Exit', exit_button_rect, 30)

        continue_game = menu_buttons(continue_butt_color_inactive, continue_butt_color_active,
                                     text_continue_butt_color, 'Continue Game', continue_button_rect, 30)

        pygame.display.flip()

def start_game(number1 = 0, number2 = 0, count_time = 0, health = 100, score = 0):
    math_operators = ["+", "*"]
    speed_level = 20
    game_blocks = []
    user_text = ''
    done = False
    simplify = False
    fps = 2
    simplify_ability_amount = 2
    # display game menu
    menu_window()
    # a main game process
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN and simplify:
                if simplify_ability_amount > 0:
                    simpl.example_simplifying(game_blocks[0][0])
                    simplify_ability_amount -= 1
            if event.type == pygame.KEYDOWN:
                # if Esc button is pressed - show pause window
                if event.key == pygame.K_ESCAPE:
                    print('Escape is pressed!')
                    pause_window()
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                if event.key in key_digits or event.key in key_NumLock_digits:
                    if len(user_text) < 5:
                        # adding symbols in Unicode format(aka just numbers or other symbols)
                        user_text += event.unicode
                if event.key == pygame.K_RETURN and len(user_text) != 0:
                    user_answer = int(user_text)
                    for i in range(len(game_blocks)):
                        if user_answer == game_blocks[i][0].calc_answer():
                            print("Answer correct! Block removed!")
                            score += user_answer
                            print(score)
                            health = health_adding(health, user_answer)
                            user_text = ''
                            # removing game block object from list
                            game_blocks.pop(i)
                            break
                        else:
                            user_text = ''

        screen.fill("black")

        fps = increase_complexity(count_time, fps, speed_level)[0]
        speed_level = increase_complexity(count_time, fps, speed_level)[1]

        if count_time % speed_level == 0:
            # print("Add New Block to Game!")
            print('dropping block speed:', speed_level)
            if count_time < 10:
                number1 = random.randint(1, 10)
                number2 = random.randint(1, 10)
            elif count_time >= 10 and count_time <= 30:
                number1 = random.randint(10, 30)
                number2 = random.randint(10, 30)
            elif count_time > 30:
                number1 = random.randint(30, 99)
                number2 = random.randint(30, 99)

        math_operator = math_operators[random.randint(0, 1)]
        # if health_field() return False - game is over!
        game_over_flag = health_field(health, game_blocks)
        if not game_over_flag:
            print("Game Over process starting...")
            # game_blocks - for cleaning list of blocks
            # scores - for displaying info about current score and writing to score file
            game_over_process(game_blocks, score)
            #==== reset all parameter for new game ====#
            count_time = 0
            health = 100
            score = 0
            user_text = ''
            fps = 2
            simplify_ability_amount = 2
            speed_level = 20
            game_over_flag = True
            simplify = False
        else:
            # add block only after certain time period; also as parameter in complexity func
            if count_time % speed_level == 0:
                new_block = blck.ArithBlock(num1=number1, num2=number2, math_operation=math_operator)
                # append (ArithBlock obj, Rect obj) to list
                game_blocks.append((new_block, new_block.create_block()))
                print(game_blocks[-1])

        # print(game_blocks)
        for g_block in game_blocks:
            g_block[1].top += random.randint(10, 15)   # should be changable(!)
            block_dropping(g_block[1], g_block[0])

        defence_zone() # bottom zone

        # input field
        input_field(user_text)

        # show health field of defence zone
        health = health_reducing(game_blocks, health)           # list of ArithBlock objects
        # show current health points of your defence zone
        health_field(health, game_blocks, score)
        health_title()
        input_answer_title()
        score_title()
        score_field(score)

        #display a simplify button
        simplify = simpl.simplifier_button(screen, simplify_ability_amount)

        pygame.display.flip()  # updating a game process on screen

        dt = clock.tick(fps) # dt - tick(frames) per sec
        count_time += 1

# start our Arith Game - Enjoying)
start_game()