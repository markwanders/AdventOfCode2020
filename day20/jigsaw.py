with open("input.txt") as f:
    original_pieces = [l.split("\n") for l in f.read().split("\n\n")]


def flip(tile):  # along horizontal axis
    return tile[::-1]


def v_flip(tile):  # along vertical axis
    return rotate270(flip(rotate(tile)))


def rotate(tile):  # 90 degrees clockwise
    return ["".join(t) for t in list(zip(*tile[::-1]))]


def rotate180(tile):
    return rotate(rotate(tile))


def rotate270(tile):
    return rotate(rotate(rotate(tile)))


def print_tile(tile):
    print("\n".join(tile))
    print("\n")


def trim_edges(tile):
    return [c[1:-1] for c in tile[1:-1]]


matching_sides = dict()
tiles = dict()
for piece in original_pieces:
    tile = piece[1:]
    tile_id = int(piece[0][-5:-1])
    tiles[tile_id] = tile
    if tile_id not in matching_sides.keys():
        matching_sides[tile_id] = []
    rotated_tile = rotate(tile)
    edges = [tile[0], tile[-1], rotated_tile[0], rotated_tile[-1]]
    for other_piece in original_pieces:
        other_tile = other_piece[1:]
        other_tile_id = int(other_piece[0][-5:-1])
        if tile_id != other_tile_id and other_tile_id not in matching_sides[tile_id] and tile_id not in matching_sides.get(other_tile_id, []):
            if other_tile_id not in matching_sides.keys():
                matching_sides[other_tile_id] = []
            rotated_other_tile = rotate(other_tile)
            other_edges = [other_tile[0], other_tile[-1], rotated_other_tile[0], rotated_other_tile[-1]]
            if any(s for s in edges if s in other_edges or s in [flip(r) for r in other_edges]) > 0:
                matching_sides[tile_id].append(other_tile_id)
                matching_sides[other_tile_id].append(tile_id)

corners = list(k for k, v in matching_sides.items() if len(v) == 2)
answer = 1
for corner in corners:
    answer *= corner
print(answer)

current_tile_id = corners[1]
column_top = tiles[current_tile_id]
puzzle = trim_edges(column_top)
operations = [rotate, rotate180, rotate270, flip]

i = 1
while i < 14:
    current_tile = tiles[current_tile_id]
    print(current_tile_id)
    print(matching_sides[current_tile_id])
    for adjacent_tile_id in matching_sides[current_tile_id]:
        adjacent_tile = tiles[adjacent_tile_id]
        if current_tile[-1] == adjacent_tile[0]:  # if the bottom of current tile matches top of adjacent tile
            print("Found matching top and bottom!")
            puzzle += trim_edges(adjacent_tile)  # then add it to the bottom of the puzzle, current column
            matching_sides[current_tile_id].remove(adjacent_tile_id)  # remove these tile_ids from the list to solve
            matching_sides[adjacent_tile_id].remove(current_tile_id)
            current_tile_id = adjacent_tile_id
            break
        elif current_tile[-1] == rotate(adjacent_tile)[0]:
            print("Found matching top and bottom after rotating 90 degrees!")
            puzzle += trim_edges(rotate(adjacent_tile))
            matching_sides[current_tile_id].remove(adjacent_tile_id)  # remove these tile_ids from the list to solve
            matching_sides[adjacent_tile_id].remove(current_tile_id)
            tiles[adjacent_tile_id] = rotate(adjacent_tile)  # put in correct position
            current_tile_id = adjacent_tile_id
            break
        elif current_tile[-1] == rotate180(adjacent_tile)[0]:
            print("Found matching top and bottom after rotating 180 degrees!")
            puzzle += trim_edges(rotate180(adjacent_tile))
            matching_sides[current_tile_id].remove(adjacent_tile_id)  # remove these tile_ids from the list to solve
            matching_sides[adjacent_tile_id].remove(current_tile_id)
            tiles[adjacent_tile_id] = rotate180(adjacent_tile)  # put in correct position
            current_tile_id = adjacent_tile_id
            break
        elif current_tile[-1] == rotate270(adjacent_tile)[0]:
            print("Found matching top and bottom after rotating 270 degrees!")
            puzzle += trim_edges(rotate270(adjacent_tile))
            matching_sides[current_tile_id].remove(adjacent_tile_id)  # remove these tile_ids from the list to solve
            matching_sides[adjacent_tile_id].remove(current_tile_id)
            tiles[adjacent_tile_id] = rotate270(adjacent_tile)  # put in correct position
            current_tile_id = adjacent_tile_id
            break
        elif current_tile[-1] == flip(adjacent_tile)[0]:
            print("Found matching top and bottom after flipping!")
            puzzle += trim_edges(flip(adjacent_tile))
            matching_sides[current_tile_id].remove(adjacent_tile_id)  # remove these tile_ids from the list to solve
            matching_sides[adjacent_tile_id].remove(current_tile_id)
            tiles[adjacent_tile_id] = flip(adjacent_tile)
            current_tile_id = adjacent_tile_id
            break
        elif current_tile[-1] == rotate(flip(adjacent_tile))[0]:
            print("Found matching top and bottom after flipping and rotating 90 degrees!")
            puzzle += trim_edges(rotate(flip(adjacent_tile)))
            matching_sides[current_tile_id].remove(adjacent_tile_id)  # remove these tile_ids from the list to solve
            matching_sides[adjacent_tile_id].remove(current_tile_id)
            tiles[adjacent_tile_id] = rotate(flip(adjacent_tile))
            current_tile_id = adjacent_tile_id
            break
        elif current_tile[-1] == rotate180(flip(adjacent_tile))[0]:
            print("Found matching top and bottom after flipping and rotating 180 degrees!")
            puzzle += trim_edges( rotate180(flip(adjacent_tile)))
            matching_sides[current_tile_id].remove(adjacent_tile_id)  # remove these tile_ids from the list to solve
            matching_sides[adjacent_tile_id].remove(current_tile_id)
            tiles[adjacent_tile_id] =  rotate180(flip(adjacent_tile))
            current_tile_id = adjacent_tile_id
            break
        elif current_tile[-1] == rotate270(flip(adjacent_tile))[0]:
            print("Found matching top and bottom after flipping and rotating 270 degrees!")
            puzzle += trim_edges( rotate270(flip(adjacent_tile)))
            matching_sides[current_tile_id].remove(adjacent_tile_id)  # remove these tile_ids from the list to solve
            matching_sides[adjacent_tile_id].remove(current_tile_id)
            tiles[adjacent_tile_id] = rotate270(flip(adjacent_tile))
            current_tile_id = adjacent_tile_id
            break
    i += 1
print_tile(puzzle)
