# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round F - Problem B. Festival
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887dba
#
# Time:  O(NlogN)
# Space: O(N)
#

from heapq import heappush, heappop
from collections import defaultdict

def festival():
    D, N, K = map(int, raw_input().strip().split())
    points = []
    for _ in xrange(N):
        h, s, e = map(int, raw_input().strip().split())
        points.append((s, 1, h))
        points.append((e+1, -1, h))
    points.sort()

    topk, others, to_remove = [], [], defaultdict(int)
    result = curr = l = 0
    for _, c, h in points:
        if c == 1:
            heappush(topk, h)
            curr += h
            l += 1
            if l == K+1:  # keep topk with k elements
                v = heappop(topk)
                curr -= v
                l -= 1
                heappush(others, -v)
            result = max(result, curr)
        else:
            to_remove[h] += 1
            if not others or -others[0] < h:
                curr -= h
                l -= 1
                if others:
                    v = -heappop(others)
                    heappush(topk, v)  # keep topk with k elements
                    curr += v
                    l += 1
        while others and -others[0] in to_remove:
            to_remove[-others[0]] -= 1
            if not to_remove[-others[0]]:
                del to_remove[-others[0]]
            heappop(others)
        while topk and topk[0] in to_remove:
            to_remove[topk[0]] -= 1
            if not to_remove[topk[0]]:
                del to_remove[topk[0]]
            heappop(topk)
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, festival())
