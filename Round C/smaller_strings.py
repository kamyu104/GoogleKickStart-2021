# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round C - Problem A. Smaller Strings
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ebe5e
#
# Time:  O(N)
# Space: O(N)
#    

def smaller_strings():
    N, K = map(int, raw_input().strip().split())
    S = raw_input().strip()

    result = 0
    pow_of_2 = [1]
    for i in xrange((len(S)+1)//2-1):
        pow_of_2.append((cnt[-1]*K)%MOD)
    for i in xrange((len(S)+1)//2):
        result = (result+(ord(S[i])-ord('a'))*pow_of_2[-1-i])%MOD
    if S[:(len(S)+1)//2]+S[:len(S)//2][::-1] < S:
        result = (result+1)%MOD
    return result

MOD =10**9+7
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, smaller_strings())
