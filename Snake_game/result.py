import pygame as pg
from button import Button
from menu import menu_screen
import sys


BLACK = (0, 0, 0)


def multi_result_screen(screen, first_snake, second_snake, first_food,
                        second_food, player_wasd, player_ijkl, time_flag):
    result_screen = True

    points_w = len(first_snake.tail)
    points_i = len(second_snake.tail)

    player_w = player_wasd + ':'
    player_w = '{} {}'.format(player_w.ljust(15, ' '), points_w)

    player_i = player_ijkl + ':'
    player_i = '{} {}'.format(player_i.ljust(15, ' '), points_i)

    winner = 'Winner:'.ljust(15, ' ')

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

    cause_button = Button(0, 0, -40, 40, (0, 0, 0), (0, 0, 0))
    cause_button_ = Button(0, 0, -60, 60, (0, 0, 0), (0, 0, 0))
    first_player_scores = Button(0, 0, 20, 140, (0, 0, 0), (0, 0, 0))
    second_player_scores = Button(0, 0, 20, 190, (0, 0, 0), (0, 0, 0))
    winner_button = Button(0, 0, 20, 240, (0, 0, 0), (0, 0, 0))
    menu_button = Button(200, 50, 150, 360, (169, 169, 169), (225, 186, 207))

    while result_screen:
        pg.time.delay(50)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        screen.fill(BLACK)

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
    result_screen = True

    points_w = len(first_snake.tail)

    player_w = player_wasd + ':'
    player_w = '{} {}'.format(player_w.ljust(20, ' '), points_w)

    cause_button = Button(0, 0, - 40, 40, (0, 0, 0), (0, 0, 0))
    cause_button_ = Button(0, 0, - 60, 60, (0, 0, 0), (0, 0, 0))
    player_scores = Button(0, 0, 130, 180, (0, 0, 0), (0, 0, 0))
    menu_button = Button(200, 50, 150, 360, (169, 169, 169), (225, 186, 207))

    while result_screen:
        pg.time.delay(50)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        screen.fill(BLACK)

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
