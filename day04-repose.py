"""
https://adventofcode.com/2018/day/4
"""
from typing import NamedTuple
import re
from collections import defaultdict

Sleep = NamedTuple('Sleep', [('guard', int),
                             ('sleep', int),
                             ('wake', int)])

TEST_INPUT ="""[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""

def parse_records(lines: str) -> [Sleep]:
    lines = sorted(lines.split('\n'))
    rgx = '\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})\] (.*)'
    sleeping = False
    sleeplist = []
    for line in lines:
        minute, event = re.match(rgx, line).groups()
        if event.split()[0] == 'Guard':
            guard = int(event.split()[1].strip('#'))
        elif event == 'falls asleep':
            sleeping = True
            sleepminute = int(minute)
        elif event == 'wakes up':
            sleeping = False
            wakeminute = int(minute)
            sleeplist.append(Sleep(guard, sleepminute, wakeminute))
        else:
            raise ValueError("improper event %r" % (event))
    return sleeplist

def most_sleepy(lines: str) -> int:
    naps = parse_records(lines)
    sleepingtime= defaultdict(int)
    for nap in naps:
        sleepingtime[nap.guard] += (nap.wake - nap.sleep)
    return max(sleepingtime, key=sleepingtime.get)

assert most_sleepy(TEST_INPUT) == 10

def sleepy_minute(lines: str) -> int:
    sleepy_guard = most_sleepy(lines)
    naps = parse_records(lines)
    sleeping_minutes = defaultdict(int)
    for nap in naps:
        if nap.guard == sleepy_guard:
            for i in range(nap.sleep, nap.wake):
                sleeping_minutes[i] += 1
    return max(sleeping_minutes, key=sleeping_minutes.get)

assert sleepy_minute(TEST_INPUT) == 24

def sleepiest_guard_minute(lines: str) -> int:
    guardminute = defaultdict(int)
    naps = parse_records(lines)
    for nap in naps:
        for i in range(nap.sleep, nap.wake):
            guardminute[(nap.guard, i)] += 1
    return max(guardminute, key=guardminute.get)

assert sleepiest_guard_minute(TEST_INPUT) == (99, 45)

file = "data/day04_input.txt"
with open(file) as f:
    inputstring = f.read().strip()
    guard = most_sleepy(inputstring)
    minute = sleepy_minute(inputstring)
    print(guard*minute)
    guard2, minute2 = sleepiest_guard_minute(inputstring)
    print(guard2*minute2)
