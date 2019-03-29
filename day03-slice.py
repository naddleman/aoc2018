"""
https://adventofcode.com/2018/day/3
"""
import re
from typing import NamedTuple
import numpy as np

# defines a rectangle xmin < x <= xmax, ymin < y <= ymax
# where x=0 is the left side and y=0 is the top
Claim = NamedTuple('Claim', [('id', int),
                                    ('xmin', int),
                                    ('ymin', int),
                                    ('xmax', int),
                                    ('ymax', int)])

TEST_CLAIMS = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""

def parseline(line: str) -> Claim:
    regex =  '#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)'
    id, xmin, ymin, width, height = [int(x) for x in 
                                     re.match(regex, line).groups()]
    return Claim(id, xmin, ymin, xmin+width, ymin+height)

def parselines(lines: [str]) -> [Claim]:
    return [parseline(line) for line in lines.split('\n')]

assert parselines(TEST_CLAIMS) == \
        [Claim(id=1, xmin=1, ymin=3, xmax=5, ymax=7),
         Claim(id=2, xmin=3, ymin=1, xmax=7, ymax=5),
         Claim(id=3, xmin=5, ymin=5, xmax=7, ymax=7)]

def fabric_from_claims(claims):
    width = max(claims, key= lambda c: c.xmax).xmax
    height = max(claims, key = lambda c: c.ymax).ymax
    fabric = np.zeros((height, width))
    for claim in claims:
        fabric[claim.ymin:claim.ymax, claim.xmin:claim.xmax] +=1
    for claim in claims:
        if (fabric[claim.ymin:claim.ymax, claim.xmin:claim.xmax] == 1).all():
            claimid = claim.id
    return fabric, claimid

test_fabric = fabric_from_claims(parselines(TEST_CLAIMS))[0]
assert len(test_fabric[test_fabric > 1]) == 4

assert fabric_from_claims(parselines(TEST_CLAIMS))[1] == 3

file = "data/day03_input.txt"
with open(file) as f:
    input_claims = [parseline(line) for line in f]

fabric, intact = fabric_from_claims(input_claims)
print(len(fabric[fabric>1]))
print(intact)    
