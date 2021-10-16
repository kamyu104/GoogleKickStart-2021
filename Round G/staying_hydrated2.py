# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round G - Problem B. Staying Hydrated
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b3a1c
#
# Time:  O(KlogK)
# Space: O(K)
#

def min_pos(arr):
    # let f(x) be the distance function for x in arr:
    #   - when x starts from smallest to largest in arr,
    #     f(x) will be strictly decreasing at the begining, then constant,
    #     and finally strictly increasing
    #   - since the 2 medians of arr are the exact endpoints where f(x) either starts or ends to be constant,
    #     so the answer is the smaller median which meets the problem constraints
    arr.sort()
    return arr[(len(arr)+1)//2-1]

def staying_hydrated():
    K = input()
    X, Y = [], []
    for _ in xrange(K):
        X1, Y1, X2, Y2 = map(int, raw_input().strip().split())
        X.extend([X1, X2])
        Y.extend([Y1, Y2])

    return '%s %s' % (min_pos(X), min_pos(Y))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, staying_hydrated())
