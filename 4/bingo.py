import os
import re
import pprint


def number_draws(line):
    number_strings = [num for num in re.split(' |,|\n', line)]
    return [int(num) for num in number_strings[:-1]]


def read_boards(lines):
    boards = []
    curr_board = []
    for lineno in range(len(lines)):
        if lineno % 6 == 0:
            boards.append(curr_board)
            curr_board = []
        else:
            nums = [(int(num), False) for num in lines[lineno].split()]
            curr_board.append(nums)
    boards.append(curr_board)
    return boards[1:]


def mark_draw(boards, draw):
    for board in boards:
        for row_idx, row in enumerate(board):
            for col_idx, (num, drawed) in enumerate(row):
                board[row_idx][col_idx] = (num, drawed or num == draw)

    return boards


def check_boards(boards):
    for board_idx, board in enumerate(boards):
        if check_board_rows(board) or check_board_cols(board):
            return board_idx
    return -1


def check_board_rows(board):
    for row in board:
        bingo = True
        for _, called in row:
            bingo &= called
        if bingo:
            return True
    return False


def check_board_cols(board):
    for col_idx in range(len(board[0])):
        bingo = True
        for row in board:
            bingo &= row[col_idx][1]
        if bingo:
            return True
    return False


def play_bingo(draws, boards):
    for draw_idx, draw in enumerate(draws):
        boards = mark_draw(boards, draw)
        winning_board_idx = check_boards(boards)
        if winning_board_idx != -1:
            break

    return winning_board_idx, draw_idx


def get_worst_board(draws, boards):
    game_boards, game_draws = boards, draws
    last_winning_board = []
    last_winning_num = 0
    while len(game_boards) > 0 and len(game_draws) > 0:
        winning_board_index, winning_draw_idx = play_bingo(
            game_draws, game_boards)
        last_winning_board = game_boards[winning_board_index]
        last_winning_num = game_draws[winning_draw_idx]
        del game_boards[winning_board_index]
        game_draws = game_draws[winning_draw_idx:]
    print(calc_score(last_winning_board) * last_winning_num)


def calc_score(board):
    sum_uncalled = 0
    for row in board:
        for num, called in row:
            if not called:
                sum_uncalled += num
    return sum_uncalled


with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input:
    readings = [reading for reading in input.readlines()]
    draws = number_draws(readings[0])
    boards = read_boards(readings[1:])
    # winning_board_index, winning_draw_idx = play_bingo(draws, boards)
    # if winning_board_index != -1:
    #     print(
    #         calc_score(boards[winning_board_index]) * draws[winning_draw_idx])
    get_worst_board(draws, boards)
