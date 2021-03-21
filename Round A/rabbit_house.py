# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round A - Problem C. Rabbit House
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cb14
#
# Time:  O(R * C)
# Space: O(R * C)
#

from collections import defaultdict

def rabbit_house():
    R, C = map(int, raw_input().strip().split())
    G = [map(int, raw_input().strip().split()) for _ in xrange(R)]

    buckets = defaultdict(set)
    for i in xrange(R):
        for j in xrange(C):
            buckets[G[i][j]].add((i, j))
    max_G = max(G[i][j] for i in xrange(R) for j in xrange(C))
    result = 0
    for h in reversed(xrange((max_G-((R-1)+(C-1)))+1, max_G+1)):
        for i, j in buckets[h]:
            for di, dj in DIRECTIONS:
                ni, nj = i+di, j+dj
                if not (0 <= ni < R and 0 <= nj < C and G[ni][nj] < h-1):
                    continue
                buckets[G[ni][nj]].remove((ni, nj))
                result += (h-1)-G[ni][nj]
                G[ni][nj] = h-1
                buckets[G[ni][nj]].add((ni, nj))
    return result

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, rabbit_house())
