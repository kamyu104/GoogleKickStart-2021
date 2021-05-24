# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round C - Problem D. Binary Operator
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec290
#
# Time:  O(N^2 * E)
# Space: O(N + E)
#

from random import seed, randint

def hash(lookup, x, y):
    if (x, y) not in lookup:
        lookup[(x, y)] = randint(0, MOD-1)
    return lookup[(x, y)]    

def count(E):
    lookup = {}
    class Operand(object):
        def __init__(self, state=None):
            self.state = state

        def __radd__(self, other):
            return Operand(other)

        def __add__(self, other):
            return hash(lookup, self.state, other)

    result, groups, x = [], {}, Operand()
    for e in E:
        g = eval(e.replace("#", "+x+"))
        if g not in groups:
            groups[g] = len(groups)+1
        result.append(str(groups[g]))
    return " ".join(result)

def binary_operator():
    N = input()
    E = [raw_input().strip() for _ in xrange(N)]

    prev = None
    while True:
        curr = count(E)
        if curr != prev:
            prev = curr
            cnt = 1
            continue
        cnt += 1
        if cnt == K:
            return curr

seed(0)
MOD = 10**9+7
K = 3
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, binary_operator())
