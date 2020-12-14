with open("input.txt") as f:
    lines = [line.strip("\n").split(" = ") for line in f.readlines()]

memory = {}
bitmask = ""
for line in lines:
    if line[0] == "mask":
        bitmask = line[1]
    else:
        address = int(line[0][4:-1])
        value_to_assign = int(line[1])
        binary_value = "{0:b}".format(value_to_assign).zfill(36)
        new_value = list(bitmask)
        for i, b in enumerate(bitmask):
            if b == "X":
                new_value[i] = binary_value[i]
        memory[address] = int("".join(new_value), 2)
print(sum(memory.values()))
