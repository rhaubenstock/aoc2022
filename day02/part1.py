from __future__ import annotations

import argparse
import os.path

# import pytest

# import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    acc = 0
    for line in s.split('\n'):
        oppCode = ord(line[0]) - 64
        yourCode = ord(line[2]) - 87
        # 1 - rock, 2 - paper, 3 - scissors
        # 2 > 1 > 3
        # your code | opp code | pts
        # 1 | 1 | 3
        # 1 | 2 | 0
        # 1 | 3 | 6
        # 2 | 1 | 6
        # 2 | 2 | 3
        # 2 | 3 | 0
        # 3 | 1 | 0
        # 3 | 2 | 6
        # 3 | 3 | 3
        acc += yourCode
        if oppCode == yourCode:
            acc += 3
            continue
        diff = yourCode - oppCode
        if diff == 1 or diff == -2:
            acc += 6
    return acc


    


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
EXPECTED = 24000


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

    # with open(args.data_file) as f, support.timing():
    #     print(compute(f.read()))
    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
