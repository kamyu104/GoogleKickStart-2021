# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round B - Problem A. Increasing Substring
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a882
#
# Time:  O(N)
# Space: O(1)
#

def increasing_substring():
    N = input()
    S = raw_input()

    result = [1]*N
    for i in xrange(1, N):
        if S[i-1] < S[i]:
            result[i] = result[i-1]+1
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, increasing_substring())
