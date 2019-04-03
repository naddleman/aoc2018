"""
https://adventofcode.com/2018/day/7
"""
import re

TEST_INPUT = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

rgx = r"Step ([A-Z]) must be finished before step ([A-Z]) can begin."

def parse_requirement(line):
    tail, head = re.match(rgx, line).groups()
    return (tail, head)

DEPENDENCIES = [parse_requirement(line) for line in TEST_INPUT.split('\n')]

def get_steps(reqs):
    steps = set()
    steps = steps.union([i for (i,_) in reqs])
    steps = steps.union([j for (_,j) in reqs])
    return steps

def make_dependencies(reqs):
    depends_on = dict()
    steps = get_steps(reqs)
    heads = {req[0] for req in reqs}
    tails = {req[1] for req in reqs}
    initials = {req[0] for req in reqs if req[0] not in tails}
    terminals = {req[1] for req in reqs if req[1] not in heads}
    return terminals, initials

def order(reqs):
    """lets try a naive approach"""
    requirements = reqs[:]
    lis = []
    terminals, initials = make_dependencies(reqs)
    while initials:
        next_step = min(initials)
        lis.append(next_step)
        requirements = [req for req in requirements if req[0] != next_step]
        _, initials = make_dependencies(requirements)
    lis.append(min(terminals))
    return lis
    # does not work for multiple terminals?
    #completed = set()
    #for step in get_steps(deps):
assert ''.join(order(DEPENDENCIES)) == 'CABDFE'

with open('data/day07_input.txt') as f:
    lines = [line.strip() for line in f]
    requirements = [parse_requirement(line) for line in lines]

print(''.join(order(requirements)))
