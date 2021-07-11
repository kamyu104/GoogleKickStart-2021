# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round D - Problem A. Arithmetic Square
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082b813
#
# Time:  O(1)
# Space: O(1)
#

from collections import Counter

def arithmetic_square():
    G = []
    for _ in xrange(3):
        G.extend(map(int, raw_input().strip().split()))
    # 0 1 2
    # 3   4
    # 5 6 7
    result = sum(G[i]+G[j] == 2*G[k] for i, j, k in [(0, 2, 1), (5, 7, 6), (0, 5, 3), (2, 7, 4)])
    count = Counter()
    for i, j in [(0, 7), (2, 5), (1, 6), (3, 4)]:
        if (G[i]+G[j]) % 2 == 0:
            count[G[i]+G[j]] += 1
    return result + max(count.values() or [0])

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, arithmetic_square())
