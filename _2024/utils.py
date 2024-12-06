def get_lines(file: str) -> list[str]:
    try:
        with open(file) as f:
            return [line.strip() for line in f.readlines()]
    except IOError:
        print("Error reading files")
        return []

class Matrix:
    def __init__(self, mat: list[list[str]]) -> None:
        self._mat: list[list[str]] = mat

    def __getitem__(self, idx: tuple[int, int]|int) -> str|list[str]:
        if isinstance(idx, int):
            return self._mat[idx]
        elif isinstance(idx, tuple):
            return self._mat[idx[0]][idx[1]]

    def __len__(self) -> int:
        return len(self._mat)

    def is_top_bound(self, y: int) -> bool:
        return y == 0

    def is_bot_bound(self, y: int) -> bool:
        return y == len(self._mat)-1

    def is_lft_bound(self, x: int) -> bool:
        return x == 0

    def is_rgt_bound(self, x: int) -> bool:
        return x == len(self._mat[0]) - 1

    def UL_from(self, y: int, x: int) -> str:
        if self.is_top_bound(y) or self.is_lft_bound(x): return ""
        return self._mat[y-1][x-1]

    def UR_from(self, y: int, x: int) -> str:
        if self.is_top_bound(y) or self.is_rgt_bound(x): return ""
        return self._mat[y-1][x+1]

    def UP_from(self, y: int, x: int) -> str:
        if self.is_top_bound(y): return ""
        return self._mat[y-1][x]

    def DL_from(self, y: int, x: int) -> str:
        if self.is_bot_bound(y) or self.is_lft_bound(x): return ""
        return self._mat[y+1][x-1]

    def DR_from(self, y: int, x: int) -> str:
        if self.is_bot_bound(y) or self.is_rgt_bound(x): return ""
        return self._mat[y+1][x+1]

    def DN_from(self, y: int, x: int) -> str:
        if self.is_bot_bound(y): return ""
        return self._mat[y+1][x]

    def L_from(self, y: int, x: int) -> str:
        if self.is_lft_bound(x): return ""
        return self._mat[y][x-1]

    def R_from(self, y: int, x: int) -> str:
        if self.is_rgt_bound(x): return ""
        return self._mat[y][x+1]
