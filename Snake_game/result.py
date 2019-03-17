def game_result(first_snake, second_snake, player_wasd, player_ijkl, time_flag):		
    points_w = len(first_snake.tail)		
    points_i = len(second_snake.tail)		
    player_w = player_wasd + ':'		
    player_i = player_ijkl + ':'		

    print('-' * 25)		
    print('{} {}'.format(player_w.ljust(10, ' '), points_w))		
    print('{} {}'.format(player_i.ljust(10, ' '), points_i))		
    print('-' * 25)		
    print('-' * 25)		


    print('Cause:'.ljust(10, ' '), end='')		
    if not time_flag:		
        print('TIME IS OVER')		
    else:		
        print('BUMPED')		
    print('-' * 25)		
    print('-' * 25)	

    if not time_flag:
        if points_w > points_i:		
            first_snake.win = 0		
            second_snake.win = 1		
        elif points_w < points_i:		
            first_snake.win = 1		
            second_snake.win = 0		
        else:		
            first_snake.win = 1		
            second_snake.win = 1		

    print('Winner:'.ljust(10, ' '), end='')		
    if first_snake.win + second_snake.win >= 2:
        print('FRIENDSHIP')		
        print('-' * 25)		
    elif first_snake.win == 0:
        print(f'{player_wasd}')		
        print('-' * 25)		
    elif second_snake.win == 0:		
        print(f'{player_ijkl}')		
        print('-' * 25)
