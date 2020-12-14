from itertools import product

with open("input.txt") as f:
    lines = [line.strip("\n").split(" = ") for line in f.readlines()]


def part1():
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
    return sum(memory.values())


print(part1())


def replace(binary):
    options = [(c,) if c != "X" else ("0", "1") for c in binary]
    return (''.join(o) for o in product(*options))


def part2():
    memory = {}
    bitmask = ""
    for line in lines:
        if line[0] == "mask":
            bitmask = line[1]
        else:
            address_to_assign = int(line[0][4:-1])
            binary_address = list("{0:b}".format(address_to_assign).zfill(36))
            for i, b in enumerate(bitmask):
                if b == "X":
                    binary_address[i] = "X"
                elif b == "1":
                    binary_address[i] = "1"
            for address in list(replace(binary_address)):
                memory[address] = int(line[1])
    return sum(memory.values())


print(part2())
