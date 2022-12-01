advent of code 2022
===================

https://adventofcode.com/2022


### about

Trying to challenge myself and complete the full 25 days of AOC, using Anthony Sottile's repo structure as a starting point.

Set up according to his tutorial here:
https://www.youtube.com/watch?v=CZZLCeRya74

### timing

- comparing to these numbers isn't necessarily useful
- normalize your timing to day 1 part 1 and compare
- alternate implementations are listed in parens
- these timings are very non-scientific (sample size 1)

```console
$ find -maxdepth 1 -type d -name 'day*' -not -name day00 | sort | xargs --replace bash -xc 'python {}/part1.py {}/input.txt; python {}/part2.py {}/input.txt'
+ python day01/part1.py day01/input.txt
68787
> 756 μs
+ python day01/part2.py day01/input.txt
198041
> 789 μs
```
