from typing import List


def convert_choice(choice: str) -> str:
    if ord(choice) > 65 + 2:
        return chr(ord(choice) - 23)
    else:
        return chr(ord(choice) + 23)


def get_score(choice: str) -> int:
    return ord(choice) - 64


def get_beater(loser: str) -> str:
    return chr(((ord(loser) - 65 + 1) % 3) + 65)


def get_loser(winner: str) -> str:
    return chr(((ord(winner) - 65 - 1) % 3) + 65)


def part_one(file_lines: List[str]) -> int:
    score = 0
    for line in file_lines:
        (opp, me) = line.strip().split()
        me = convert_choice(me)
        score += get_score(me)
        if opp == me:
            score += 3
        elif me == get_beater(opp):
            score += 6

    return score


def part_two(file_lines: List[str]) -> int:
    score = 0
    for line in file_lines:
        (opp, result) = line.strip().split()
        if result == "X":
            score += get_score(get_loser(opp))
        elif result == "Y":
            score += get_score(opp) + 3
        else:
            score += get_score(get_beater(opp)) + 6

    return score
