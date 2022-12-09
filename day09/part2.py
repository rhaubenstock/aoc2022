from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def update(h,t):
    hr,hc = h
    tr,tc = t
    if abs(hr-tr) > 1 or abs(hc-tc) > 1:
        if hr > tr:
            tr += 1
        elif hr < tr:
            tr -= 1
        if hc > tc:
            tc += 1
        elif hc < tc:
            tc -= 1

    return (tr,tc)


def compute(s: str) -> int:
    #Assume the head and the tail both start at the same position, overlapping.
    tailSet = set([(0,0)])
    rope = [(0,0)]*10
    
    dirVec = {'U':(-1,0), 'R':(0,1), 'L':(0,-1), 'D':(1,0)}
    for line in s.split("\n"):
        dirStr, movStr = line.split()
        diff_r, diff_c = dirVec[dirStr]
        for _ in range(int(movStr)):
            rope[0] = (rope[0][0] + diff_r, rope[0][1] + diff_c)
            for i in range(1,10):
                rope[i] = update(rope[i-1],rope[i])
            tailSet.add(rope[-1])
    return len(tailSet)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())