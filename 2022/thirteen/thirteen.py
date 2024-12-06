from ast import literal_eval
from functools import cmp_to_key
from typing import List, Tuple

from printing import fprinter

p = fprinter("thirteen/output.txt")


def to_list(var) -> List:
    if isinstance(var, list):
        return var
    else:
        return [var]


def compare(a: List, b: List, depth: int = 1, verbose=False) -> int:
    for a_item, b_item in zip(a, b):
        if verbose:
            p.put(f"{depth * '  '}- Compare {a_item} vs {b_item}")
        if isinstance(a_item, list) or isinstance(b_item, list):
            result = compare(to_list(a_item), to_list(b_item), depth + 1)
            if result == 0:
                continue
            else:
                return result
        elif a_item == b_item:
            continue
        else:
            return 1 if a_item < b_item else -1

    if len(a) == len(b):
        return 0

    return 1 if len(a) < len(b) else -1


def part_one(file_lines: List[str]) -> int:
    pairs: List[Tuple[List, List]] = []

    lines = iter(file_lines)
    while True:
        left = literal_eval(next(lines))
        right = literal_eval(next(lines))
        pairs.append((left, right))
        try:
            next(lines)
        except StopIteration:
            break

    good_indices = []
    for i, (left, right) in enumerate(pairs):
        p.put(f"== Pair {i + 1} ==")
        p.put(f"- Compare {left} vs {right}")
        is_good = compare(left, right, verbose=True)
        if is_good == 1:
            good_indices.append(i + 1)
        p.put(f"{is_good}\n")

    return sum(good_indices)


def part_two(file_lines: List[str]) -> int:
    dividers = [[[2]], [[6]]]
    packets: List[List] = dividers.copy()
    for line in file_lines:
        if len(line) < 2:
            continue
        packet = literal_eval(line)
        packets.append(packet)

    packets.sort(key=cmp_to_key(compare), reverse=True)

    for packet in packets:
        p.put(packet)

    decoder_key = 1
    for i, packet in enumerate(packets):
        if packet in dividers:
            decoder_key *= (i + 1)

    return decoder_key
