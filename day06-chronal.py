"""
https://adventofcode.com/2018/day/6


given a list of points
find the area of the largest finite set of coordinates closest to some point


Theorem: The area V(p) is infinite if p is on the boundary of the convex hull

"""

TEST_INPUT = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

def from_coord(coord: str):
    x, y = [int(a) for a in coord.split(", ")]
    return (x,y)

def manhattan(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

def edges(points):
    xs = [pt[0] for pt in points]
    ys = [pt[1] for pt in points]
    return (min(xs), min(ys), max(xs), max(ys))

import numpy as np

def makegrid(points):
    """
    makes a grid much bigger than the enclosed area to estimate which pts have
    infinite regions
    """
    (height, width) = (edges(points)[3],edges(points)[2]) 
    grid = np.zeros((3*height, 3* width), dtype=np.uint8)
    for i in range(len(points)):
        pt = points[i]
        grid[height + pt[1], width + pt[0]] += i + 1
    return grid




TEST_POINTS = [from_coord(coord) for coord in TEST_INPUT.split("\n")]
print(makegrid(TEST_POINTS))
