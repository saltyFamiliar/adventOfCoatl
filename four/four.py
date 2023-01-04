from typing import List, Tuple


def split_ranges(line: str) -> Tuple[List[str], List[str]]:
    one, two = line.strip().split(",")
    one, two = one.split("-"), two.split("-")
    one, two = list(map(int, one)), list(map(int, two))
    return one, two


def part_one(file_lines: List[str]) -> int:
    total_overlap = 0
    for line in file_lines:
        one, two = split_ranges(line)
        if one[0] >= two[0] and one[1] <= two[1]:
            total_overlap += 1
        elif one[0] <= two[0] and one[1] >= two[1]:
            total_overlap += 1

    return total_overlap


def part_two(file_lines: List[str]) -> int:
    total_overlap = 0
    for line in file_lines:
        one, two = split_ranges(line)
        if (two[0] <= one[0] <= two[1] or
                one[0] <= two[0] <= one[1] or
                two[0] <= one[1] <= two[1] or
                one[0] <= two[1] <= one[1]):
            total_overlap += 1

    return total_overlap
