from rendering import render, clear_terminal
from getch import _Getch
from board import Board

from random import randint


def main():
    board = Board(3, 3)
    cursor_pos = [0, 0]
    player1_is_x = True
    is_player1_turn = True

    key_reader = _Getch()

    print('Would you like to play as x? (y/n)')
    if key_reader().lower() == 'y':
        player1_is_x = True
        is_player1_turn = True
    else:
        player1_is_x = False
        is_player1_turn = False
    clear_terminal()

    # Game loop
    while True:
        render(board.state, board.height, board.width, cursor_pos)
        check_if_win(board.state, player1_is_x)

        key = key_reader()

        if key == 'q':
            exit()
        elif key == 'w' and cursor_pos[1] - 1 >= 0:
            cursor_pos[1] -= 1
        elif key == 'a' and cursor_pos[0] - 1 >= 0:
            cursor_pos[0] -= 1
        elif key == 's' and cursor_pos[1] + 1 <= board.height - 1:
            cursor_pos[1] += 1
        elif key == 'd' and cursor_pos[0] + 1 <= board.width - 1:
            cursor_pos[0] += 1
        elif key == ' ' and board.state[cursor_pos[1]][cursor_pos[0]] == 0:
            if player1_is_x:
                board.state[cursor_pos[1]][cursor_pos[0]] = 1
                render(board.state, board.height, board.width, cursor_pos)
                check_if_win(board.state, player1_is_x)
                ai_move(board, player1_is_x)
            else:
                board.state[cursor_pos[1]][cursor_pos[0]] = 2
                render(board.state, board.height, board.width, cursor_pos)
                check_if_win(board.state, player1_is_x)
                ai_move(board, player1_is_x)


def check_if_win(board_state, player1_is_x):
    for index, row in enumerate(board_state):
        for count, cell in enumerate(board_state[index]):
            if board_state[index][count] != 0:
                # Check for horizontal wins
                if count + 2 < len(board_state[index]) and board_state[index][count + 1] == cell and board_state[index][count + 2] == cell:
                    if cell == 1 and player1_is_x:
                        print('Player 1 wins!')
                        exit(0)
                    elif cell == 2 and not player1_is_x:
                        print('Player 1 wins!')
                        exit(0)
                    else:
                        print('Player 2 wins!')
                        exit(0)
                # Check for vertical wins
                elif index + 2 < len(board_state) and board_state[index + 1][count] == cell and board_state[index + 2][count] == cell:
                    if cell == 1 and player1_is_x:
                        print('Player 1 wins!')
                        exit(0)
                    elif cell == 2 and not player1_is_x:
                        print('Player 1 wins!')
                        exit(0)
                    else:
                        print('Player 2 wins!')
                        exit(0)
                # Check for diagonal wins down right
                elif index + 2 < len(board_state) and count + 2 < len(board_state[index]) and board_state[index + 1][count + 1] == cell and board_state[index + 2][count + 2] == cell:
                    if cell == 1 and player1_is_x:
                        print('Player 1 wins!')
                        exit(0)
                    elif cell == 2 and not player1_is_x:
                        print('Player 1 wins!')
                        exit(0)
                    else:
                        print('Player 2 wins!')
                        exit(0)
                # Check for diagonal wins down left
                elif count - 2 >= 0 and index + 2 < len(board_state) and board_state[index + 1][count - 1] == cell and board_state[index + 2][count - 2] == cell:
                    if cell == 1 and player1_is_x:
                        print('Player 1 wins!')
                        exit(0)
                    elif cell == 2 and not player1_is_x:
                        print('Player 1 wins!')
                        exit(0)
                    else:
                        print('Player 2 wins!')
                        exit(0)
                # Check for a draw
                elif not any(0 in row for row in board_state):
                    print('Draw!')
                    exit(0)


def ai_move(Board, player1_is_x):
    turn_done = False
    while turn_done == False:
        random_height = randint(0, Board.height - 1)
        random_width = randint(0, Board.width - 1)

        if Board.state[random_height][random_width] == 0:
            if player1_is_x:
                Board.state[random_height][random_width] = 2
                turn_done = True
            else:
                Board.state[random_height][random_width] = 1
                turn_done = True


if __name__ == '__main__':
    main()
