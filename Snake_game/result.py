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

    if points_w > points_i:		
        first_snake.win = True		
        second_snake.win = False		
    elif points_w < points_i:		
        first_snake.win = False		
        second_snake.win = True		
    else:		
        first_snake.win = True		
        second_snake.win = True		

    print('Winner:'.ljust(10, ' '), end='')		
    if first_snake.win and second_snake.win:		
        print('FRIENDSHIP')		
        print('-' * 25)		
    elif first_snake.win:		
        print(f'{player_wasd}')		
        print('-' * 25)		
    elif second_snake.win:		
        print(f'{player_ijkl}')		
        print('-' * 25)