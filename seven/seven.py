from typing import List


def change_dir(cwd: list[str], opt) -> str:
    if opt == "..":
        cwd.pop()
    else:
        cwd.append(opt)
    return ''.join(cwd)


def get_dir_sizes(lines: List[str]) -> dict[str, int]:
    dir_sizes = {}
    cwd, cwd_path = [], ""
    files_checked = []
    for tokens in [x.split() for x in lines]:
        if tokens[0] == "$":
            if len(tokens) < 3:
                continue
            _, cmd, opt = tokens
            if cmd == "cd":
                cwd_path = change_dir(cwd, opt)
                if opt != ".." and cwd_path not in dir_sizes.keys():
                    dir_sizes[cwd_path] = 0
        elif tokens[0].isnumeric():
            size, filename = tokens
            if cwd_path + filename not in files_checked:
                for i in range(len(cwd)):
                    dir_sizes[''.join(cwd[:i + 1])] += int(size)
                files_checked.append(cwd_path + filename)
    return dir_sizes


def part_one(file_lines: List[str]) -> int:
    dir_sizes = get_dir_sizes(file_lines)
    size_limit = 100000
    total = 0
    for size in dir_sizes.values():
        if size <= size_limit:
            total += size
    return total


def part_two(file_lines: List[str]) -> int:
    dir_sizes = get_dir_sizes(file_lines)
    disk_space = 70000000
    space_needed = 30000000

    total_used = dir_sizes["/"]
    free_space = disk_space - total_used
    for size in sorted(dir_sizes.values()):
        if free_space + size >= space_needed:
            return size
