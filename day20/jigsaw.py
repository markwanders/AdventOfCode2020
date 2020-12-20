with open("input.txt") as f:
    original_pieces = [l.split("\n") for l in f.read().split("\n\n")]


def transpose_tile(tile):
    return ["".join(t) for t in list(map(list, zip(*tile)))]


matching_sides = dict()
for piece in original_pieces:
    tile = piece[1:]
    tile_id = int(piece[0][-5:-1])
    if tile_id not in matching_sides.keys():
        matching_sides[tile_id] = []
    transposed_tile = transpose_tile(tile)
    edges = [tile[0], tile[-1], transposed_tile[0], transposed_tile[-1]]
    for other_piece in original_pieces:
        other_tile = other_piece[1:]
        other_tile_id = int(other_piece[0][-5:-1])
        if tile_id != other_tile_id and other_tile_id not in matching_sides[tile_id] and tile_id not in matching_sides.get(other_tile_id, []):
            if other_tile_id not in matching_sides.keys():
                matching_sides[other_tile_id] = []
            transposed_other_tile = transpose_tile(other_tile)
            other_edges = [other_tile[0], other_tile[-1], transposed_other_tile[0], transposed_other_tile[-1]]
            if any(s for s in edges if s in other_edges or s in [r[::-1] for r in other_edges]) > 0:
                matching_sides[tile_id].append(other_tile_id)
                matching_sides[other_tile_id].append(tile_id)

corners = list(k for k, v in matching_sides.items() if len(v) == 2)
answer = 1
for corner in corners:
    answer *= corner
print(answer)
