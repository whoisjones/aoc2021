import numpy as np


def task(consider_diagonal: bool):
    points = read_input()
    field = np.zeros([1000, 1000])
    for point_pair in points:
        x_selector, y_selector = compute_line(point_pair, consider_diagonal)
        field[x_selector, y_selector] += 1
    unique, counts = np.unique(field, return_counts=True)
    output = dict(zip(unique, counts))
    return f"Output: {output}."


def compute_line(point_pair, consider_diagonal):
    from_point, to_point = point_pair

    if from_point.x == to_point.x:
        if from_point.y < to_point.y:
            y = range(from_point.y, to_point.y + 1)
        else:
            y = range(to_point.y, from_point.y + 1)
        x = from_point.x

    elif from_point.y == to_point.y:
        if from_point.x < to_point.x:
            x = range(from_point.x, to_point.x + 1)
        else:
            x = range(to_point.x, from_point.x + 1)
        y = from_point.y
    else:
        if consider_diagonal:
            if from_point.x < to_point.x and from_point.y < to_point.y:
                x = [[x_coord] for x_coord in range(from_point.x, to_point.x + 1)]
                y = [[y_coord] for y_coord in range(from_point.y, to_point.y + 1)]
            elif from_point.x < to_point.x and from_point.y > to_point.y:
                x = [[x_coord] for x_coord in range(from_point.x, to_point.x + 1)]
                y = [[y_coord] for y_coord in reversed(range(to_point.y, from_point.y + 1))]
            elif from_point.x > to_point.x and from_point.y > to_point.y:
                x = [[x_coord] for x_coord in range(to_point.x, from_point.x + 1)]
                y = [[y_coord] for y_coord in range(to_point.y, from_point.y + 1)]
            else:
                x = [[x_coord] for x_coord in range(to_point.x, from_point.x + 1)]
                y = [[y_coord] for y_coord in reversed(range(from_point.y, to_point.y + 1))]
        else:
            x = []
            y = []

    return x, y


class Point:
    def __init__(self, coordinates: list):
        self.x = coordinates[0]
        self.y = coordinates[1]


def read_input():
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip().split(" -> ") for line in lines]
        coordinates = [[list(map(lambda x: int(x), coordinate.split(','))) for coordinate in pair] for pair in lines]
        points = [[Point(coordinate) for coordinate in from_to_pair] for from_to_pair in coordinates]
        return points


if __name__ == "__main__":
    print(task(False))
    print(task(True))
