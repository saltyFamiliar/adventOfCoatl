import re

from _2024 import utils as ut

lines: list[str] = ut.get_lines("_2024/three/input.txt")

able = True
part1 = part2 = 0
for l in lines:
    m: str
    for m in  re.findall(r"mul\(\d+,\d+\)|don\'t\(\)|do\(\)", l):
        if m == "do()":
            able = True; continue
        if m == "don\'t()":
            able = False; continue
        a: int; b: int;
        (a, b) = eval(m[3:])
        part1 += a*b
        if able: part2 += a*b

print("silver: ", part1)
print("gold: ", part2)
