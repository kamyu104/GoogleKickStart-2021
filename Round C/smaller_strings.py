# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round C - Problem A. Smaller Strings
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ebe5e
#
# Time:  O(N)
# Space: O(1)
#  

def smaller_strings():
    N, K = map(int, raw_input().strip().split())
    S = raw_input().strip()

    result, cnt = 0, 1
    has_diff = False
    for i in reversed(xrange((len(S)+1)//2)):
        result = (result+(ord(S[i])-ord('a'))*cnt)%MOD
        cnt = (cnt*K)%MOD
        if has_diff:
            continue
        if S[i] != S[-1-i]:
            has_diff = True
            result = (result+int(S[i] < S[-1-i]))%MOD
    return result

MOD =10**9+7
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, smaller_strings())
