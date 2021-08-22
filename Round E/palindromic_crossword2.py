# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round E - Problem C. Palindromic Crossword
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000043585c/0000000000859dcd
#
# Time:  O(N * M * alpha(N * M)) ~= O(N * M)
# Space: O(N * M)
#
# union find solution (slower)
#

from collections import defaultdict

class UnionFind(object):  # Time: (n * alpha(n)), Space: O(n)
    def __init__(self, n):
        self.set = range(n)
        self.rank = [0]*n

    def find_set(self, x):
        stk = []
        while self.set[x] != x:  # path compression
            stk.append(x)
            x = self.set[x]
        while stk:
            self.set[stk.pop()] = x
        return x

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        if self.rank[x_root] < self.rank[y_root]:  # union by rank
            self.set[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.set[y_root] = x_root
        else:
            self.set[y_root] = x_root
            self.rank[x_root] += 1
        return True

def get_index(c, i, j):
    return i*c+j

def get_coordinate(i, j, transposed):
    return (i, j) if not transposed else (j, i)

def get_grid(grid, i, j, transposed):
    return grid[i][j] if not transposed else grid[j][i]

def build_adj(grid, transposed, adj):
    n, m = (len(grid), len(grid[0])) if not transposed else (len(grid[0]), len(grid))
    for i in xrange(n):
        prev = -1
        for j in xrange(m+1):
            if j != m and get_grid(grid, i, j, transposed) != '#':
                continue
            left, right = prev+1, j-1
            while left < right:
                adj[get_coordinate(i, left, transposed)].append(get_coordinate(i, right, transposed))
                adj[get_coordinate(i, right, transposed)].append(get_coordinate(i, left, transposed))
                left, right = left+1, right-1
            prev = j

def palindromic_crossword():
    N, M = map(int, raw_input().strip().split())
    GRID = [list(raw_input().strip()) for _ in xrange(N)]

    adj = defaultdict(list)
    for transposed in xrange(2):
        build_adj(GRID, transposed, adj)
    uf = UnionFind(N*M)
    for (r1, c1), pairs in adj.iteritems():
        for (r2, c2) in pairs:
            uf.union_set(get_index(M, r1, c1), get_index(M, r2, c2))
    fill = ['.']*(N*M)
    for i in xrange(N):
        for j in xrange(M):
            if GRID[i][j] != '.' and GRID[i][j] != '#':
                fill[uf.find_set(get_index(M, i, j))] = GRID[i][j]
    result = 0
    for i in xrange(N):
        for j in xrange(M):
            if GRID[i][j] == '.' and fill[uf.find_set(get_index(M, i, j))] != '.':
                GRID[i][j] = fill[uf.find_set(get_index(M, i, j))]
                result += 1
    return "%s\n%s" % (result, "\n".join(("".join(row) for row in GRID)))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, palindromic_crossword())
