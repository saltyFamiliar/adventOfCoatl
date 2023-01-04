class fprinter:
    def __init__(self, filename) -> None:
        self.f = filename
        self.clear_file()

    def clear_file(self):
        open(self.f, "w").close()

    def put(self, s):
        with open(self.f, "a") as fp:
            fp.write(f"{s}\n")

    def put_top(self, s):
        with open(self.f, "r+") as f:
            content = f.read()
            f.seek(0, 0)
            f.write(f"{s}\n{content}")
