from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input2.txt')


def compute(s: str) -> int:
    arr = [0]*26
    k = 14
    for i in range(k-1):
        arr[ord(s[i])-97] += 1
    countDupes = k-1 - len(set(s[:k-1]))

    for i, c in enumerate(s[3:]):
        if arr[ord(s[i + 3])-97] > 0:
            countDupes += 1
        arr[ord(s[i + 3])-97] += 1
        if countDupes == 0:
            return i + 4
        if arr[ord(s[i])-97] > 1:
            countDupes -= 1
        arr[ord(s[i])-97] -= 1
    


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())