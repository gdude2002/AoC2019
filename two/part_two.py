from typing import List

orig_memory: List[int]

with open("data.txt") as fh:
    orig_memory = [
        int(x) for x in fh.read().strip().replace("\n", "").split(",")
    ]


def attempt(noun: int, verb: int):
    memory = orig_memory.copy()
    memory_iter = iter(memory)

    memory[1], memory[2] = noun, verb

    for operation in memory_iter:
        if operation in (1, 2):
            left = next(memory_iter, None)
            right = next(memory_iter, None)
            position = next(memory_iter, None)

            if operation == 1:
                memory[position] = memory[left] + memory[right]
            elif operation == 2:
                memory[position] = memory[left] * memory[right]
        elif operation == 99:
            break

    return memory[0]


wanted = 19690720
result = 0


def run():
    for i in range(99):
        for j in range(99):
            result = attempt(i, j)

            print(f"{i}, {j} -> {result}")

            if wanted == result:
                print("Found noun/verb combo:", i, j)
                print("Result:", 100 * i + j)
                return


run()
