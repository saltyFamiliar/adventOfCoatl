from typing import List


def file_lines(file_path: str) -> List[str]:
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except IOError:
        print("Error getting file lines")
