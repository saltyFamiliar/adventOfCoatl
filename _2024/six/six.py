from _2024 import utils as ut
import time
import os

lines: list[str] = ut.get_lines("_2024/six/input.txt")
mat: list[list[list[str]]] = [[[x] for x in line] for line in lines]

nxt_chr = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
chr_dir = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

cur_pos: list[int] = []
for y, line in enumerate(mat):
    if ['^'] in line:
        cur_pos = [y, line.index(['^'])]; break
assert(cur_pos)
mat[cur_pos[0]][cur_pos[1]].insert(0, ' ')

def next_pos(y: int, x: int) -> tuple[int,int]|None:
    cur_chr = mat[y][x][-1]
    dy, dx = chr_dir[cur_chr]
    if not 0 <= y + dy < len(mat): return None
    if not 0 <= x + dx < len(mat[0]): return None
    return (y + dy, x + dx)

def advance(y: int, x: int, virtual:bool=False) -> list[int]:
    cur_chr = mat[y][x][-1]
    assert(cur_chr not in ['.', ' ', '#'])
    assert((nxt := next_pos(y, x)) is not None)
    _ = mat[y][x].pop()
    if not virtual:
        if mat[y][x][-1] == '.':
            mat[y][x][-1] = ' '
    mat[nxt[0]][nxt[1]].append(cur_chr)
    return [nxt[0], nxt[1]]

def rotate_full(y: int, x: int) -> bool:
    while (nxt := next_pos(y, x)) is not None and mat[nxt[0]][nxt[1]][-1] == '#':
        time.sleep(slp_dur)
        cur_chr = rotate(y, x)
        mat[y][x][-1] = cur_chr
        print_mat()
    return nxt is None

def rotate(y: int, x: int) -> str:
    assert(mat[y][x][-1] not in ['.', ' ', '#'])
    return nxt_chr[mat[y][x][-1]]

def print_mat():
    _ = os.system("clear")
    for y, l in enumerate(mat): 
        if abs(cur_pos[0] - y) < 38: 
            print(''.join(d[-1] for d in l))

block_loc: tuple[int, int]|None = None
def toggle_block(y: int, x: int):
     global block_loc
     if block_loc is None:
         block_loc = (y, x)
         mat[y][x].append('#')
     else:
         _ = mat[block_loc[0]][block_loc[1]].pop()
         block_loc = None

def check_for_loop(y: int, x: int) -> bool:
    if rotate_full(y, x): return False
    mat[y][x].append(mat[y][x][-1])
    fast = advance(y, x, virtual=True)
    out = False
    while True:
        if rotate_full(fast[0], fast[1]): 
            out=False; break
        fast = advance(fast[0], fast[1], virtual=True)
        if rotate_full(y, x):
            out=False; break
        y, x = advance(y, x, virtual=True)
        if rotate_full(fast[0], fast[1]):
            out=False; break
        fast = advance(fast[0], fast[1], virtual=True)
        time.sleep(slp_dur)
        print_mat()
        if mat[fast[0]][fast[1]] == mat[y][x] and fast[0] == y and fast[1] == x: 
            out=True; break
    _ = mat[fast[0]][fast[1]].pop()
    _ = mat[y][x].pop()
    return out

visited = 1
possible_loops = 0
fps = 15
slp_dur = 1/fps
while True:
    time.sleep(slp_dur)
    print_mat()
    y, x = cur_pos
    nxt = next_pos(y, x)
    if nxt is None: 
        print("A")
        break
    toggle_block(nxt[0], nxt[1])
    if check_for_loop(y, x): possible_loops+=1
    y, x = cur_pos
    toggle_block(nxt[0], nxt[1])
    if rotate_full(y, x): 
        print("b")
        break
    nxt = next_pos(y, x)
    if nxt is None:
        print("C")
        break
    if mat[nxt[0]][nxt[1]][-1] == '.': visited+=1

    cur_pos = advance(y, x)

print("visited: ", visited)
