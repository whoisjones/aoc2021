import numpy as np


def task1():
    numbers_drawn, boards = read_input()
    currently_drawn = []
    for drawn_number in numbers_drawn:
        currently_drawn.append(drawn_number)

        for game in boards:
            for i in range(5):
                row = game[i]
                col = game[:, i]
                if set(row) <= set(currently_drawn) or set(col) <= set(currently_drawn):
                    unmarked_numbers = list(filter(lambda x: x not in currently_drawn, game.flatten().tolist()))
                    sum_unmakred_numbers = sum(unmarked_numbers)
                    return sum_unmakred_numbers * drawn_number


def task2():
    numbers_drawn, boards = read_input()
    boards = [Board(board=b) for b in boards]

    currently_drawn = []
    for drawn_number in numbers_drawn:
        currently_drawn.append(drawn_number)

        for board in boards:
            for i in range(5):
                row = board.board[i]
                col = board.board[:, i]
                if set(row) <= set(currently_drawn) or set(col) <= set(currently_drawn):
                    board.has_won = True
                    if all([x.has_won for x in boards]):
                        unmarked_numbers = list(filter(lambda x: x not in currently_drawn, board.board.flatten().tolist()))
                        sum_unmakred_numbers = sum(unmarked_numbers)
                        return sum_unmakred_numbers * drawn_number


class Board:
    def __init__(self, board: np.array):
        self.board = board
        self.has_won = False


def read_input():
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        numbers_drawn = [int(x) for x in lines[0].split(',')]
        boards = []
        for idx, line in enumerate(lines):
            if line == "":
                game = []
                for i in range(1, 6):
                    game.append([int(x) for x in lines[idx + i].split()])
                boards.append(np.array(game))
    return numbers_drawn, boards


if __name__ == "__main__":
    print(task1())
    print(task2())
