# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round D - Problem D. Primes and Queries
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082bcf4#analysis
#
# Time:  O(N * log(max(A)) + Q * (logN + log(max(S)) + log(max(val))))
# Space: O(N)
#

class BIT(object):  # 0-indexed.
    def __init__(self, n):
        self.__bit = [0]*(n+1)  # Extra one for dummy node.

    def add(self, i, val):
        i += 1  # Extra one for dummy node.
        while i < len(self.__bit):
            self.__bit[i] += val
            i += (i & -i)

    def query(self, i):
        i += 1  # Extra one for dummy node.
        ret = 0
        while i > 0:
            ret += self.__bit[i]
            i -= (i & -i)
        return ret

def vp(p, x):
    result = 0
    while x%p == 0:
        result += 1
        x //= p
    return result

# vp(a^s-a^s) = vp(s) + vp(a-b)
def lte_odd(p, a, b):
    return vp(p, a-b)

# vp(a^s-a^s) = vp(s) + (vp(a-b)+vp(a+b)-1)
def lte_even(p, a, b):
    return vp(p, a-b)+vp(p, a+b)-1

def add(p, bits, pos, val):
    if val < p:  # vp(p, val) is 0, just skip
        return
    if val%p == 0:
        bits[0].add(pos, vp(p, val))
    else:
        bits[1].add(pos, 1)
        bits[2].add(pos, lte_even(p, val, val%p))
        bits[3].add(pos, lte_odd(p, val, val%p))

def remove(p, bits, pos, val):
    if val < p:  # vp(p, val) is 0, just skip
        return
    if val%p == 0:
        bits[0].add(pos, -vp(p, val))
    else:
        bits[1].add(pos, -1)
        bits[2].add(pos, -lte_even(p, val, val%p))
        bits[3].add(pos, -lte_odd(p, val, val%p))

def query(p, bits, pos, s):
    return s*bits[0].query(pos) + vp(p, s)*bits[1].query(pos) + bits[2].query(pos) if p == 2 and s%2 == 0 else \
           s*bits[0].query(pos) + vp(p, s)*bits[1].query(pos) + bits[3].query(pos)

def primes_and_queries():
    N, Q, P = map(int, raw_input().strip().split())

    bits = [BIT(N) for _ in xrange(4)]
    A = [0]*N
    for i, val in enumerate(map(int, raw_input().strip().split())):
        A[i] = val
        add(P, bits, i, A[i])
    result = []
    for ops in (map(int, raw_input().strip().split()) for _ in xrange(Q)):
        if len(ops) == 3:
            _, pos, val = ops
            i = pos-1
            remove(P, bits, i, A[i])
            A[i] = val
            add(P, bits, i, A[i])
        else:
            _, S, L, R = ops
            result.append(query(P, bits, (R-1), S) - query(P, bits, (L-1)-1, S))
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, primes_and_queries())
