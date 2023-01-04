from typing import List


class SystemClock:
    def __init__(self, mode=0) -> None:
        self.mode = mode
        if mode == 0:
            self.interesting_record = []
            self.interesting_cycles = [x for x in range(20, 221, 40)]
            self.cycle = 1
        elif mode == 1:
            self.interesting_cycles = [x for x in range(40, 241, 40)]
            self.cycle = 0

    def next_pixel(self, reg_val):
        if abs(reg_val - ((self.cycle % 40) + 0)) <= 1:
            return "#"
        else:
            return "."

    def tick(self, reg_val, line_buff=""):
        self.cycle += 1
        if self.mode == 1:
            line_buff += self.next_pixel(reg_val)
            if self.cycle in self.interesting_cycles:
                print(line_buff)
                return ""
        else:
            if self.cycle in self.interesting_cycles:
                self.interesting_record.append(reg_val * self.cycle)
        return line_buff


def part_one(file_lines: List[str]) -> int:
    clock = SystemClock()
    reg_x = 1
    for args in [x.split() for x in file_lines]:
        clock.tick(reg_x)
        if len(args) > 1:
            reg_x += int(args[1])
            clock.tick(reg_x)
    return sum(clock.interesting_record)


def part_two(file_lines: List[str]) -> int:
    clock = SystemClock(mode=1)
    reg_x = 1
    line_buffer = ""
    for args in [x.split() for x in file_lines]:
        line_buffer = clock.tick(reg_x, line_buffer)
        if len(args) > 1:
            reg_x += int(args[1])
            line_buffer = clock.tick(reg_x, line_buffer)
    return 0
