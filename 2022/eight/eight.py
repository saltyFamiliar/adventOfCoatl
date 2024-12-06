from typing import List


def get_scenic_value(grid, row_num, col_num):
    if row_num == 0 or col_num == 0:
        return 0
    scenic_value = 1
    tree_height = grid[row_num][col_num]

    # From North
    north_vision = 0
    for i in reversed(range(row_num)):
        north_vision += 1
        if grid[i][col_num] >= tree_height:
            break
    scenic_value *= north_vision

    # From South
    south_vision = 0
    for i in range(row_num + 1, len(grid)):
        south_vision += 1
        if grid[i][col_num] >= tree_height:
            break
    scenic_value *= south_vision

    # From East
    east_vision = 0
    for i in reversed(range(col_num)):
        east_vision += 1
        if grid[row_num][i] >= tree_height:
            break
    scenic_value *= east_vision

    # From West
    west_vision = 0
    for i in range(col_num + 1, len(grid[0])):
        west_vision += 1
        if grid[row_num][i] >= tree_height:
            break

    return scenic_value * west_vision


def is_visible(grid, row_num, col_num):
    tree_height = grid[row_num][col_num]

    # From North
    for i in range(row_num):
        if grid[i][col_num] >= tree_height:
            break
    else:
        return True

    # From South
    for i in range(row_num + 1, len(grid)):
        if grid[i][col_num] >= tree_height:
            break
    else:
        return True

    # From East
    for i in range(col_num):
        if grid[row_num][i] >= tree_height:
            break
    else:
        return True

    # From West
    for i in range(col_num + 1, len(grid[0])):
        if grid[row_num][i] >= tree_height:
            return False
    return True


def part_one(file_lines: List[str]) -> int:
    forest = [list(map(int, list(line))) for line in file_lines]
    visible_trees = 0

    for row_num, row in enumerate(forest):
        for col_num, _ in enumerate(row):
            visible_trees += is_visible(forest, row_num, col_num)

    return visible_trees


def part_two(file_lines: List[str]) -> int:
    forest = [list(map(int, list(line))) for line in file_lines]
    max_scenic = 0

    for row_num, row in enumerate(forest):
        for col_num, _ in enumerate(row):
            new_scenic_value = get_scenic_value(forest, row_num, col_num)
            max_scenic = max(max_scenic, new_scenic_value)

    return max_scenic
