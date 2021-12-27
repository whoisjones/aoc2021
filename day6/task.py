def task(days: int):
    population = read_input()
    for _ in range(days):
        new_fishes = population.get(0)

        new_population = {}
        for days_to_live, pop in population.items():
            if days_to_live == 0:
                if new_population.get(6):
                    new_population[6] += pop
                else:
                    new_population[6] = pop
            else:
                if (days_to_live - 1) == 6 and new_population.get(6):
                    new_population[days_to_live - 1] += pop
                else:
                    new_population[days_to_live - 1] = pop

        if new_fishes:
            new_population[8] = new_fishes

        population = new_population

    print(sum(population.values()))


def read_input():
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        population = lines[0].split(',')
        population = [int(x) for x in population]
        population = {x: population.count(x) for x in population}
        return population

if __name__ == "__main__":
    task(days=80)
    task(days=256)
