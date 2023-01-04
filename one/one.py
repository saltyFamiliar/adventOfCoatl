from typing import List


def in_top_three(top_three: list[int], new_term: int) -> list[int]:
    top_three.sort()
    if top_three[0] < new_term:
        top_three[0] = new_term
    return top_three


def part_one(file_lines: List[str]) -> int:
    max_cal: int = 0
    current_bunch: int = 0
    for line in file_lines:
        if len(line) < 2:
            max_cal = max(current_bunch, max_cal)
            current_bunch = 0
        else:
            current_bunch += int(line)

    max_cal = max(current_bunch, max_cal)
    return max_cal


def part_two(file_lines: List[str]) -> int:
    max_cal: List[int] = [0, 0, 0]
    current_bunch: int = 0
    for line in file_lines:
        if len(line) < 2:
            max_cal = in_top_three(max_cal, current_bunch)
            current_bunch = 0
        else:
            current_bunch += int(line)

    max_cal = in_top_three(max_cal, current_bunch)
    return sum(max_cal)
