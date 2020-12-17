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


def print_grid(grid):
    string = ""
    y = 0
    for k, v in grid.items():
        if k[2] == 0:
            if k[1] > y:
                string += "\n" + v
                y += 1
            else:
                string += v
    print(string)
    print("\n")


def part1(g):
    grid = dict(g)
    for i in range(6):
        print_grid(grid)
        old_grid = grid.copy()
        for point in old_grid.keys():
            neighbor_points = neighbors(point[0], point[1], point[2])
            active_neighbors = sum(n == "#" for n in [old_grid.get(p, ".") for p in neighbor_points])
            if old_grid[point] == "#":
                if not (active_neighbors == 2 | active_neighbors == 3):
                    grid[point] = "."
            elif active_neighbors == 3:
                grid[point] = "#"
    print(sum(v == "#" for v in grid.values()))


part1(data)
