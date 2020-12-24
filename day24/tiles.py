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


def neighbors(tile):
    return [tile + (2 + 0j), tile + (-2 + 0j), tile + (1 + 1j), tile + (-1 - 1j), tile + (1 - 1j), tile + (-1 + 1j)]


for i in range(100):
    old_tiles = dict(tiles)
    tiles_to_check = list(tiles.keys())
    while len(tiles_to_check) > 0:
        tile = tiles_to_check.pop()
        neighboring_tiles = neighbors(tile)
        black_neighbors = sum(old_tiles.get(n, False) for n in neighboring_tiles)
        if old_tiles.get(tile, False):
            if black_neighbors == 0 or black_neighbors > 2:
                tiles[tile] = False
            tiles_to_check += list(t for t in neighboring_tiles if t not in tiles.keys())
        elif not old_tiles.get(tile, False) and black_neighbors == 2:
            tiles[tile] = True
print(sum(v for v in tiles.values()))
