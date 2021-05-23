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

    result = 0
    cnt = pow(K, (len(S)+1)//2-1, MOD)  # Time:  O(logN)
    inv_K = pow(K, MOD-2, MOD)  # Time:  O(logN), Fermat's little theorem, k^(p-1) % p = 1 => k^(p-2) % p = k^(-1) % p
    for i in xrange((len(S)+1)//2):
        result = (result+(ord(S[i])-ord('a'))*cnt)%MOD
        cnt = (cnt*inv_K)%MOD
    for i in reversed(xrange(len(S)//2)):
        if S[i] != S[-1-i]:
            result = (result+int(S[i] < S[-1-i]))%MOD
            break
    return result

MOD =10**9+7
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, smaller_strings())
