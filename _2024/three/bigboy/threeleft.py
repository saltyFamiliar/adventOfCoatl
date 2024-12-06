import time

import numpy as np


def is_valid_sequence(nums):
    if len(nums) < 2:
        return True
    diffs = np.diff(nums)
    if np.any(np.abs(diffs) > 3) or np.any(diffs == 0):
        return False
    increasing = diffs[0] > 0
    return np.all((diffs > 0) == increasing)


def check_sequence_with_removal(nums):
    n = len(nums)
    for skip in range(n):
        seq = np.delete(nums, skip)
        diffs = np.diff(seq)

        if np.all(np.abs(diffs) <= 3) and np.all(diffs != 0):
            if np.all(diffs > 0) or np.all(diffs < 0):
                return True
    return False


def process_sequences(sequences):
    count1 = sum(is_valid_sequence(seq) for seq in sequences)
    count2 = sum(is_valid_sequence(seq) or check_sequence_with_removal(seq) for seq in sequences)
    return count1, count2


def read_input(filename):
    with open(filename, 'r') as f:
        return [np.fromstring(line.strip(), sep=' ', dtype=int) for line in f]


def benchmark(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"Execution time: {end - start:.2f} seconds")
    return result


def main():
    sequences = benchmark(read_input, "input.txt")
    part1, part2 = benchmark(process_sequences, sequences)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()
