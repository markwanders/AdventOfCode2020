with open("input.txt") as f:
    instructions = [line.strip().split(" ") for line in f.readlines()]

indeces = set()
accumulator, index = 0, 0
while True:
    instruction = instructions[index][0]
    argument = int(instructions[index][1])
    if instruction == "acc":
        accumulator += argument
        index += 1
    elif instruction == "jmp":
        index += argument
    elif instruction == "nop":
        index += 1
    else:
        print("Unrecognized instruction: %s at index %s" % (instruction[index], index))
    if index in indeces:
        break
    indeces.add(index)
print(accumulator)
