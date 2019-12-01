from math import floor


def get_fuel(mass: float) -> int:
    return floor(mass / 3) - 2


def get_total():
    total = 0

    with open("data.txt") as fh:
        for line in fh.readlines():
            if line.strip():
                total += get_fuel(int(line))

    return total


if __name__ == "__main__":
    print(f"Total mass: {get_total()}")
