from typing import List


class Coordinate:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def update(self, adjustments):
        self.x += adjustments[0]
        self.y += adjustments[1]

    def coords(self):
        return self.x, self.y

    def is_touching(self, other):
        return abs(self.x - other.x) < 2 and abs(self.y - other.y) < 2

    def is_identical(self, other):
        return self.x == other.x and self.y == other.y


def parse_direction(direction_char, dist):
    if direction_char == "U":
        return 0, dist
    elif direction_char == "D":
        return 0, -dist
    elif direction_char == "R":
        return dist, 0
    elif direction_char == "L":
        return -dist, 0
    else:
        return 0, 0


def show_positions(knots, max_x=6, max_y=5):
    with open("nine/output.txt", 'a') as f:
        for y in reversed(range(max_y)):
            for x in range(max_x):
                ch = "."
                for i, k in enumerate(knots):
                    if k.is_identical(Coordinate(x, y)):
                        ch = str(i)
                        break
                f.write(ch)
            f.write("\n")
        f.write("\n")


def next_knot_direction(knot, next_knot):
    y_dif = knot.y - next_knot.y
    x_dif = knot.x - next_knot.x
    if y_dif != 0:
        y_adjust = 1 if y_dif < 0 else -1
    else:
        y_adjust = 0

    if x_dif != 0:
        x_adjust = 1 if x_dif < 0 else -1
    else:
        x_adjust = 0
    return x_adjust, y_adjust


def part_one(file_lines: List[str]) -> int:
    tail, head = Coordinate(), Coordinate()
    tail_history = set()
    tail_history.add(tail.coords())

    for direction, dist in [x.split() for x in file_lines]:
        for _ in range(int(dist)):
            pos_adjustment = parse_direction(direction, 1)
            head.update(pos_adjustment)
            if not head.is_touching(tail):
                tail.update(pos_adjustment)
                if tail.x != head.x and tail.y != head.y:
                    if direction == "U" or direction == "D":
                        adjustments = (1 if tail.x < head.x else -1, 0)
                    else:
                        adjustments = (0, 1 if tail.y < head.y else -1)
                    tail.update(adjustments)
                tail_history.add(tail.coords())

    return len(tail_history)


def part_two(file_lines: List[str]) -> int:
    knots = [Coordinate(11, 5) for _ in range(10)]
    head = knots[0]
    tail_history = set()
    tail_history.add(knots[-1].coords())

    # with open("nine/output.txt", "w"):
    #    pass
    # show_positions(knots, 26, 21)

    for direction, dist in [x.split() for x in file_lines]:
        # with open("nine/output.txt", "a") as of:
        #    of.write(f"\n== {direction} {dist} ==\n\n")

        for _ in range(int(dist)):
            head.update(parse_direction(direction, 1))
            for next_knot_idx, knot in enumerate(knots[1:]):
                next_knot = knots[next_knot_idx]
                if not knot.is_touching(next_knot):
                    knot.update(next_knot_direction(knot, next_knot))
                    tail_history.add(knots[-1].coords())
            # show_positions(knots, 26, 21)

    return len(tail_history)
