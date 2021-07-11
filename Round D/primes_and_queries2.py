# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round D - Problem D. Primes and Queries
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082bcf4
#
# Time:  O(N * (logN + log(log(max(A)))) + Q * (logN + log(log(max(val))) + log(log(max(S)))))
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

def binary_search_right(left, right, check):
    while left <= right:
        mid = left + (right-left)//2
        if not check(mid):
            right = mid-1
        else:
            left = mid+1
    return right

def vp(p, x):  # Time: O(log(logx))
    if x == 0:
        return 0
    exp, right = p, 1
    while exp < x:
        exp = exp*exp
        right *= 2
    assert(right <= 64)
    return binary_search_right(1, right, lambda n: x%p**n == 0)  # since p**n is O(logn), and n <= 64, we treat it as O(1)

def lte1(p, a, b):
    return vp(p, a-b)

def lte2(p, a, b):
    return vp(p, a+b)

def add(p, bits, pos, val, sign):  # Time: O(logN + log(log(max(val))))
    if val < p:
        return  # V(val^s - (val%p)^s) is 0, just skip
    if val%p == 0:
        bits[0].add(pos, sign*vp(p, val))
    else:
        bits[1].add(pos, sign*1)
        bits[2].add(pos, sign*lte1(p, val, val%p))
        if p == 2:
            bits[3].add(pos, sign*lte2(p, val, val%p))

def query(p, bits, pos, s):  # Time: O(logN + log(log(max(S))))
    # sum(s*vp(p, A[i]) for i in xrange(pos+1) if A[i] >= p and A[i]%p == 0) + \
    # sum(vp(p, s) + vp(p, A[i]-A[i]%p) for i in xrange(pos+1) if A[i] >= p and A[i]%p != 0) + \
    # (sum(vp(p, A[i]+A[i]%p)-1 for i in xrange(pos+1) if A[i] >= p and A[i]%p != 0) if p == 2 and s%2 == 0 else 0)
    return s*bits[0].query(pos) + \
           vp(p, s)*bits[1].query(pos) + bits[2].query(pos) + \
           (bits[3].query(pos)-bits[1].query(pos) if p == 2 and s%2 == 0 else 0)

def primes_and_queries():
    N, Q, P = map(int, raw_input().strip().split())

    bits = [BIT(N) for _ in xrange(3 if P != 2 else 4)]
    A = [0]*N
    for i, val in enumerate(map(int, raw_input().strip().split())):
        A[i] = val
        add(P, bits, i, A[i], 1)  # Time: O(logN + log(log(max(A))))
    result = []
    for ops in (map(int, raw_input().strip().split()) for _ in xrange(Q)):
        if len(ops) == 3:
            _, pos, val = ops
            i = pos-1
            add(P, bits, i, A[i], -1)  # Time: O(logN + log(log(max(val))))
            A[i] = val
            add(P, bits, i, A[i], 1)  # Time: O(logN + log(log(max(val))))
        else:
            _, S, L, R = ops
            result.append(query(P, bits, (R-1), S) - query(P, bits, (L-1)-1, S))  # Time: O(logN + log(log(max(S))))
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, primes_and_queries())
