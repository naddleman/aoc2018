"""
https://adventofcode.com/2018/day/6

given a list of points
find the area of the largest finite set of coordinates closest to some point

Theorem: The area V(p) is infinite if p is on the boundary of the convex hull
"""
import numpy as np

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

def makegrid2(points):
    (height, width) = (edges(points)[3] + 5,edges(points)[2] + 5) 
    grid = np.zeros((height, width), dtype=np.uint8)
    for i in range(len(points)):
        pt = points[i]
        grid[pt[1] + 2, pt[0] + 2] += i + 1
    return grid, height, width

def assign_areas(points):
    grid, height, width= makegrid2(points)
    print(grid.shape)
    step = 0
    for (x,y), value in np.ndenumerate(grid):
        if step % 10000 == 0:
            print(step)
        step += 1
        distances = []
        for i in range(len(points)):
            pt = points[i]
            distances.append(manhattan((x,y), (pt[0], pt[1])))
        nearest = [i for i, v in enumerate(distances) if v == min(distances)]
        if len(nearest) == 1:
            grid[x,y] = nearest[0] + 1
    unique, counts = np.unique(grid, return_counts=True)
    infinites = set()
    infinites = infinites.union(set(np.unique(grid[0])))
    infinites = infinites.union(set(np.unique(grid[-1])))
    infinites = infinites.union(set(np.unique(grid[:, 0])))
    infinites = infinites.union(set(np.unique(grid[:, -1])))
    areas = []
    for i in range(1, len(points) + 1):
        if i not in infinites:
            areas.append(counts[i])
    return max(areas)

TEST_POINTS = [from_coord(coord) for coord in TEST_INPUT.split("\n")]
assert assign_areas(TEST_POINTS) == 17

def total_dist(points, dist_limit):
    grid, height, width= makegrid2(points)
    close_enough = 0
    step = 0
    for (x,y), value in np.ndenumerate(grid):
        if step % 10000 == 0:
            print(step)
        step += 1
        total_dist = 0
        for pt in points:
            total_dist += manhattan((x,y), (pt[0], pt[1]))
        if total_dist < dist_limit:
            close_enough += 1
    return close_enough

assert total_dist(TEST_POINTS, 32) == 16

file = 'data/day06_input.txt'
with open(file) as f:
    ins = f.read().rstrip('\n')
    points = [from_coord(coord) for coord in ins.split('\n')]
    #print(assign_areas(points))
    print(total_dist(points, 10000))
