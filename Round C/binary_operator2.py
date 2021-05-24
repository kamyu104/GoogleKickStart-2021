# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round C - Problem D. Binary Operator
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec290
#
# Time:  O(N * E)
# Space: O(N + E)
#

from random import seed, randint
from functools import partial

def addmod(x, y):
    return (x+y)%MOD

def mulmod(x, y):
    return (x*y)%MOD

def hash(lookup, x, y):
    if (x, y) not in lookup:
        lookup[(x, y)] = randint(0, MOD-1)
    return lookup[(x, y)]    

def evaluate(s, ops):
    operands, operators, operand = [], [], 0
    for i in xrange(len(s)):
        if s[i].isdigit():
            operand = addmod(operand*10, int(s[i]))
            if i == len(s)-1 or not s[i+1].isdigit():
                operands.append(operand)
                operand = 0
        elif s[i] == ')':
            right, left = operands.pop(), operands.pop()
            operands.append(ops[operators.pop()](left, right))
        elif s[i] != '(':
            operators.append(s[i])
    return operands[-1]

def count(E):
    result, groups = [], {}
    ops = {'+':addmod, '*':mulmod, '#':partial(hash, {})}
    for s in E:
        g = evaluate(s, ops)
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
            cnt = 0
        cnt += 1
        if cnt == K:
            return curr

seed(0)
MOD = 10**9-63  # a prime rather than 10**9+7 to avoid collision made by corner case
K = 2
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, binary_operator())
