def task1():
    inputs, outputs = read_input()
    filtered = list(map(lambda output: list(filter(lambda code: (len(code) in [2, 3, 4, 7]), output)), outputs))
    total = sum([len(codes) for codes in filtered])
    print(total)

def task2():
    inputs, outputs = read_input()

    grand_total = 0
    for input, output in zip(inputs, outputs):
        one = set([list(x) for x in input if len(x) == 2][0])
        seven = set([list(x) for x in input if len(x) == 3][0])
        four = set([list(x) for x in input if len(x) == 4][0])
        eight = set([list(x) for x in input if len(x) == 7][0])

        possible_six_nine_zero = [set(list(x)) for x in input if len(x) in [6]]
        possible_two_three_five = [set(list(x)) for x in input if len(x) in [5]]

        for candidate in possible_two_three_five:
            if len(seven.intersection(candidate)) == 3:
                three = candidate
                possible_two_three_five.remove(candidate)
            else:
                pass

        for candidate in possible_six_nine_zero:
            if len(four.intersection(candidate)) == 4:
                nine = candidate
                possible_six_nine_zero.remove(candidate)
            else:
                pass

        for x in possible_six_nine_zero:
            for y in possible_two_three_five:
                if len(x.intersection(y)) == 5:
                    six = x
                    five = y
                    possible_six_nine_zero.remove(x)
                    possible_two_three_five.remove(y)

        zero = possible_six_nine_zero.pop()
        two = possible_two_three_five.pop()

        solver = [
            (zero, 0),
            (one, 1),
            (two, 2),
            (three, 3),
            (four, 4),
            (five, 5),
            (six, 6),
            (seven, 7),
            (eight, 8),
            (nine, 9)
        ]

        final = ''
        for code in output:
            for key, value in solver:
                if set(list(code)) == key:
                    final += str(value)

        grand_total += int(final)

    print(grand_total)

def read_input():
    with open("input.txt") as file:
        input = list(map(lambda pair:
                         list(map(lambda codes: codes.split(' '), pair)),
                         [line.strip().split(' | ') for line in file.readlines()]))
        return [x[0] for x in input], [x[1] for x in input]


if __name__ == "__main__":
    task1()
    task2()
