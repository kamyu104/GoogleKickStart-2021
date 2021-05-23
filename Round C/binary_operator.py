# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round C - Problem D. Binary Operator
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec290
#
# Time:  O(N * E)
# Space: O(N + E)
#

from random import seed, randint

def solution(E):
    lookup = {}
    class Operand(object):
        def __init__(self, state=None):
            self.state = state

        def __radd__(self, other):
            return Operand(other)

        def __add__(self, other):
            if (self.state, other) not in lookup:
                lookup[(self.state, other)] = randint(1, MAX_N*MAX_E)
            return lookup[(self.state, other)]

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
        curr = solution(E)
        if curr == prev:
            return curr
        prev = curr

seed(0)
MAX_N = MAX_E = 100
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, binary_operator())
