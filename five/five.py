from typing import List, Tuple


def parse_instruction(line: str) -> Tuple[int, int, int]:
    line = line.strip().split()
    return int(line[1]), int(line[3]), int(line[5])


def build_dockyard(line: str, dockyard: List[List], stack_map: dict[int, int]) -> None:
    for i, ch in enumerate(line):
        if ch.isalpha():
            if i not in stack_map:
                stack_map[i] = (i // 4) + 1
            dockyard[stack_map[i]].insert(0, ch)


def move_cargo(dockyard: List[List[str]], instruction: str, reverse_stack: bool = False) -> None:
    amount, from_, to = parse_instruction(instruction)
    if reverse_stack:
        dockyard[to].extend(dockyard[from_][-amount:][::-1])
    else:
        dockyard[to].extend(dockyard[from_][-amount:])

    dockyard[from_] = dockyard[from_][:-amount]


def part_one(file_lines: List[str]) -> str:
    # extra empty list because puzzle input stacks are 1-indexed
    stack_map: dict[int] = {}
    dockyard: List[List[str]] = [[] for x in range(10)]
    for line in file_lines:
        if line[0] == 'm':
            move_cargo(dockyard, line, True)
        else:
            build_dockyard(line, dockyard, stack_map)

    return ''.join([stack[-1] for stack in dockyard if stack])


def part_two(file_lines: List[str]) -> str:
    # extra empty list because puzzle input stacks are 1-indexed
    stack_map: dict[int, int] = {}
    dockyard: List[List[str]] = [[] for x in range(10)]
    for line in file_lines:
        if line[0] == 'm':
            move_cargo(dockyard, line, False)
        else:
            build_dockyard(line, dockyard, stack_map)

    return ''.join([stack[-1] for stack in dockyard if stack])
