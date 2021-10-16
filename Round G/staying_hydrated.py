# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round G - Problem B. Staying Hydrated
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b3a1c
#
# Time:  O(KlogK)
# Space: O(K)
#

from bisect import bisect_left

def min_pos(arr):
    a = sorted(x[1] for x in arr)
    left, lookup_l = [0]*(len(arr)+1), {}
    for i in xrange(len(arr)):
        left[i+1] = left[i]+a[i]
        lookup_l[a[i]] = i
    b = sorted(x[0] for x in arr)
    right, lookup_r = [0]*(len(arr)+1), {}
    for i in reversed(xrange(len(arr))):
        right[i] = right[i+1]+b[i]
        lookup_r[b[i]] = i

    min_dist, result = float("inf"), None
    for x in sorted(set(a+b)):
        total = 0
        i = bisect_left(a, x+1)-1  # find max i s.t. a[i] <= x
        if 0 <= i:
            i = lookup_l[a[i]]
            total += x*(i+1)-left[i+1]
        i = bisect_left(b, x)  # find min j s.t. b[i] >= x
        if i != len(b):
            i = lookup_r[b[i]]
            total += right[i]-x*(len(b)-i)
        if total < min_dist:
            min_dist = total
            result = x
    return result

def staying_hydrated():
    K = input()
    X, Y = [], []
    for _ in xrange(K):
        X1, Y1, X2, Y2 = map(int, raw_input().strip().split())
        X.append([X1, X2])
        Y.append([Y1, Y2])

    return "%s %s" % (min_pos(X), min_pos(Y))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, staying_hydrated())
