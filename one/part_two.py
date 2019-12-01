from math import floor

from part_one import get_fuel


def get_real_total(fuel):
    additional = get_fuel(fuel)

    if additional <= 0:
        return fuel

    return fuel + get_real_total(additional)


total = 0


with open("data.txt") as fh:
    for line in fh.readlines():
        if line.strip():
            current_fuel = get_fuel(int(line))

            total += get_real_total(current_fuel)

print(f"Total: {total}")
