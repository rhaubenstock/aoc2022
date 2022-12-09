from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def update(hr,hc,tr,tc):
    if abs(hr-tr) > 1:
        tr = (hr+tr)//2
        return tr, hc
    if abs(hc-tc) > 1:
        tc = (hc+tc)//2
        return hr, tc
    return tr,tc


def compute(s: str) -> int:
    #Assume the head and the tail both start at the same position, overlapping.
    tailSet = set([(0,0)])
    head_r = head_c = tail_r = tail_c = 0
    
    dirVec = {'U':(-1,0), 'R':(0,1), 'L':(0,-1), 'D':(1,0)}
    for line in s.split("\n"):
        dirStr, movStr = line.split()
        diff_r, diff_c = dirVec[dirStr]
        for _ in range(int(movStr)):
            head_r += diff_r
            head_c += diff_c
            tail_r, tail_c = update(head_r, head_c, tail_r, tail_c)
            tailSet.add((tail_r,tail_c))
    

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