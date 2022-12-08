from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.split("\n")
    rows = len(lines)
    cols = len(lines[0])

    #iterate over everything? -- except border bc those will have score 0
    bestScore = 0
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            nr = r - 1
            while nr > 0 and lines[nr][c] < lines[r][c]:
                nr -= 1
            n = r - nr

            sr = r + 1
            while sr < rows - 1 and lines[sr][c] < lines[r][c]:
                sr += 1
            s = sr - r

            ec = c + 1
            while ec < cols - 1 and lines[r][ec] < lines[r][c]:
                ec += 1
            e = ec - c

            wc = c - 1
            while wc > 0 and lines[r][wc] < lines[r][c]:
                wc -= 1
            w = c - wc
            
            score = n * e * w * s
            if score > bestScore:
                bestScore = score
    return bestScore


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())