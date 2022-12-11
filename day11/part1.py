from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input2.txt')

class Monkey:
    def __init__(self, items, op, nextMonkey):
        self.items = items
        self.op = op
        self.nextMonkey = nextMonkey
        self.inspections = 0

def compute(monkeys: list) -> int:
    
    
    for _ in range(20):
        for monkey in monkeys:
            monkey.inspections += len(monkey.items)
            for item in monkey.items:
                item = monkey.op(item)//3
                nextMonkey = monkeys[monkey.nextMonkey(item)]
                nextMonkey.items.append(item)
            monkey.items.clear()
    
    sortedInspections = sorted(map(lambda m: m.inspections, monkeys))
    print(sortedInspections)
    return sortedInspections[-1]*sortedInspections[-2]





def main() -> int:
    # parser = argparse.ArgumentParser()
    # parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    # args = parser.parse_args()

    # with open(args.data_file) as f:
    #     print(compute(f.read()))
    monkeys = []
    #0
    monkeys.append(Monkey(
        [66,79],
        lambda x: x*11,
        lambda x: 6 if x%7==0 else 7
    ))
    #1
    monkeys.append(Monkey(
        [84, 94, 94, 81, 98, 75],
        lambda x: x*17,
        lambda x: 5 if x%13==0 else 2
    ))
    #2
    monkeys.append(Monkey(
        [85, 79, 59, 64, 79, 95, 67],
        lambda x: x+8,
        lambda x: 4 if x%5==0 else 5
    ))
    #3
    monkeys.append(Monkey(
        [70],
        lambda x: x+3,
        lambda x: 6 if x%19==0 else 0
    ))
    #4
    monkeys.append(Monkey(
        [57, 69, 78, 78],
        lambda x: x+4,
        lambda x: 0 if x%2==0 else 3
    ))
    #5
    monkeys.append(Monkey(
        [65, 92, 60, 74, 72],
        lambda x: x+7,
        lambda x: 3 if x%11==0 else 4
    ))
    #6
    monkeys.append(Monkey(
        [77, 91, 91],
        lambda x: x*x,
        lambda x: 1 if x%17==0 else 7
    ))
    #7
    monkeys.append(Monkey(
        [76, 58, 57, 55, 67, 77, 54, 99],
        lambda x: x+6,
        lambda x: 2 if x%3==0 else 1
    ))

    # #0
    # monkeys.append(Monkey(
    #     [79, 98],
    #     lambda x: x*19,
    #     lambda x: 2 if x%23==0 else 3
    # ))

    # #1
    # monkeys.append(Monkey(
    #     [54, 65, 75, 74],
    #     lambda x: x + 6,
    #     lambda x: 2 if x%19==0 else 0
    # ))

    # #2
    # monkeys.append(Monkey(
    #     [79, 60, 97],
    #     lambda x: x * x,
    #     lambda x: 1 if x%13 == 0 else 3
    # ))

    # #3
    # monkeys.append(Monkey(
    #     [74],
    #     lambda x: x + 3,
    #     lambda x: 0 if x%17 == 0 else 1
    # ))

    print(compute(monkeys))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())