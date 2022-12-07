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
    # ^ WRONG!, but is true no two directories in same direct parent directory have same name
    #there are repeated names fml

    DISKSIZE = 7*10**7
    NEEDEDFREE = 3*10**7

    rootNode = Node(None)
    nodeSizes = []

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
                childDirName = words[1]
                childNode = Node(currentDir)
                currentDir.children[childDirName] = childNode
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
            nodeSizes.append(currentDir.size)
            currentDir.parent.size += currentDir.size
            currentDir = currentDir.parent
        else:
            currentDir = currentDir.children[words[2]]
        i += 1
        
    while currentDir.parent:
        nodeSizes.append(currentDir.size)
        currentDir.parent.size += currentDir.size
        currentDir = currentDir.parent

    currentFree = DISKSIZE - rootNode.size
    neededToFree = NEEDEDFREE - currentFree

    #find smallest num >= neededToFree
    smallestToUpdate = rootNode.size

    for value in nodeSizes:
        if value > neededToFree and value < smallestToUpdate:
            smallestToUpdate = value
    
    return smallestToUpdate


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())