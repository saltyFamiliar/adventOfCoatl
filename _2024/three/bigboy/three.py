import cProfile
import pstats
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np


def is_valid_sequence(nums):
    if len(nums) < 2:
        return True
    diffs = np.diff(nums)
    if np.any((diffs == 0) | (np.abs(diffs) > 3)):
        return False
    increasing = diffs[0] > 0
    if increasing:
        return np.all(diffs > 0)
    return np.all(diffs < 0)


def check_sequence_with_removal(nums):
    n = len(nums)
    for skip in range(n):
        masked = np.delete(nums, skip)
        diffs = np.diff(masked)

        increasing_valid = np.all((diffs > 0) & (diffs <= 3))
        if increasing_valid:
            return True

        decreasing_valid = np.all((diffs < 0) & (diffs >= -3))
        if decreasing_valid:
            return True
    return False


def process_chunk(chunk):
    results = np.zeros((len(chunk), 2), dtype=bool)
    for i, seq in enumerate(chunk):
        results[i, 0] = is_valid_sequence(seq)
        results[i, 1] = results[i, 0] or check_sequence_with_removal(seq)
    return results


def process_sequences(chunks, num_workers=8):
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        results = list(executor.map(process_chunk, chunks))
    return np.concatenate(results)


def read_input(filename):
    chunks = []
    current_chunk = []
    chunk_size = 10000

    with open(filename, 'r') as f:
        for line in f:
            nums = np.fromstring(line, dtype=int, sep=' ')
            current_chunk.append(nums)
            if len(current_chunk) == chunk_size:
                chunks.append(current_chunk)
                current_chunk = []

    if current_chunk:
        chunks.append(current_chunk)
    return chunks


def main():
    start_time = time.time()
    chunks = read_input('input.txt')
    read_duration = time.time() - start_time
    print(f"Reading duration: {read_duration:.4f} seconds")

    profiler = cProfile.Profile()
    profiler.enable()

    all_results = process_sequences(chunks)

    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumulative')
    stats.dump_stats('python_profile.stats')

    part1 = np.sum(all_results[:, 0])
    part2 = np.sum(all_results[:, 1])

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main_start = time.time()
    main()
    print(f"Total execution time: {time.time() - main_start:.4f} seconds")
