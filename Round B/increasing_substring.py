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

    result = []
    prev, cnt = -1, 0
    for c in S:
        if ord(c)-ord('A') <= prev:
            prev = -1
            cnt = 0
        prev = ord(c)-ord('A')
        cnt += 1
        result.append(cnt)
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, increasing_substring())
