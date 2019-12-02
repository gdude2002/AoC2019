from typing import List

memory: List[int]


with open("data.txt") as fh:
    memory = [
        int(x) for x in fh.read().strip().replace("\n", "").split(",")
    ]


memory_iter = iter(memory)

print("Initial state:", memory)

for i, operation in enumerate(memory_iter):

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
    else:
        print(f"Unknown opcode: {operation}")

    print(f"{i} ({operation}) =>", memory)

print(f"Position 0: {memory[0]}")
