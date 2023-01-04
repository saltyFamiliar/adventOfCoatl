import testing
from fifteen import fifteen

DAY = "fifteen"

print("PART ONE:\n-------------")
if testing.test_part(fifteen.part_one, DAY, 26):
    print("\nPART TWO:\n-------------")
    testing.test_part(fifteen.part_two, DAY, 56000011)
