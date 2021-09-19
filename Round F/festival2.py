# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round F - Problem B. Festival
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887dba
#
# Time:  O(NlogN)
# Space: O(N)
#

from heapq import heappush, heappop

def festival():
    D, N, K = map(int, raw_input().strip().split())
    intervals = []
    for _ in xrange(N):
        h, s, e = map(int, raw_input().strip().split())
        intervals.append((s, 1, h))
        intervals.append((e+1, -1, h))
    intervals.sort()

    topk, others, topk_to_remove, others_to_remove = [], [], [], []
    result = curr = l = 0
    for _, e, h in intervals:
        if e == 1:
            while topk and topk_to_remove and topk[0] == topk_to_remove[0]:
                heappop(topk), heappop(topk_to_remove)
            heappush(topk, h)
            curr += h
            l += 1
            if l == K+1:  # keep topk_sl with k elements
                v = heappop(topk)
                curr -= v
                l -= 1
                heappush(others, -v)
            result = max(result, curr)
        else:
            while others and others_to_remove and others[0] == others_to_remove[0]:
                heappop(others), heappop(others_to_remove)
            if others and h <= -others[0]:
                heappush(others_to_remove, -h)
                continue
            heappush(topk_to_remove, h)
            curr -= h
            l -= 1
            if not others:
                continue
            v = -heappop(others)
            heappush(topk, v)  # keep topk_sl with k elements
            curr += v
            l += 1
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, festival())
