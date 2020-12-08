with open("input.txt") as f:
    instructions = [line.strip().split(" ") for line in f.readlines()]


def run_program(instr):
    indices = set()
    accumulator, index = 0, 0
    while True:
        instruction = instr[index][0]
        argument = int(instr[index][1])
        if instruction == "acc":
            accumulator += argument
            index += 1
        elif instruction == "jmp":
            index += argument
        elif instruction == "nop":
            index += 1
        else:
            print("Unrecognized instruction: %s at index %s" % (instruction[index], index))
        if index >= len(instr):
            print("Tried to access operation beyond program memory: %s %s" % (index, accumulator))
            break
        if index in indices:
            break
        indices.add(index)
    return accumulator


print(run_program(instructions))


def variate(instr):
    nopjmp = [i for i in instr if i[0] == "jmp" or i[0] == "nop"]
    for op in nopjmp:
        changed_instructions = instr.copy()
        op_index = instr.index(op)
        if op[0] == "jmp":
            changed_instructions[op_index] = ["nop", op[1]]
            run_program(changed_instructions)
        elif op[0] == "nop":
            changed_instructions[op_index] = ["jmp", op[1]]
            run_program(changed_instructions)


variate(instructions)
