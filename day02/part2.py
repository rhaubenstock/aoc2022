from __future__ import annotations

import argparse
import os.path

# import pytest

# import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    acc = 0
    lookup = [3,1,2,1,2,3,2,3,1]
    for line in s.split('\n'):
        oppCode = ord(line[0]) - 64
        #so now x means lose
        #       y means tie
        #       z means win
        indicatorCode = ord(line[2]) - 87
        # 1 - rock, 2 - paper, 3 - scissors
        # 2 > 1 > 3
        # opp code | indicator | your code (also num of points) | 
        # 1 | 1 | 3
        # 1 | 2 | 1 -- covered
        # 1 | 3 | 2
        # 2 | 1 | 1
        # 2 | 2 | 2 -- covered
        # 2 | 3 | 3
        # 3 | 1 | 2
        # 3 | 2 | 3 -- covered 
        # 3 | 3 | 1

        acc += 3*(indicatorCode - 1) # 1 -> 0, 2 -> 3, 3 -> 6
        acc += lookup[3*oppCode + indicatorCode - 4]
        
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
