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
        if index >= len(instr):
            return 0, accumulator
        if index in indices:
            return 1, accumulator
        indices.add(index)


print(run_program(instructions)[1])


def fix_program(instr):
    for op in instr:
        changed_instructions = instr.copy()
        op_index = instr.index(op)
        if op[0] == "jmp":
            changed_instructions[op_index] = ["nop", op[1]]
        elif op[0] == "nop":
            changed_instructions[op_index] = ["jmp", op[1]]
        answer = run_program(changed_instructions)
        if answer[0] == 0:
            return answer


print(fix_program(instructions)[1])
