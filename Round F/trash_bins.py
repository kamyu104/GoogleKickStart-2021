# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round F - Problem A. Trash Bins
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887c32
#
# Time:  O(N)
# Space: O(N)
#

def trash_bins():
    N = input()
    S = raw_input().strip()

    left = [None]*N
    curr = float("-inf")
    for i, c in enumerate(S):
        if c == '1':
            curr = i
        left[i] = curr
    result = 0
    curr = float("inf")
    for i in reversed(xrange(len(S))):
        if S[i] == '1':
            curr = i
        result += min(i-left[i], curr-i)
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, trash_bins())
