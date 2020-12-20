with open("input.txt") as f:
    original_pieces = [l.split("\n") for l in f.read().split("\n\n")]


def print_tile(tile):
    for line in tile:
        print("%s" % line)
    print("\n")


def to_number(line):
    return int(line.replace(".", "0").replace("#", "1"), 2)


def transpose_tile(tile):
    return ["".join(t) for t in list(map(list, zip(*tile)))]


def flip_tile_horizontally(tile):
    return [s[::-1] for s in tile]


def flip_tile_vertically(tile):
    return transpose_tile([s[::-1] for s in transpose_tile(tile)])


def permutations(pieces):
    permutations = {}
    for piece in pieces:
        header = piece[0]
        tile = piece[1:]
        tile_id = int(header[-5:-1])
        permutations[tile_id] = []
        permutations[tile_id] += [flip_tile_horizontally(tile)]
        permutations[tile_id] += [flip_tile_vertically(tile)]
        permutations[tile_id] += [flip_tile_vertically(flip_tile_horizontally(tile))]
    return permutations


tops, bottoms, lefts, rights = dict(), dict(), dict(), dict()
pieces = permutations(original_pieces)
print(pieces)
for tile_id, permutations in pieces.items():
    tops[tile_id], bottoms[tile_id], lefts[tile_id], rights[tile_id] = [], [], [], []
    for tile in permutations:
        top = tile[0]
        bottom = tile[-1]
        transposed_tile = transpose_tile(tile)
        left = transposed_tile[0]
        right = transposed_tile[-1]
        tops[tile_id] += [to_number(top)]
        bottoms[tile_id] += [to_number(bottom)]
        lefts[tile_id] += [to_number(left)]
        rights[tile_id] += [to_number(right)]


print(bottoms, tops, lefts, rights)

