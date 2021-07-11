# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round D - Problem B. Cutting Intervals
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082b933
#
# Time:  O(NlogN)
# Space: O(N)
#

from collections import Counter

def cutting_intervals():
    N, C = map(int, raw_input().strip().split())

    points = []
    for l, r in [map(int, raw_input().strip().split()) for _ in xrange(N)]:
        points.append((l+1, 1))
        points.append((r, -1))
    points.sort()
    curr = 0
    count = Counter()
    for i, c in points:
        curr += c
        count[i] = curr
    points = sorted(count.iterkeys())
    overlap_to_cnt = Counter()
    for i in xrange(1, len(points)):
        if count[points[i-1]]:
            overlap_to_cnt[count[points[i-1]]] += points[i]-points[i-1]
    overlap_to_cnt = sorted(x for x in overlap_to_cnt.iteritems())
    result = N
    while overlap_to_cnt:
        overlap, cnt = overlap_to_cnt.pop()
        cnt = min(C, cnt)
        result += cnt*overlap
        C -= cnt
        if C == 0:
            break
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, cutting_intervals())
