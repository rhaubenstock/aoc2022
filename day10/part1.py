from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.split("\n")
    signal = 1
    scoreAcc = 0
    n = len(lines)
    cycle = 1
    instr = 0
    endCond = 21
    sameInstr = False
    addAmt = 0
    while instr < n:
        while cycle < endCond and instr < n:
            # print("instr", instr)
            # print("cycle", cycle)
            cycle += 1
            if sameInstr:
                sameInstr = False
                instr += 1
                continue
            signal += addAmt
            addAmt = 0
            lineArr = lines[instr].split()
            if lineArr[0] != "addx":
                instr += 1
                continue
            sameInstr = True
            addAmt = int(lineArr[1])

        if cycle == endCond:
            scoreAcc += signal * (cycle-1)
        endCond += 40

    return scoreAcc


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())