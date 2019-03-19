"""
https://adventofcode.com/2018/day/1
"""

file = "data/day01_input.txt"
with open(file) as f:
    frequencies = [int(line) for line in f]

print(sum(frequencies))

from itertools import cycle

def freq_seen_before(changelist):
    """
    Finds the first frequency that has been seen before
    danger of infinite loops
    """
    changecycle = cycle(changelist)
    seen = set()
    currentfreq = 0
    while True:
        if currentfreq in (seen):
            return currentfreq
        else:
            seen.add(currentfreq)
            currentfreq += next(changecycle)

assert freq_seen_before([1, -1]) == 0
assert freq_seen_before([3, 3, 4, -2, -4]) == 10
assert freq_seen_before([-6, 3, 8, 5, -6]) == 5
assert freq_seen_before([7, 7, -2, -7, -4]) == 14

print(freq_seen_before(frequencies))


