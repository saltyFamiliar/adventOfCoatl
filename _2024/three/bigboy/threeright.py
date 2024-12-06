import cProfile
import pstats
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np

np.ndarray.argsort()


def validate_sequence(nums):
    if len(nums) < 2:
        return True, True

    # Calculate differences between adjacent elements
    diffs = np.diff(nums)

    # Check if differences are within the valid range (-3 to 3, excluding 0)
    valid_diffs = (np.abs(diffs) > 0) & (np.abs(diffs) <= 3)

    # Check if the sequence is valid without removal
    no_removal_valid = np.all(valid_diffs) and (np.all(diffs > 0) or np.all(diffs < 0))

    if no_removal_valid:
        return True, True

    # Check if removing one element can make the sequence valid
    n = len(nums)

    # Create a sliding window view of the array
    windows = np.lib.stride_tricks.sliding_window_view(nums, 3)

    # Calculate differences for each window
    window_diffs = np.diff(windows, axis=1)

    # Check if removing the middle element makes the window valid
    valid_windows = (np.abs(window_diffs.sum(axis=1)) > 0) & (np.abs(window_diffs.sum(axis=1)) <= 3)

    # Check if there's a valid window that makes the entire sequence valid
    removal_valid = np.any(valid_windows) and (
            (valid_diffs[:n - 3].all() and valid_diffs[n - 2:].all()) or
            (valid_diffs[:n - 2].all() and valid_diffs[n - 1:].all()) or
            (valid_diffs[:n - 1].all() and valid_diffs[n:].all())
    )

    return no_removal_valid, removal_valid


def process_chunk(chunk):
    results = np.array([validate_sequence(seq) for seq in chunk])
    return results


def process_sequences(sequences, num_workers=8):
    chunk_size = len(sequences) // num_workers
    chunks = [sequences[i:i + chunk_size] for i in range(0, len(sequences), chunk_size)]

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        results = list(executor.map(process_chunk, chunks))
    return np.concatenate(results)


def main():
    start_time = time.time()
    sequences = np.loadtxt('input.txt', dtype=int)
    read_duration = time.time() - start_time
    print(f"Reading duration: {read_duration:.4f} seconds")

    profiler = cProfile.Profile()
    profiler.enable()

    all_results = process_sequences(sequences)

    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumulative')
    stats.dump_stats('python_profile.stats')

    part1 = np.sum(all_results[:, 0])
    part2 = np.sum(all_results[:, 1])

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


main()
