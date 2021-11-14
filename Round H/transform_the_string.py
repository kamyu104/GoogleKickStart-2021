# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round H - Problem A. Transform the String
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008da461
#
# Time:  O(n)
# Space: O(1)
#

from collections import defaultdict

def transform_the_string():
    S, F = [raw_input().strip() for _ in xrange(2)]

    dist = defaultdict(lambda: float("inf"))
    for c in set(list(S)):
        for f in F:
            x = abs((ord(f)-ord('a'))-(ord(c)-ord('a')))
            dist[c] = min(dist[c], min(x, 26-x))
    return sum(dist[c] for c in S)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, transform_the_string())
