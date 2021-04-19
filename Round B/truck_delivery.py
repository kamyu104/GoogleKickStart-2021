# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round B - Problem D. Truck Delivery
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a885
#
# Time:  O((N + R) * log(min(MAX_L, MAX_W))), pass in PyPy2 but Python2
# Space: O(min(MAX_L, MAX_W))
#

from collections import defaultdict
from functools import partial
from fractions import gcd

class SegmentTree(object):  # 0-based index
    def __init__(self, N,
                 build_fn=lambda x, y: [y]*(2*x),
                 query_fn=lambda x, y: y if x is None else gcd(x, y),
                 update_fn=lambda x, y: y,
                 default_val=0):
        self.N = N
        self.H = (N-1).bit_length()
        self.query_fn = query_fn
        self.update_fn = update_fn
        self.default_val = default_val
        self.tree = build_fn(N, default_val)
        self.lazy = [None]*N

    def __apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.N:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def update(self, L, R, h):  # Time: O(logN), Space: O(N)
        def pull(x):
            while x > 1:
                x //= 2
                assert(x*2 < len(self.tree))
                self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2+1])
                if self.lazy[x] is not None:
                    self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

        if L > R:
            return
        L += self.N
        R += self.N
        L0, R0 = L, R
        while L <= R:
            if L & 1:  # is right child
                self.__apply(L, h)
                L += 1
            if R & 1 == 0:  # is left child
                self.__apply(R, h)
                R -= 1
            L //= 2
            R //= 2
        pull(L0)
        pull(R0)

    def query(self, L, R):  # Time: O(logN), Space: O(N)
        def push(x):
            n = 2**self.H
            while n != 1:
                y = x // n
                if self.lazy[y] is not None:
                    self.__apply(y*2, self.lazy[y])
                    self.__apply(y*2 + 1, self.lazy[y])
                    self.lazy[y] = None
                n //= 2

        result = self.default_val
        if L > R:
            return result

        L += self.N
        R += self.N
        push(L)
        push(R)
        while L <= R:
            if L & 1:  # is right child
                result = self.query_fn(result, self.tree[L])
                L += 1
            if R & 1 == 0:  # is left child
                result = self.query_fn(result, self.tree[R])
                R -= 1
            L //= 2
            R //= 2
        return result
    
    def __str__(self):
        showList = []
        for i in xrange(self.N):
            showList.append(self.query(i, i))
        return ",".join(map(str, showList))

def iter_dfs(adj, queries, st, result, MAX_L, MAX_W):
    def divide(curr, prev):
        for node, l, a in reversed(adj[curr]):
            if node == prev:
                continue
            stk.append(partial(postprocess, l))
            stk.append(partial(divide, node, curr))
            stk.append(partial(prevprocess, l, a))
        stk.append(partial(init, curr))

    def init(curr):
        for w, i in queries[curr]:
            result[i] = st.query(0, min(w, MAX_L)-1)

    def prevprocess(l, a):
        if l <= MAX_W:
            st.update(l-1, l-1, a)  # all Li are distinct

    def postprocess(l):
        if l <= MAX_W:
            st.update(l-1, l-1, 0)

    stk = [partial(divide, 1, 0)]
    while stk:
        stk.pop()()

def truck_delivery():
    N, Q = map(int, raw_input().strip().split())
    adj = defaultdict(list)
    MAX_L = 0
    for _ in xrange(N-1):
        X, Y, L, A = map(int, raw_input().strip().split())
        MAX_L = max(MAX_L, L)
        adj[X].append((Y, L, A))
        adj[Y].append((X, L, A))
    MAX_W = 0
    queries = defaultdict(list)
    for i in xrange(Q):
        C, W = map(int, raw_input().strip().split())
        MAX_W = max(MAX_W, W)
        queries[C].append((W, i))
    st = SegmentTree(min(MAX_L, MAX_W))
    result = [0]*Q
    iter_dfs(adj, queries, st, result, MAX_L, MAX_W)
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, truck_delivery())
