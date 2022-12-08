from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.split("\n")
    rows = len(lines)
    cols = len(lines[0])
    
    visited = set()
    for r in range(rows):
        visited.add((r,0))
        visited.add((r,cols-1))
    for c in range(cols):
        visited.add((0,c))
        visited.add((rows-1,c))

    #NSEW
    for c in range(cols):

        prevTallest = lines[-1][c]
        for r in range(rows-2,0,-1):
            loc = (r,c)
            if lines[r][c] < prevTallest:
                continue
            if lines[r][c] > prevTallest:
                prevTallest = lines[r][c]
                if loc not in visited:
                    visited.add(loc)
            
        prevTallest = lines[0][c]
        for r in range(1,rows-1):
            loc = (r,c)
            if lines[r][c] < prevTallest:
                continue
            if lines[r][c] > prevTallest:
                prevTallest = lines[r][c]
                if loc not in visited:
                    visited.add(loc)
            
    
    for r in range(rows):

        prevTallest = lines[r][0]
        for c in range(1,cols-1):
            loc = (r,c)
            if lines[r][c] < prevTallest:
                continue
            if lines[r][c] > prevTallest:
                prevTallest = lines[r][c]
                if loc not in visited:
                    visited.add(loc)

        prevTallest = lines[r][-1]
        for c in range(cols-2,0,-1):
            loc = (r,c)
            if lines[r][c] < prevTallest:
                continue
            if lines[r][c] > prevTallest:
                prevTallest = lines[r][c]
                if loc not in visited:
                    visited.add(loc)       
    
    return len(visited)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())