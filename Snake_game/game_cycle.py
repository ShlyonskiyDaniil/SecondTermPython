import pygame as pg
from action_control import Control_first_snake, Control_second_snake
from snake import Snake, Snake_second
from snake_food import Food
from time import time


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def game_cycle(screen, screen_size, delay,
               first_snake, second_snake,
               control_first_snake,
               control_second_snake,
               first_food, second_food,
               game_time, time_flag,
               player_quantity):

    timer = time()
    while control_first_snake.run and control_second_snake.run:
        if time() - timer > game_time:
            time_flag[0] = False
            control_first_snake.run = False

        if time() - timer > game_time // 2:
            pg.time.delay(delay - 30)
        else:
            pg.time.delay(delay)

        screen.fill(BLACK)

        if player_quantity == 'multi':
            control_first_snake.control(first_snake)
            control_second_snake.control(second_snake)

            first_snake.draw_snake(screen)
            first_snake.turn(control_first_snake, screen_size)
            first_snake.movement()

            second_snake.draw_snake(screen)
            second_snake.turn(control_second_snake, screen_size)
            second_snake.movement()

            if time() - timer < game_time // 2:
                second_food.was_eaten(first_snake, control_first_snake)
                second_food.was_eaten(second_snake, control_second_snake)

                second_food.draw_food(screen, first_snake)
                second_food.draw_food(screen, second_snake)

            first_food.was_eaten(first_snake, control_first_snake)
            first_food.was_eaten(second_snake, control_second_snake)

            first_food.draw_food(screen, first_snake)
            first_food.draw_food(screen, second_snake)

            first_snake.bump(control_first_snake, second_snake)
            second_snake.bump(control_second_snake, first_snake)

        elif player_quantity == 'single':
            control_first_snake.control(first_snake)

            first_snake.draw_snake(screen)
            first_snake.turn(control_first_snake, screen_size)
            first_snake.movement()

            first_food.was_eaten(first_snake, control_first_snake)
            first_food.draw_food(screen, first_snake)

            first_snake.bump(control_first_snake)

        pg.display.update()
