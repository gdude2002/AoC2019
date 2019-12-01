from math import floor

from part_one import get_fuel, get_total


total_before = get_total()


def calculate_extra(fuel: int):
    return floor(fuel / 3) - 2


def get_real_total(fuel):
    additional = calculate_extra(fuel)

    if additional <= 0:
        return fuel

    return fuel + get_real_total(additional)


total = 0


with open("data.txt") as fh:
    for line in fh.readlines():
        if line.strip():
            fuel = get_fuel(int(line))

            total += get_real_total(fuel)

print(f"Total: {total}")


# Wrong: 5109605 (too high)
