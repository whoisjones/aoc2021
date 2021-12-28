def task1():
    positions = read_input()
    max_pos = max(positions)
    min_pos = min(positions)

    best_pos = None
    best_score = 1000000000000000
    for pos in range(min_pos, max_pos + 1):
        current_score = list(map(lambda x: x - pos, positions))
        current_score = sum([x * (-1) if x < 0 else x for x in current_score])
        if current_score < best_score:
            best_score = current_score
            best_pos = pos

    print(f"Best score {best_score} at position {best_pos}.")


def task2():
    positions = read_input()
    max_pos = max(positions)
    min_pos = min(positions)

    best_pos = None
    best_score = 1000000000000000
    for pos in range(min_pos, max_pos + 1):
        current_score = list(map(lambda x: x - pos, positions))
        current_score = [x * (-1) if x < 0 else x for x in current_score]
        current_score = sum([sum(range(1, dist + 1)) for dist in current_score])
        if current_score < best_score:
            best_score = current_score
            best_pos = pos

    print(f"Best score {best_score} at position {best_pos}.")


def read_input():
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        positions = lines[0].split(',')
        positions = [int(x) for x in positions]
        return positions


if __name__ == "__main__":
    task1()
    task2()
