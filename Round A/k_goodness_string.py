# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round A - Problem A. K-Goodness String
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cca3
#
# Time:  O(N)
# Space: O(1)
#

def k_goodness_string():
    N, K = map(int, raw_input().strip().split())
    S = raw_input().strip()

    return abs(sum(int(S[i] != S[N-1-i]) for i in xrange(N//2))-K)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, k_goodness_string())
