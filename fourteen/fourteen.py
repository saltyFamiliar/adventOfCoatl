from typing import List

from point import Pt
from printing import fprinter

p = fprinter("fourteen/output.txt")
sand_entry = Pt(500, 0)


class Sand:
    def __init__(self, pos: Pt, cave_ref: List[List], offset) -> None:
        self.pos = pos
        self.cave = cave_ref
        self.offset = offset

    def rel_x(self):
        return self.pos.x - self.offset

    def fall(self) -> bool:
        self.cave[self.pos.y][self.rel_x()] = '.'
        try:
            if self.cave[self.pos.y + 1][self.rel_x()] != '.':
                if self.cave[self.pos.y + 1][self.rel_x() - 1] == '.':
                    self.pos.x -= 1
                else:
                    self.pos.x += 1

            self.pos.y += 1
            self.cave[self.pos.y][self.rel_x()] = '*'
            # sand went out of bounds
            return (
                    self.pos.y >= len(self.cave) or
                    self.rel_x() <= 0 or
                    self.rel_x() >= len(self.cave[0]))
        except:
            return True

    def can_fall(self):
        try:
            return '.' in self.cave[self.pos.y + 1][self.rel_x() - 1: self.rel_x() + 2]
        except:
            return True


def show_cave(cave: List[List], left, right, width):
    def row_padding(i):
        max_y = len(cave)
        return f"{(len(str(max_y)) - len(i)) * ' '} "

    # show col labels
    label_digits = ""
    for i in range(len(str(right))):
        label_digits += row_padding('')
        label_digits += ' '.join([str(x)[i] for x in range(left, left + width)]) + '\n'

    # show cave and row labels
    cave_str = ""
    for i, row in enumerate(cave):
        cave_str += f"{i}{row_padding(str(i))}{' '.join(row)}\n"

    p.clear_file()
    p.put(label_digits.rstrip())
    p.put(cave_str)


def build_cave(val_lines: List[List[str]], left, right, bottom, add_floor: bool = False) -> List[List[str]]:
    if add_floor:
        width = right - left
        height = bottom + 2
    else:
        width, height = (right - left) + 1, bottom + 1
    cave: List[List[str]] = [['.' for _ in range(width)] for _ in range(height)]
    if add_floor:
        cave.append(['#' for _ in range(width)])
    cave[sand_entry.y][sand_entry.x - left] = '+'

    for line in val_lines:
        cursor = Pt(*list(map(int, line.pop(0).split(","))))
        for val in line:
            x, y = list(map(int, val.split(",")))
            if cursor.x != x:
                start = min(cursor.x, x) - left
                for i in range(start, start + abs(cursor.x - x) + 1):
                    cave[y][i] = '#'
            elif cursor.y != y:
                start = min(cursor.y, y)
                for i in range(start, start + abs(cursor.y - y)):
                    cave[i][x - left] = '#'
            cursor = Pt(x, y)
    return cave


def fill_cave(cave: List[List[str]], left: int, skip_to: int = 0) -> int:
    exit_reached = False
    sand_count = 0

    while not exit_reached:
        sand = Sand(Pt(sand_entry.x, sand_entry.y), cave, left)
        sand_count += 1
        # print(f"{sand_count=}")
        while sand.can_fall():
            exit_reached = sand.fall()
            if exit_reached:
                break
            # if sand_count >= skip_to:
            #     show_cave(cave, left, right, width)
            #     sleep(0.05)
        if cave[sand_entry.y + 1][(sand_entry.x + 1) - left] == '*':
            exit_reached = True
    return sand_count + 1


def part_one(file_lines: List[str]) -> int:
    # find cave dimensions
    left, right, bottom = 1000, 0, 0
    val_lines: List[List[str]] = [line.split(" -> ") for line in file_lines]

    for line in val_lines:
        for val in line:
            x, y = list(map(int, val.split(",")))
            left = min(x, left)
            right = max(x, right)
            bottom = max(y, bottom)

    cave: List[List[str]] = build_cave(val_lines, left, right, bottom)
    return fill_cave(cave, left) - 2


def part_two(file_lines: List[str]) -> int:
    # find cave dimensions
    left, right, bottom = 1000, 0, 0
    val_lines = [line.split(" -> ") for line in file_lines]

    for line in val_lines:
        for val in line:
            x, y = list(map(int, val.split(",")))
            left = min(x, left)
            right = max(x, right)
            bottom = max(y, bottom)
    height = bottom + 2
    left -= height
    right += height

    cave: List[List[str]] = build_cave(val_lines, left, right, bottom, add_floor=True)
    return fill_cave(cave, left)
