"""
https://adventofcode.com/2018/day/2
"""
from collections import Counter

def doubleletter(id_string):
    """
    checks a string for a character appearing exactly twice
    """
    counts = Counter(id_string)
    return 2 in counts.values()

def tripleletter(id_string):
    """
    checks a string for a character appearing exactly twice
    """
    counts = Counter(id_string)
    return 3 in counts.values()

def checksum(ids):
    """
    returns the product of #(ids containing double letters) and
    #(ids containing triple letters)
    """
    doubles = [code for code in ids if doubleletter(code)]
    triples = [code for code in ids if tripleletter(code)]
    return len(doubles) * len(triples)


test_ids =["abcdef", "bababc", "abbcde", "abcccd", "aabcdd",
           "abcdee", "ababab"]

assert checksum(test_ids) == 12
file = "data/day02_input.txt"
with open(file) as f:
    real_ids = [line.strip() for line in f]

print(checksum(real_ids))

"""
to avoid an O(n^2) solution we iterate over the id list once, saving strings
with each letter deleted
"""

def deletions(string):
    out = set()
    for i in range(len(string)):
        out.add(string[:i] + '_' + string[i+1:])
    return out

def find_match(ids):
    seen = set()
    for id in ids:
        removeds = deletions(id)
        for item in removeds:
            if item in seen:
                return item
        seen = seen.union(removeds)

test_ids2 = ["abcde","fghij","klmno","pqrst","fguij","axcye","wvxyz"]
assert find_match(test_ids2) == "fg_ij"
print(find_match(real_ids).replace("_", ""))
