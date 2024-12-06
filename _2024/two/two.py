from _2024 import utils

lines = utils.get_lines("input.txt")


def safe_decrease(s):
    for i, n in enumerate(s[1:], start=1):
        if abs(s[i - 1] - n) > 3 or abs(s[i - 1] - n) < 1:
            return False
    return True


safe = 0
for l in lines:
    # part 1
    # nums = [int(x) for x in l.split()]
    # nums_f = sorted(nums)
    # nums_b = sorted(nums, reverse=True)
    # if nums != nums_f and nums != nums_b:
    #     continue
    # if safe_decrease(nums):
    #     safe += 1

    # part 2
    nums = [int(x) for x in l.split()]
    for i in range(len(nums)):
        _nums = nums[:i] + nums[i + 1:]
        nums_f = sorted(_nums)
        nums_b = sorted(_nums, reverse=True)
        if _nums != nums_f and _nums != nums_b:
            continue
        if safe_decrease(_nums):
            safe += 1
            break

print(safe)
