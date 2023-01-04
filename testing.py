import time
from functools import wraps
from typing import Callable

from colorama import Fore

import io_utils


def test_part(part_func: Callable, file_dir: str, wanted: int | str) -> bool:
    test_lines = io_utils.file_lines(f"{file_dir}/test.txt")
    if not test_lines:
        print("test.txt may be empty")
        return False
    real_lines = io_utils.file_lines(f"{file_dir}/input.txt")
    if not real_lines:
        print("input.txt may be empty")
        return False

    test_result = part_func(test_lines)
    if test_result == wanted:
        print(Fore.GREEN + "Test passed with result: " + Fore.RESET, test_result)
        print(f"Final result: ", part_func(real_lines))
        return True
    else:
        print(Fore.RED + "Test failed with result: " + Fore.RESET, test_result)
        return False


def show_perf(func):
    @wraps(func)
    def wrapper(*arg):
        tic = time.perf_counter_ns()
        print(func(*arg))
        toc = time.perf_counter_ns()
        print(f"In {toc - tic:0.4f} nanoseconds")

    return wrapper
