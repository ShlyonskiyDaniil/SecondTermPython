import pygame as pg
from button import Button
from menu import menu_screen
import sys
from colours import Colours


def multi_result_screen(screen, first_snake, second_snake, first_food,
                        second_food, player_wasd, player_ijkl, time_flag):
    """Defines a result screen view in multiplyplayer mode.

    Arguments:
        screen: Game display.
        first_snake(Snake): An instanse of Snake.
        second_snake(Second_snake): An instance Second_snake.
        first_food(Food): An instance of Food.
        second_food(Food): An instance of Food.
        player_wasd(str): Name of player, which plays on 'wasd' keys.
        player_ijkl(str): Name of player, which plays on 'ijkl' keys.
        time_flag(bool): Var, that trace time end.
    """

    result_screen = True

    points_w = len(first_snake.tail)
    points_i = len(second_snake.tail)

    player_w = player_wasd + ':'
    player_w = '{}{}'.format(player_w.ljust(20, ' '), points_w)

    player_i = player_ijkl + ':'
    player_i = '{}{}'.format(player_i.ljust(20, ' '), points_i)

    winner = 'Winner:'.ljust(20, ' ')

    if not time_flag[0]:
        if points_w > points_i:
            first_snake.win = 0
            second_snake.win = 1
        elif points_w < points_i:
            first_snake.win = 1
            second_snake.win = 0
        else:
            first_snake.win = 1
            second_snake.win = 1

    if (first_snake.win + second_snake.win >= 2 or
       first_snake.win + second_snake.win == 0):

        winner += 'FRIENDSHIP'
    elif first_snake.win == 0:
        winner += '{}'.format(player_wasd)
    elif second_snake.win == 0:
        winner += '{}'.format(player_ijkl)

    cause_button = Button(0, 0, -40, 40, Colours().BLACK, Colours().BLACK)
    cause_button_ = Button(0, 0, -60, 60, Colours().BLACK, Colours().BLACK)
    first_player_scores = Button(0, 0, 20, 140,
                                 Colours().BLACK,
                                 Colours().BLACK)
    second_player_scores = Button(0, 0, 20, 190,
                                  Colours().BLACK,
                                  Colours().BLACK)
    winner_button = Button(0, 0, 20, 240, Colours().BLACK, Colours().BLACK)
    menu_button = Button(200, 50, 150, 360, Colours().GREY, Colours().PINK)

    while result_screen:
        pg.time.delay(50)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        screen.fill(Colours().BLACK)

        first_food.draw_food(screen, first_snake)
        second_food.draw_food(screen, second_snake)

        first_snake.draw_snake(screen)
        second_snake.draw_snake(screen)

        if not time_flag[0]:
            cause_button.draw(screen, 'OVERTIME ' * 10, 30, 17)
            cause_button_.draw(screen, 'OVERTIME ' * 10, 30, 17)
        else:
            cause_button.draw(screen, 'BUMPED ' * 10, 30, 17)
            cause_button_.draw(screen, 'BUMPED ' * 10, 30, 17)

        first_player_scores.draw(screen, player_w, 30, 17)
        second_player_scores.draw(screen, player_i, 30, 17)
        winner_button.draw(screen, winner, 30, 17)

        key = menu_button.draw(screen, 'Back to menu', 30, 17)
        if key == 'done':
            break

        pg.display.update()


def single_result_screen(screen, first_snake, first_food,
                         player_wasd, time_flag):
    """Defines a result screen view in singleplayer mode.

    Arguments:
        screen: Game display.
        first_snake(Snake): An instanse of Snake.
        first_food(Food): An instance of Food.
        player_wasd(str): Name of player, which plays on 'wasd' keys.
        time_flag(bool): Var, that trace time end.
    """

    result_screen = True

    points_w = len(first_snake.tail)

    player_w = player_wasd + ':'
    player_w = '{} {}'.format(player_w.ljust(20, ' '), points_w)

    cause_button = Button(0, 0, - 40, 40, Colours().BLACK, Colours().BLACK)
    cause_button_ = Button(0, 0, - 60, 60, Colours().BLACK, Colours().BLACK)
    player_scores = Button(0, 0, 130, 180, Colours().BLACK, Colours().BLACK)
    menu_button = Button(200, 50, 150, 360, Colours().GREY, Colours().PINK)

    while result_screen:
        pg.time.delay(50)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        screen.fill(Colours().BLACK)

        first_food.draw_food(screen, first_snake)
        first_snake.draw_snake(screen)

        if not time_flag[0]:
            cause_button.draw(screen, 'OVERTIME ' * 10, 30, 17)
            cause_button_.draw(screen, 'OVERTIME ' * 10, 30, 17)
        else:
            cause_button.draw(screen, 'BUMPED ' * 10, 30, 17)
            cause_button_.draw(screen, 'BUMPED ' * 10, 30, 17)

        player_scores.draw(screen, player_w, 30, 17)

        key = menu_button.draw(screen, 'Back to menu', 30, 17)
        if key == 'done':
            break

        pg.display.update()
