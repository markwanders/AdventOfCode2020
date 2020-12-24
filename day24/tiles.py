with open("input.txt") as f:
    lines = f.read().split("\n")

tiles = {}
for line in lines:
    pos = 0 + 0j
    chars = [char for char in line]
    while len(chars) > 0:
        instr = chars.pop(0)
        if 'n' in instr or 's' in instr:
            instr += chars.pop(0)
        if instr == 'e':
            pos += 2
        elif instr == 'w':
            pos -= 2
        elif instr == 'nw':
            pos = pos + (-1 + 1j)
        elif instr == 'ne':
            pos = pos + (1 + 1j)
        elif instr == 'sw':
            pos = pos + (-1 - 1j)
        elif instr == 'se':
            pos = pos + (1 - 1j)
    if pos in tiles:
        tiles[pos] ^= True
    else:
        tiles[pos] = True
print(sum(v for v in tiles.values()))
