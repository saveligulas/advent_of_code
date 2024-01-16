from FileReader import read_line_with_spaces
import sys


sys.setrecursionlimit(10000)


mazetxt = read_line_with_spaces("./input/test_input.txt")


maze = []
for i in range(len(mazetxt)):
    maze.append([])
    for letter in mazetxt[i]:
        maze[i].append(letter)


def check_square_is_accessible(tuple_xy, maze_c):
    if maze_c[tuple_xy[1]][tuple_xy[0]] == "#":
        return False
    return True


def get_up(tuple_xy):
    return tuple_xy[0], tuple_xy[1] + 1


def get_down(tuple_xy):
    return tuple_xy[0], tuple_xy[1] - 1


def get_right(tuple_xy):
    return tuple_xy[0] + 1, tuple_xy[1]


def get_dir_from_int(i, tuple_xy):
    if i == 0:
        return get_down(tuple_xy)
    if i == 1:
        return get_right(tuple_xy)
    if i == 2:
        return get_up(tuple_xy)
    if i == 3:
        return get_left(tuple_xy)


def get_left(tuple_xy):
    return tuple_xy[0] - 1, tuple_xy[1]


def get_start():
    for i in range(len(maze)):
        if maze[i][0] == " ":
            return 1, i
    return None


def get_possible_directions(tuple_xy, maze_c):
    drul_directions_possible = []

    if check_square_is_accessible(get_down(tuple_xy), maze_c):
        drul_directions_possible.append(1)
    else:
        drul_directions_possible.append(0)
    if check_square_is_accessible(get_right(tuple_xy), maze_c):
        drul_directions_possible.append(1)
    else:
        drul_directions_possible.append(0)
    if check_square_is_accessible(get_up(tuple_xy), maze_c):
        drul_directions_possible.append(1)
    else:
        drul_directions_possible.append(0)
    if check_square_is_accessible(get_left(tuple_xy), maze_c):
        drul_directions_possible.append(1)
    else:
        drul_directions_possible.append(0)
    return drul_directions_possible


def solve():
    start = get_start()
    maze_copy = maze.copy()
    path = find_way_v2((start[0] - 1, start[1]), start, maze_copy)
    for line in maze_copy:
        print(line)
    return path


def get_first_possible_direction(drul):
    for i in range(len(drul)):
        if drul[i] == 1:
            return i


def get_next_possible_direction(drul, count):
    counter = 0
    for i in range(len(drul)):
        if drul[i] == 1:
            counter += 1
            if counter == count:
                return i


def find_way_v2(prev_tuple_xy, tuple_xy, maze_c, path=[]):
    prev = tuple_xy
    if not path:
        maze_c[prev_tuple_xy[1]][prev_tuple_xy[0]] = "#"
    path.append(tuple_xy)
    if maze_c[tuple_xy[1]][tuple_xy[0]] == "e":
        return path
    drul_directions_possible = get_possible_directions(tuple_xy, maze_c)
    if sum(drul_directions_possible) == 0:
        return maze_c
    i = get_first_possible_direction(drul_directions_possible)
    if prev_tuple_xy == get_dir_from_int(i, tuple_xy):
        if sum(drul_directions_possible) == 1:
            maze_c[tuple_xy[1]][tuple_xy[0]] = "#"
            path.pop(-1)
            prev = path[-1]
        else:
            i = get_next_possible_direction(drul_directions_possible, 2)
    return find_way_v2(prev, get_dir_from_int(i, tuple_xy), maze_c, path)


def is_dead_end(prev, current, dir):
    if prev == get_dir_from_int(dir, current):
        return True
    return False


print(solve())