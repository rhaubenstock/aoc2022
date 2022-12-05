from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    arr = [[] for _ in range(10)]
    lines = s.split("\n")
    j = 0
    for line in lines:
        if '[' in line:
            j += 1
            n = len(line)
            i = 0
            while i < n-2:
                if line[i+1] != ' ':
                    arr[1 + (i >> 2)].append(line[i+1])
                i+=4
        else:
            break
    for a in arr:
        a.reverse()
    for line in lines[j+2:]:
        move = line.split(" ")
        numBlocks = int(move[1])
        fromIdx = int(move[3])
        toIdx = int(move[5])

        bucket = arr[fromIdx]
        n = len(bucket)
        i = n - numBlocks
        for el in bucket[i:]:
            arr[toIdx].append(el)
        arr[fromIdx] = bucket[:i]
    
    print(arr)
    return ''.join([arr[i].pop() for i in range(1,10) if arr[i]])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())