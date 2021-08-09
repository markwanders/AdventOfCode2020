import math
import re

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


def rotate_flip(tile):
    return rotate(flip(tile))


def rotate_v_flip(tile):
    return rotate(v_flip(tile))


def rotate180_flip(tile):
    return rotate180(flip(tile))


def rotate270_flip(tile):
    return rotate270(flip(tile))


def print_tile(tile):
    print("\n".join(tile))
    print("\n")


def trim_edges(tile):
    return [c[1:-1] for c in tile[1:-1]]


def find_sea_monsters(completed_puzzle):
    k = len(completed_puzzle[0])
    for operation in operations:
        image = "\n".join(operation(completed_puzzle))
        monsters = len(re.findall('(?=(#..{'+str(k-19)+'}#.{4}##.{4}##.{4}###.{'+str(k-19)+'}.#.{2}#.{2}#.{2}#.{2}#.{2}#.{3}))', image, re.DOTALL))
        if monsters > 0:
            return monsters

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

puzzle_size = int(math.sqrt(len(tiles)))


def find_vertical_match(tile_id):
    tile = tiles[tile_id]
    for adjacent_tile_id in matching_sides[tile_id]:
        adjacent_tile = tiles[adjacent_tile_id]
        if tile[-1] == adjacent_tile[0]:  # if the bottom of current tile matches top of adjacent tile
            matching_sides[tile_id].remove(adjacent_tile_id)  # remove these tile_ids from the list to solve
            matching_sides[adjacent_tile_id].remove(tile_id)
            return adjacent_tile_id
        else:
            for operation in operations:
                if tile[-1] == operation(adjacent_tile)[0]:
                    matching_sides[tile_id].remove(adjacent_tile_id)
                    matching_sides[adjacent_tile_id].remove(tile_id)
                    tiles[adjacent_tile_id] = operation(adjacent_tile)  # put in correct position
                    return adjacent_tile_id


def find_horizontal_match(tile_id):
    tile = tiles[tile_id]
    for adjacent_tile_id in matching_sides[tile_id]:
        adjacent_tile = tiles[adjacent_tile_id]
        if rotate(tile)[-1] == rotate(adjacent_tile)[0]:  # if the left of current tile matches right of adjacent tile
            matching_sides[tile_id].remove(adjacent_tile_id)  # remove these tile_ids from the list to solve
            matching_sides[adjacent_tile_id].remove(tile_id)
            return adjacent_tile_id
        else:
            for operation in operations:
                if rotate(tile)[-1] == rotate(operation(adjacent_tile))[0]:
                    matching_sides[tile_id].remove(adjacent_tile_id)
                    matching_sides[adjacent_tile_id].remove(tile_id)
                    tiles[adjacent_tile_id] = operation(adjacent_tile)  # put in correct position
                    return adjacent_tile_id


def add_tile_to_puzzle(_tile_id, _puzzle, insert_height):
    if len(_puzzle) < 8 * puzzle_size:  # if we haven't completed a single column yet, just add the tile to the bottom
        _puzzle += trim_edges(tiles[_tile_id])
    else:
        tile_to_add = trim_edges(tiles[_tile_id])
        insert_height = (insert_height + 1) * 8
        for i, line in enumerate(tile_to_add):
            _puzzle[insert_height + i] += line


current_tile_id = corners[1]  # top left corner found by trial and error, should improve
column_top = current_tile_id
puzzle = trim_edges(tiles[current_tile_id])
operations = [rotate, rotate180, rotate270, flip, rotate_flip, rotate180_flip, rotate270_flip, v_flip, rotate_v_flip]

for x in range(0, puzzle_size):
    for y in range(0, puzzle_size - 1):
        current_tile = tiles[current_tile_id]
        matching_tile_id = current_tile_id = find_vertical_match(current_tile_id)
        add_tile_to_puzzle(current_tile_id, puzzle, y)
    column_top = current_tile_id = find_horizontal_match(column_top)
    if current_tile_id:
        add_tile_to_puzzle(current_tile_id, puzzle, -1)

pixels = sum([line.count('#') for line in puzzle])
print(pixels - find_sea_monsters(puzzle) * 15)  # 16 pixels per sea monster
