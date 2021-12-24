def task1():
    commands = read_input()

    horizontal = 0
    vertical = 0

    for command in commands:
        direction, value = command
        if direction == "forward":
            horizontal += int(value)
        elif direction == "down":
            vertical += int(value)
        elif direction == "up":
            vertical -= int(value)
        else:
            raise Exception

    print(f"Solution: {horizontal * vertical}")


def task2():
    commands = read_input()

    depth = 0
    horizontal = 0
    vertical = 0

    for command in commands:
        direction, value = command
        if direction == "forward":
            horizontal += int(value)
            depth += (vertical * int(value))
        elif direction == "down":
            vertical += int(value)
        elif direction == "up":
            vertical -= int(value)
        else:
            raise Exception

    print(f"Solution: {horizontal * depth}")


def read_input():
    with open("input.txt") as file:
        lines = file.readlines()
        vals = [line.strip().split() for line in lines]
    return vals


if __name__ == "__main__":
    task1()
    task2()