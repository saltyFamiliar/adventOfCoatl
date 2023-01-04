class Pt:
    def __init__(self, x, y, x_offset=0, y_offset=0) -> None:
        self.x = x
        self.y = y
        self.x_offset = x_offset
        self.y_offset = y_offset

    def rel_x(self):
        return self.x - self.x_offset

    def rel_y(self):
        return self.y - self.y_offset
