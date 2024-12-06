from collections import defaultdict

from .. import utils as ut

lines = ut.get_lines("_2024/five/input.txt")
blank = lines.index("")
orders, updates = lines[:blank], lines[blank + 1:]

comes_after: dict[str, list[str]] = defaultdict(list)
comes_before: dict[str, list[str]] = defaultdict(list)
for bef, aft in [o.split("|") for o in orders]:
    comes_after[bef].append(aft)
    comes_before[aft].append(bef)

def order_is_good(line_updates: list[str]) -> bool:
    for i, u in enumerate(line_updates):
        bef, aft = line_updates[:i], line_updates[i + 1 :]
        if any(n in comes_after[u] for n in bef):
            return False
        if any(n in comes_before[u] for n in aft):
            return False
    return True

def insert_in_order(new_update: str, update_list: list[str]):
    for i, good_update in enumerate(update_list):
        if new_update in comes_before[good_update] \
        or good_update in comes_after[new_update]:
            update_list.insert(i, new_update)
            return
    update_list.append(new_update)

def make_good(line_updates: list[str]):
    good:list[str] = []
    for new_update in line_updates:
        insert_in_order(new_update, good)
    return good

part1 = part2 = 0
for update_line in [x.split(",") for x in updates]:
    if order_is_good(update_line):
        part1 += int(update_line[len(update_line) // 2])
    else:
        good = make_good(update_line)
        part2 += int(good[len(good) // 2])

print(part1)
print(part2)
