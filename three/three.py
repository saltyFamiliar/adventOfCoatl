from typing import List


def priority(ch: str) -> int:
    if ch.islower():
        return ord(ch) - 96
    else:
        return ord(ch) - 38


def part_one(file_lines: List[str]) -> int:
    total_priority = 0
    for line in file_lines:
        line = line.strip()
        compartment_size = len(line) // 2
        sack_1, sack_2 = line[:compartment_size], line[compartment_size:]
        for item in sack_1:
            if item in sack_2:
                total_priority += priority(item)
                break

    return total_priority


def part_two(file_lines: List[str]) -> int:
    total_priority = 0
    group_sets = []
    for line in file_lines:
        line = line.strip()
        if len(group_sets) < 2:
            group_sets.append(line)
        else:
            for ch in line:
                if ch in group_sets[0] and ch in group_sets[1]:
                    total_priority += priority(ch)
                    group_sets = []
                    break

    return total_priority
