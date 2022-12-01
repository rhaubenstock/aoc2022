from __future__ import annotations

import argparse
import os.path

# import pytest

# import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    calorie_counts = (
        sum(int(line) for line in part.splitlines())
        for part in s.split('\n\n')
    )
    
    first, second, third = sorted((next(calorie_counts), next(calorie_counts), next(calorie_counts)))


    for this_cal in calorie_counts:
        if this_cal < third:
            continue
        if this_cal > first:
            third = second
            second = first
            first = this_cal
            continue
        if this_cal > second:
            third = second
            second = this_cal
            continue
        third = this_cal
    
    return first + second + third
        

INPUT_S = '''\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''
EXPECTED = 45000


# @pytest.mark.parametrize(
#     ('input_s', 'expected'),
#     (
#         (INPUT_S, EXPECTED),
#     ),
# )
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f: #, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
