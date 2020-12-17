from itertools import product, starmap

data = {}

with open("input.txt") as f:
    y = 0
    z = 0
    for _y in [line.rstrip() for line in f]:
        x = 0
        for _x in _y:
            data[(x, y, z)] = _x
            x += 1
        y += 1


def neighbors(x, y, z):
    n = list(starmap(lambda a, b, c: (x + a, y + b, z + c), product((0, -1, +1), (0, -1, +1), (0, -1, +1))))
    n.remove((x, y, z))
    return n


def part1(g):
    grid = dict(g)
    for i in range(6):
        old_grid = grid.copy()
        points_to_check = list(grid.keys())
        while len(points_to_check) > 0:
            point = points_to_check.pop()
            neighbor_points = neighbors(point[0], point[1], point[2])
            active_neighbors = sum(n == "#" for n in [old_grid.get(p, ".") for p in neighbor_points])
            if old_grid.get(point, ".") == "#":
                points_to_check += list(p for p in neighbor_points if p not in grid.keys())
                if not (active_neighbors == 2 or active_neighbors == 3):
                    grid[point] = "."
            elif active_neighbors == 3:
                grid[point] = "#"
    print(sum(v == "#" for v in grid.values()))


part1(data)
