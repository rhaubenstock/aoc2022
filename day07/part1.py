from __future__ import annotations

import argparse
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

class Node():
    def __init__ (self, parent):
        self.size = 0
        self.children = {}
        self.parent = parent

def compute(s: str) -> int:
    #okay so first build tree
    #tree has nodes -> each node is a directory
    #but its kind of like a reverse tree right?
    #

    #assume no two directories have same name
    SIZELIMIT = 10**5
    acc = 0
    
    rootNode = Node(None)
    currentDir = rootNode

    lines = s.split("\n")
    n = len(lines)
    #first line is always "/"
    #second line is always "ls"

    i = 2
    while i < n:
        words = lines[i].split()
        if words[0] != "$":
            if words[0] == "dir":
                childNodeName = words[1]
                childNode = Node(currentDir)
                currentDir.children[childNodeName] = childNode 
            else:
                currentDir.size += int(words[0])
            i += 1
            continue
        #okay so now first "word" is '$'
        if words[1] == "ls":
            i += 1
            continue
        #so now its definitely $ cd __
        if words[2] == "..":
            #think if we go back up a directory then current dir is done
            parent = currentDir.parent
            if currentDir.size <= SIZELIMIT:
                acc += currentDir.size
            parent.size += currentDir.size

            currentDir = parent
        else:
            currentDir = currentDir.children[words[2]]
        i += 1
        
    while currentDir:
        dirSize = currentDir.size
        if dirSize >= SIZELIMIT:
            break
        acc += fileSize
        currentDir = currentDir.parent
        if currentDir:
            currentDir.size += dirSize

    return acc


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())