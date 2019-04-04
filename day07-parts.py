"""
https://adventofcode.com/2018/day/7
"""
import re
from collections import namedtuple

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

REQUIREMENTS = [parse_requirement(line) for line in TEST_INPUT.split('\n')]

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
assert ''.join(order(REQUIREMENTS)) == 'CABDFE'

with open('data/day07_input.txt') as f:
    lines = [line.strip() for line in f]
    requirements = [parse_requirement(line) for line in lines]

# Part 1:
#print(''.join(order(requirements)))

#class Task:
#    def __init__(self, label, worked_on, remaining_dur):
#        self.label = label
#        self.worked_on = worked_on
#        self.remaining_dur = remaining_dur

Task = namedtuple('Task', ['label', 'worked_on', 'remaining_dur'])
State = namedtuple('State', ['actives', 'availables', 'elves', 'reqs'])
#class State:
#    def __init__(self, actives, availables, elves, reqs):
#        self.actives = actives,
#        self.availables = availables,
#        self.elves = elves,
#        self.reqs = reqs
#    def is_valid(self):
#        return (not bool(availables)) or (not bool(elves))

def extra_dur(c):
    return ord(c) - 64

def make_dependencies_tasks(reqs, base_dur):
    depends_on = dict()
    steps = get_steps(reqs)
    heads = {req[0] for req in reqs}
    tails = {req[1] for req in reqs}
    initials  = {req[0] for req in reqs if req[0] not in tails}
    terminals = {req[1] for req in reqs if req[1] not in heads}
    initial_tasks  = {Task(i, False, extra_dur(i) + base_dur)
                      for i in initials}
    terminal_tasks = {Task(i, False, extra_dur(i) + base_dur)
                      for i in terminals}
    return terminal_tasks, initial_tasks

def initial_state(reqs, elves, base_dur):
    terminals, initials = make_dependencies_tasks(reqs, base_dur)
    active_tasks = set()
    while elves and initials:
        new = min(initials, key = lambda x: x.label)
        active_tasks.add(new._replace(worked_on = True))
        initials.remove(new)
        elves -= 1
    return active_tasks


def time_step(tasks, elves):
    pass


def parallel_time(reqs, elves, base_dur):
    requirements = reqs[:]
    free_elves = elves
    _, inits = make_dependencies(requirements)
    duration = 0
    completed, actives = set(), set()
    while free_elves:
        if inits:
            for init in inits:
                actives.add(Task(min(inits), True, extra_dur(init) + base_dur))
                elves -= 1
                inits.remove(init)
        else: break

