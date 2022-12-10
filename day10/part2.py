from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    screenArr = [['.']*40 for _ in range(6)]
    lines = s.split("\n")
    signal = 1
    n = len(lines)
    instr = 0
    endCond = 21
    sameInstr = False
    addAmt = 0

    for r in range(6):
        for c in range(40):
            if sameInstr:
                sameInstr = False
                instr += 1
                if abs(c - signal) < 2:
                    screenArr[r][c] = '#'
                continue
            signal += addAmt
            if abs(c - signal) < 2:
                screenArr[r][c] = '#'
            addAmt = 0
            lineArr = lines[instr].split()
            if lineArr[0] != "addx":
                instr += 1
                continue
            sameInstr = True
            addAmt = int(lineArr[1])

    for rowArr in screenArr:
        print(''.join(rowArr))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())