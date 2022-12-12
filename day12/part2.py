from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    #BFS
    #want shortest path from S to E
    start = None

    lines = s.split("\n")
    starts = set()
    for r,line in enumerate(lines):
        for c, char in enumerate(line):
            if char == 'S' or char == 'a':
                starts.add((r,c))

    rows = len(lines)
    cols = len(lines[0])

    def minPath(start):
        r,c = start

        q = [(r,c,0,97)]
        visited = set([(r,c)])

        def visitable(row, col, prev):
            validCell = row >= 0 and row < rows and col >= 0 and col < cols
            if not validCell or (row,col) in visited:
                return False
            charOrd = ord(lines[row][col])
            if charOrd == 69:
                charOrd = 122
            return charOrd <= prev + 1

        def tryVisit(r, c, d, p):
            if visitable(r,c,p):
                visited.add((r,c))
                q.append((r, c, d+1, ord(lines[r][c])))
                if lines[r][c] == 'E':
                    return True
            return False

        while q:
            r,c,d,p = q.pop(0)       

            if tryVisit(r-1,c,d,p):
                return d + 1
            if tryVisit(r+1,c,d,p):
                return d + 1
            if tryVisit(r,c-1,d,p):
                return d + 1
            if tryVisit(r,c+1,d,p):
                return d + 1
        
        # print(visited)
        return float('inf')
    
    return min([minPath(start) for start in starts])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())