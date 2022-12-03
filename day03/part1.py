from __future__ import annotations

import argparse
import os.path

# import pytest

# import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    acc = 0
    for sack in s.split('\n'):
        midpt= len(sack)//2
        firstHalf = set(sack[:midpt])
        secondHalf = set(sack[midpt:])
        char = (firstHalf & secondHalf).pop()
        code = ord(char)
        if code >= 97:
            acc += code - 96
            continue
        acc += code - 38
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
