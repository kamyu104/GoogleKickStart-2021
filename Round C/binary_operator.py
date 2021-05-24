# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round C - Problem D. Binary Operator
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec290
#
# Time:  O(N * E^2 * logE)
# Space: O(N + E)
#

from collections import Counter
from operator import add, mul
from functools import partial

class Poly(Counter):
    def __init__(self, expr=None):
        if expr is None:
            return
        if expr.isdigit():
            self.update({(): int(expr)})
        else:
            self[(expr,)] += 1

    def __add__(self, other):
        self.update(other)
        return self

    def __mul__(self, other):
        def merge(k1, k2):
            result = []
            i, j = 0, 0
            while i != len(k1) or j != len(k2):
                if j == len(k2):
                    result.append(k1[i])
                    i += 1
                elif i == len(k1):
                    result.append(k2[j])
                    j += 1
                elif k1[i] < k2[j]:
                    result.append(k1[i])
                    i += 1
                else:
                    result.append(k2[j])
                    j += 1
            return result

        result = Poly()
        for k1, v1 in self.iteritems():
            for k2, v2 in other.iteritems():
                result.update({tuple(merge(k1, k2)): v1*v2})
        return result

    def __str__(self):
        return " ".join(["*".join((str(v),) + k) for k, v in sorted(self.iteritems(), key=lambda x: (-len(x[0]), x[0])) if v])

def make_variable(n):
    result = []
    while n:
        result += chr((n-1)%26 + ord('a'))
        n = (n-1)//26
    result.reverse()
    return "".join(result)

def variable(lookup, x, y):
    if (str(x), str(y)) not in lookup:
        lookup[(str(x), str(y))] = make_variable(len(lookup)+1)
    return Poly(lookup[(str(x), str(y))])

def evaluate(s, ops):
    operands, operators, operand = [], [], []
    for i in xrange(len(s)):
        if s[i].isdigit():
            operand.append(s[i])
            if i == len(s)-1 or not s[i+1].isdigit():
                operands.append(Poly("".join(operand)))
                operand = []
        elif s[i] == ')':
            right, left = operands.pop(), operands.pop()
            operands.append(ops[operators.pop()](left, right))
        elif s[i] != '(':
            operators.append(s[i])
    return str(operands[-1])

def count(E):
    result, groups = [], {}
    ops = {'+':add, '*':mul, '#':partial(variable, {})}
    for s in E:
        g = evaluate(s, ops)
        if g not in groups:
            groups[g] = len(groups)+1
        result.append(str(groups[g]))
    return " ".join(result)

def binary_operator():
    N = input()
    E = [raw_input().strip() for _ in xrange(N)]

    return count(E)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, binary_operator())
