# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round G - Problem B. Staying Hydrated
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b3a1c
#
# Time:  O(KlogK)
# Space: O(K)
#

from bisect import bisect_left

def min_pos(x):
    a = sorted(v[1] for v in x)
    left, lookup_l = [0]*(len(x)+1), {}
    for i in xrange(len(x)):
        left[i+1] = left[i]+a[i]
        lookup_l[a[i]] = i
    b = sorted(v[0] for v in x)
    right, lookup_r = [0]*(len(x)+1), {}
    for i in reversed(xrange(len(x))):
        right[i] = right[i+1]+b[i]
        lookup_r[b[i]] = i

    min_dist, result = float("inf"), None
    for v in sorted(set(a+b)):
        total = 0
        i = bisect_left(a, v+1)-1  # find max i s.t. a[i] <= v
        if 0 <= i:
            total += v*(lookup_l[a[i]]+1)-left[lookup_l[a[i]]+1]
        j = bisect_left(b, v)  # find min j s.t. b[j] >= v
        if j != len(b):
            total += right[lookup_r[b[j]]]-v*(len(b)-lookup_r[b[j]])
        if total < min_dist:
            min_dist = total
            result = v
    return result

def staying_hydrated():
    K = input()
    X, Y = [], []
    for _ in xrange(K):
        X1, Y1, X2, Y2 = map(int, raw_input().strip().split())
        X.append([X1, X2])
        Y.append([Y1, Y2])
    return '%s %s' % (min_pos(X), min_pos(Y))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, staying_hydrated())
