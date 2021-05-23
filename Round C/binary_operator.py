# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round C - Problem D. Binary Operator
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec290
#
# Time:  O(N * E)
# Space: O(N + E)
#

from random import seed, randint

def binary_operator():
    lookup = {}
    class Operand(object):
        def __init__(self, state=None):
            self.state = state

        def __radd__(self, other):
            return Operand(other)

        def __add__(self, other):
            if (self.state, other) not in lookup:
                lookup[(self.state, other)] = randint(10**9, 10**18)
            return lookup[(self.state, other)]

    N = input()
    result, groups, x = [], {}, Operand()
    for _ in xrange(N):
        g = eval(raw_input().strip().replace("#", "+x+"))
        if g not in groups:
            groups[g] = len(groups)+1
        result.append(str(groups[g]))
    return " ".join(result)

seed(0)
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, binary_operator())
