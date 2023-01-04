from typing import List


class Tile:
    def __init__(self, ch, occupant='') -> None:
        self.ch = ch
        self.height = ord(ch)
        self.occupant = occupant
        self.min_steps = float("inf")

    def face(self) -> str:
        face_ch = self.occupant if self.occupant else self.ch
        steps_face = '.' if self.min_steps == float("inf") else self.min_steps
        return f"|{face_ch}:{'.' * (3 - len(str(steps_face)))}{steps_face}|"


def is_valid_move(start_height: int, end_height: int):
    return start_height + 1 >= end_height


def part_one(file_lines: List[str]) -> int:
    height_map: List[List[Tile]] = []
    end_tile: Tile = Tile('z', occupant='E')
    for line in file_lines:
        height_row = []
        for ch in line:
            if ch == 'S':
                new_tile = Tile('a', occupant='S')
                new_tile.min_steps = 0
            elif ch == 'E':
                new_tile = end_tile
            else:
                new_tile = Tile(ch)
            height_row.append(new_tile)
        height_map.append(height_row)
    map_width, map_height = len(height_map[0]), len(height_map)

    while end_tile.min_steps == float("inf"):
        for y, row in enumerate(height_map):
            for x, tile in enumerate(row):
                if x > 0 and is_valid_move(tile.height, row[x - 1].height):
                    row[x - 1].min_steps = min(tile.min_steps + 1, row[x - 1].min_steps)
                if x < map_width - 1 and is_valid_move(tile.height, row[x + 1].height):
                    row[x + 1].min_steps = min(tile.min_steps + 1, row[x + 1].min_steps)
                if y > 0 and is_valid_move(tile.height, height_map[y - 1][x].height):
                    height_map[y - 1][x].min_steps = min(tile.min_steps + 1, height_map[y - 1][x].min_steps)
                if y < map_height - 1 and is_valid_move(tile.height, height_map[y + 1][x].height):
                    height_map[y + 1][x].min_steps = min(tile.min_steps + 1, height_map[y + 1][x].min_steps)

    # for row in height_map:
    #     for t in row:
    #         print(t.face(), end='')
    #     print()

    return end_tile.min_steps


def part_two(file_lines: List[str]) -> int:
    height_map: List[List[Tile]] = []
    end_tile: Tile = Tile('z', occupant='E')
    for line in file_lines:
        height_row = []
        for ch in line:
            if ch == 'S' or ch == 'a':
                new_tile = Tile('a', occupant='S')
                new_tile.min_steps = 0
            elif ch == 'E':
                new_tile = end_tile
            else:
                new_tile = Tile(ch)
            height_row.append(new_tile)
        height_map.append(height_row)
    map_width, map_height = len(height_map[0]), len(height_map)

    map_changed = True
    while map_changed:
        map_changed = False
        for y, row in enumerate(height_map):
            for x, tile in enumerate(row):
                from_tile: int | float = tile.min_steps + 1
                if x > 0:
                    left = row[x - 1]
                    if is_valid_move(tile.height, left.height) and left.min_steps > from_tile:
                        left.min_steps = from_tile
                        map_changed = True
                if x < map_width - 1:
                    right = row[x + 1]
                    if is_valid_move(tile.height, right.height) and right.min_steps > from_tile:
                        right.min_steps = from_tile
                        map_changed = True
                if y > 0:
                    up = height_map[y - 1][x]
                    if is_valid_move(tile.height, up.height) and up.min_steps > from_tile:
                        up.min_steps = from_tile
                        map_changed = True
                if y < map_height - 1:
                    down = height_map[y + 1][x]
                    if is_valid_move(tile.height, down.height) and down.min_steps > from_tile:
                        down.min_steps = from_tile
                        map_changed = True

    # for row in height_map:
    #     for t in row:
    #         print(t.face(), end='')
    #     print()

    return end_tile.min_steps
