from typing import List


def to_next_unique(line, window_offset, window_size):
    window = line[window_offset:window_offset + window_size]
    while not all(window.count(x) == 1 for x in window):
        window = window[1:] + line[window_offset + window_size]
        window_offset += 1
    return window_offset, window


def find_unique_window_index(size: int, line: str) -> int:
    window_offset, window = to_next_unique(line, 0, size)
    while window_offset < len(line):
        ch = line[window_offset + size]
        if ch not in window:
            return window_offset + size + 1
        else:
            window_offset, window = to_next_unique(line, window_offset + 1, size)


def part_one(file_lines: List[str]) -> int:
    return find_unique_window_index(3, file_lines[0])


def part_two(file_lines: List[str]) -> int:
    return find_unique_window_index(13, file_lines[0])
