import numpy as np

def task1():

    logs = read_input()
    logs = np.array(logs)

    gamma = ''
    epsilon = ''
    for dim in range(logs.shape[1]):
        curr = logs[:, dim]
        unique, count = np.unique(curr, return_counts=True)
        zipped = dict(zip(unique, count))
        max_bit = max(zipped, key=zipped.get)
        min_bit = min(zipped, key=zipped.get)
        gamma += str(max_bit)
        epsilon += str(min_bit)

    gamma_decimal = int(gamma, 2)
    epsilon_decimal = int(epsilon, 2)

    power_consumption = gamma_decimal * epsilon_decimal

    print(f"Solution: {power_consumption}")

def task2():
    report = np.array(read_input())
    oxygen_generator_rate = get_rate(report, func=max, equal_bit=1)
    co2_scrubber_rate = get_rate(report, func=min, equal_bit=0)
    life_supporting_rate = oxygen_generator_rate * co2_scrubber_rate
    print(f"Solution: {life_supporting_rate}")


def get_rate(report: np.array, func, equal_bit: int = 1):
    for dim in range(report.shape[1]):

        if report.shape[0] == 1:
            pass
        else:
            curr = report[:, dim]
            unique, count = np.unique(curr, return_counts=True)
            zipped = dict(zip(unique, count))
            if zipped.get(0) == zipped.get(1):
                filter = [x[dim] == equal_bit for x in report]
            else:
                bit = func(zipped, key=zipped.get)
                filter = [x[dim] == bit for x in report]
            report = report[filter]

    binary = convert_numpy_to_binary_str(report[0])
    decimal = int(binary, 2)
    return decimal


def convert_numpy_to_binary_str(array: np.array):
    return ''.join(map(str, array.tolist()))


def read_input():
    with open("input.txt") as file:
        lines = file.readlines()
        vals = [list(line.strip()) for line in lines]
        vals = [[int(x) for x in sublist] for sublist in vals]
    return vals


if __name__ == "__main__":
    task1()
    task2()