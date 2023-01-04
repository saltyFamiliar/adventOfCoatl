import operator
from typing import List


class Monkey:
    def __init__(self, text: List[str]) -> None:
        self.parse_monkey(text)
        self.items_inspected = 0

    def parse_monkey(self, text: List[str]):
        # starting items
        self.items = list(map(int, text[1].split(":")[1].split(",")))

        # operation
        a, op, b = text[2].split("=")[1].split()

        if op == "+":
            op = operator.add
        else:
            op = operator.mul
        self.operation = lambda x: op(
            (x if a == "old" else int(a)),
            (x if b == "old" else int(b)))

        # test
        test_var = int(text[3].split(":")[1].split()[-1])
        test_true = int(text[4].split()[-1])
        test_false = int(text[5].split()[-1])

        self.test = lambda: test_false if (self.items[0] % test_var) else test_true

    def inspect_item(self, relief=1):
        item = self.items[0]
        item = self.operation(item)
        item //= relief
        self.items[0] = item
        self.items_inspected += 1

    def catch_item(self, item):
        self.items.insert(0, item)

    def throw_item_to(self, other_monkey):
        other_monkey.catch_item(self.items.pop(0))

    def reduce_item(self, divisor_product):
        # thanks reddit
        self.items[0] %= divisor_product


def part_one(file_lines: List[str]) -> int:
    def take_turn(monkey: Monkey):
        while monkey.items:
            monkey.inspect_item(relief=3)
            monkey.throw_item_to(monkey_pack[monkey.test()])

    monkey_pack: List[Monkey] = []
    monkey_recipe: List[str] = []
    for line in file_lines:
        if len(line) < 2:
            continue
        monkey_recipe.append(line)
        if line.startswith("If false"):
            monkey_pack.append(Monkey(monkey_recipe))
            monkey_recipe = []

    for _ in range(20):
        for monkey in monkey_pack:
            take_turn(monkey)

    monkey_pack.sort(key=lambda x: x.items_inspected)
    return monkey_pack[-1].items_inspected * monkey_pack[-2].items_inspected


def part_two(file_lines: List[str]) -> int:
    def take_turn(monkey: Monkey):
        while monkey.items:
            monkey.reduce_item(divisor_product)
            monkey.inspect_item()
            monkey.throw_item_to(monkey_pack[monkey.test()])

    monkey_pack: List[Monkey] = []
    monkey_recipe: List[str] = []
    divisor_product = 1
    for line in file_lines:
        if len(line) < 2:
            continue
        monkey_recipe.append(line)
        if line.startswith("Test"):
            divisor_product *= int(line.split()[-1])
        elif line.startswith("If false"):
            monkey_pack.append(Monkey(monkey_recipe))
            monkey_recipe = []

    for _ in range(10000):
        for monkey in monkey_pack:
            take_turn(monkey)

    monkey_pack.sort(key=lambda x: x.items_inspected)
    return monkey_pack[-1].items_inspected * monkey_pack[-2].items_inspected
