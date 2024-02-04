# кол-во клеток
BOARD_SIZE = 3
# Игровое поле
BOARD = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def draw_board():
    '''Выводим игровое поле '''
    print('_' * 4 * BOARD_SIZE)
    for i in range(BOARD_SIZE):
        print((' ' * 3 + '|') * 3)
        print('', BOARD[i * BOARD_SIZE], '|', BOARD[1 + i * BOARD_SIZE],
              '|', BOARD[2 + i * BOARD_SIZE], '|')
        print(('_' * 3 + '|') * 3)


def game_step(index, char):
    '''Выполняем ход'''
    if (index > 9 or index < 1 or BOARD[index - 1] in ('X', 'O')):
        return False

    BOARD[index - 1] = char
    return True


def check_win():
    win = False

    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонтальные линии
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикальные линии
        (0, 4, 8), (2, 4, 6)  # Диагональные линии
    )

    for pos in win_combination:
        if (BOARD[pos[0]] == BOARD[pos[1]] and BOARD[pos[1]] == BOARD[pos[2]]):
            win = BOARD[pos[0]]

    return win


def start_game():
    # текущий игрок
    current_player = 'X'
    # номер шага
    step = 1
    draw_board()
    while (step < 10) and (check_win() == False):
        index = input(f'Ходит игрок {current_player}. Введите номер поля (0 - выход): ')
        if (index == '0'):
            break

        # если получилось сделать шаг
        if (game_step(int(index), current_player)):
            print('Удачный ход!')

            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

            draw_board()
            # увеличим номер хода
            step += 1
        else:
            print('Неверный номер! Повторите')
    if step == 10:
        print('Игра окончена. Ничья!')
    else:
        print(f'Выиграл {check_win()}')


print('Welcom in Crosses and Toes')

start_game()
