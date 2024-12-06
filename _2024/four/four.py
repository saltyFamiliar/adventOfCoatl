from _2024 import utils as ut
from typing import Callable

lines = ut.get_lines("input.txt")
"""
S  S  S
 A A A
  MMM
SAMXMAS
  MMM
 A A A
S  S  S
"""


def search_spot(y: int, x: int, mat: ut.Matrix) -> int:
    def get_line(dir_func: Callable[[int,int], str], y: int, x: int, distance: int):
        line: str = ""
        for i in range(distance):
            line += dir_func(y)



    s = "XMAS"
    sr = "SAMX"
    total: int = 0
    total += ''.join(mat[y][x:x + 4]) == s
    total += ''.join(mat[y][x - 3:x + 1]) == sr
    if y >= 3:
        total += mat[y - 3][x] + mat[y - 2][x] + mat[y - 1][x] + mat[y][x] == sr
        if x >= 3:
            total += mat[y - 3][x - 3] + mat[y - 2][x - 2] + mat[y - 1][x - 1] + mat[y][x] == sr
        if x < len(mat[0]) - 3:
            total += mat[y - 3][x + 3] + mat[y - 2][x + 2] + mat[y - 1][x + 1] + mat[y][x] == sr

    if y < len(mat) - 3:
        total += mat[y][x] + mat[y + 1][x] + mat[y + 2][x] + mat[y + 3][x] == s
        if x >= 3:
            total += mat[y][x] + mat[y + 1][x - 1] + mat[y + 2][x - 2] + mat[y + 3][x - 3] == s
        if x < len(mat[0]) - 3:
            total += mat[y][x] + mat[y + 1][x + 1] + mat[y + 2][x + 2] + mat[y + 3][x + 3] == s
    return total


# M.S
# .A.
# M.S
def up_left(y: int, x: int, mat: ut.Matrix) -> bool:
    s = "MAS"; sr = "SAM"
    diag = ''.join(mat.UL_from(y, x) + mat[y][x] + mat.DR_from(y, x))
    return diag == s or diag == sr


def up_right(y: int, x: int, mat: ut.Matrix) -> bool:
    s = "MAS"; sr = "SAM"
    diag = ''.join(mat.UR_from(y, x) + mat[y][x] + mat.DL_from(y, x))
    return diag == s or diag == sr


# total = 0
# mat = [[x for x in l] for l in lines]
# for y in range(len(mat)):
#     for x in range(len(mat[0])):
#         if mat[y][x] == 'X':
#             total += search_spot(y, x, mat)
# print(total)
def get_from_mat(mat: list[list[str]], dir: tuple[int, int], center: tuple[int, int]) -> str:
    return mat[center[0] + dir[0]][center[1] + dir[1]]

total = 0
mat = ut.Matrix([[x for x in l] for l in lines])
for y in range(len(mat)):
    for x in range(len(mat[0])):
        if mat[y][x] == 'A':
            total += up_left(y, x, mat) and up_right(y, x, mat)
print(total)
