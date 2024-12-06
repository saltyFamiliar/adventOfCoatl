from typing import List

from tqdm import trange

from point import Pt


# p = fprinter("fifteen/output.txt")


class Beacon(Pt):
    def __init__(self, location: Pt) -> None:
        self.location = location

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location: Pt):
        self.x = location.x
        self.y = location.y
        self._location = location


class Sensor(Pt):
    def __init__(self, location, beacon: Beacon | None = None) -> None:
        self.location = location
        if beacon is None:
            self.beacon = Beacon(location)
        else:
            self.beacon = beacon

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location: Pt):
        self.x = location.x
        self.y = location.y
        self._location = location

    def beacon_dist(self):
        return self.dist_to(self.beacon.location)

    def dist_to(self, p: Pt):
        return abs(self.x - p.x) + abs(self.y - p.y)

    def can_see(self, p: Pt):
        return self.dist_to(p) <= self.beacon_dist()

    def edge_col_at_row(self, row):
        return (self.beacon_dist() - abs(self.y - row)) + self.x

    def report(self):
        print("--------------------------")
        print(f"Sensor: {self.x}, {self.y}")
        print(f"Beacon: {self.beacon.x}, {self.beacon.y}")


# prints sensor_map to file. Uses absolute boundaries for labels
def show_map(sensor_map: List[List], left, right, top, bottom):
    len_str = lambda x: len(str(x))

    # generate column labels string
    label_str = ""
    for row in range(len_str(right)):
        label_digits = []
        label_padding = " " * (len_str(bottom) + 1)

        for col in range(left, right + 1):
            if len_str(col) <= row:
                label_digits.append(' ')
            else:
                label_digits.append(str(col)[row])

        label_str += f"{label_padding}{' '.join(label_digits)}\n"

    # generate rows of cave along with row labels
    sensor_map_str = ""
    for i, row in enumerate(sensor_map):
        label_padding = ' ' * (len_str(bottom) - len_str(i) + 1)
        sensor_map_str += f"{i + top}{label_padding}{' '.join(row)}\n"

    p.clear_file()
    p.put(label_str.rstrip())
    p.put(sensor_map_str)


# returns first contiguous number in str
def find_num(num_str: str) -> int:
    num = ""
    for c in num_str:
        if c.isnumeric() or c == '-':
            num += c
    return int(num)


# generates sensor list from line strings iterable
def find_sensors(line_iter) -> List[Sensor]:
    sensors = []
    for sensor_str, beacon_str in map(lambda x: x.split(':'), line_iter):
        sensor_pt = Pt(*list(map(find_num, sensor_str.split()[2:])))
        beacon_pt = Pt(*list(map(find_num, beacon_str.split()[4:])))
        sensors.append(Sensor(sensor_pt, Beacon(beacon_pt)))

    return sensors


def part_one(file_lines: List[str]) -> int:
    sensors: List[Sensor] = find_sensors(file_lines)

    # get map dimensions from sensor and beacon positions
    left = min([sensor.x - sensor.beacon_dist() for sensor in sensors])
    top = min([sensor.y - sensor.beacon_dist() for sensor in sensors])
    right = max([sensor.x + sensor.beacon_dist() for sensor in sensors])
    bottom = max([sensor.y + sensor.beacon_dist() for sensor in sensors])

    # set sensor/beacon offset
    for sensor in sensors:
        # sensor.report()
        sensor.x_offset = sensor.beacon.x_offset = left
        sensor.y_offset = sensor.beacon.y_offset = top

    # example needs to check different row than real input
    if bottom > 2_000_000 > top:
        row_to_check = 2_000_000
    else:
        row_to_check = 10

    # calculate number of visible cells in row
    cols_in_row = range(left, right + 1)
    visible_cells = 0
    for col in cols_in_row:
        for sensor in sensors:
            if sensor.can_see(Pt(col, row_to_check)):
                visible_cells += 1
                break

    # remove any cells that contain beacon from count
    cols_to_remove = set()
    for sensor in sensors:
        if sensor.beacon.y == row_to_check:
            cols_to_remove.add(sensor.beacon.x)

    return visible_cells - len(cols_to_remove)


def part_two(file_lines: List[str]) -> int:
    sensors: List[Sensor] = find_sensors(file_lines)

    # search parameters are different for example and for real input
    bottom = max([sensor.y + sensor.beacon_dist() for sensor in sensors])
    left = top = 0
    if bottom < 4_000_000:
        right = bottom = 20
    else:
        right = bottom = 4_000_000

    for row in trange(top, bottom + 1):
        col = left
        while col <= right:
            cell = Pt(col, row)
            for sensor in sensors:
                if sensor.can_see(cell):
                    col = sensor.edge_col_at_row(row) + 1
                    break
            else:
                return (col * 4_000_000) + row
