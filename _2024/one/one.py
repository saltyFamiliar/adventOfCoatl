from collections import Counter

from _2024 import utils

lines = utils.get_lines("input.txt")
ls = []
rs = []
for line in lines:
    l, r = line.split()
    ls.append(int(l))
    rs.append(int(r))

ls.sort()
rs.sort()
rsc = Counter(rs)

total = 0
for n in ls:
    if n not in rsc:
        continue
    total += n * rsc[n]

# for l, r in zip(ls, rs):
#     total += abs(int(l) - int(r))
#

print(total)
