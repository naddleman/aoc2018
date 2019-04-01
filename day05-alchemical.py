"""
https://adventofcode.com/2018/day/5
Reducing a string by reduction rules of the form:
    "Xx" -> ""
    "xX" -> ""
    for x, X a lowercase/uppercase pair.

"""
from collections import defaultdict
from string import ascii_lowercase

def matching_polarity(a,b):
    return (a.lower() == b.lower() and (a != b))

assert matching_polarity('A', 'a')
assert not matching_polarity('b', 'b')

def reducepoly(polymer: str) -> str:
    polymer = polymer[:]
    for i in sorted(range(len(polymer) - 1), reverse=True):
        radius = 0
        while i - radius >= 0 and i + 1 + radius < len(polymer):
            if matching_polarity(polymer[i-radius], polymer[i+1+radius]):
                radius += 1
            else:
                break
        polymer = polymer[:1+i- radius] + polymer[1+i+radius:]
    return polymer

assert reducepoly('znAaNb') == 'zb'
assert reducepoly('abBA') == ''
assert reducepoly('abAB') == 'abAB'
assert reducepoly('dabAcCaCBAcCcaDA') == 'dabCBAcaDA'

def best_reduce(polymer):
    lengths = []
    for c in ascii_lowercase:
        newpoly = polymer[:]
        newpoly = newpoly.replace(c, "")
        newpoly = newpoly.replace(c.upper(), "")
        lengths.append(len(reducepoly(newpoly)))
    return min(lengths)

assert best_reduce('dabAcCaCBAcCcaDA') == 4

file = "data/day05_input.txt"
with open(file) as f:
    polymer = f.read().strip('\n')
    string = reducepoly(polymer)

print(len(polymer))
print(len(string))
print(best_reduce(string))
