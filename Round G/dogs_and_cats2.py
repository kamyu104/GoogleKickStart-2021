# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round G - Problem A. Dogs and Cats
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b3771
#
# Time:  O(N)
# Space: O(1)
#

def dogs_and_cats():
    N, D, C, M = map(int, raw_input().strip().split())
    S = list(raw_input().strip())

    while S and S[-1] == 'C':
        S.pop()
    for c in S:
        if c == 'D':
            if D == 0:
                return "NO"
            D -= 1
            C += M
        else:
            if C == 0:
                return "NO"
            C -= 1
    return "YES"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, dogs_and_cats())
