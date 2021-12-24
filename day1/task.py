def task1():
    vals = read_input()

    increased = 0
    for idx, _ in enumerate(vals):
        if idx == 0:
            pass
        else:
            if vals[idx] > vals[idx - 1]:
                increased += 1

    print(f"Solution: {increased}")


def task2():
    vals = read_input()

    increased = 0
    for idx, _ in enumerate(vals):
        curr = sum(vals[idx:idx+3])
        next = sum(vals[idx+1:idx+3+1])
        if next > curr:
            increased += 1

    print(f"Solution: {increased}")


def read_input():
    with open("input.txt") as file:
        lines = file.readlines()
        vals = [int(line.strip()) for line in lines]
    return vals


if __name__ == "__main__":
    task1()
    task2()