# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round C - Problem A. Smaller Strings
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ebe5e
#
# Time:  O(N)
# Space: O(1)
#    

def linear_congruence(a, m, b):  # Time: O(logN), the same as gcd, Space: O(logN)
    # gcd(a, m) = g and g|b, find x, s.t. ax % m = b % m
    # => (a%m)x = my+(b%m)
    # => gcd(m, a%m) = g and g|-(b%m), find y, s.t. my % (a%m) = -(b%m) % (a%m)
    # => y = linear_congruence(m, a%m, -(b%m))
    # => x = (my+(b%m))/(a%m)
    ambs = []
    while m:
        a, m, b = m, a%m, -(b%m)
        if m:
            ambs.append((m, a, -b))
    x = a  # a is gcd
    while ambs:
        a, m, b = ambs.pop()
        x = (m*x+b)//a
    return x

def smaller_strings():
    N, K = map(int, raw_input().strip().split())
    S = raw_input().strip()

    result = 0
    cnt = pow(K, (len(S)+1)//2-1, MOD)
    inv_K = linear_congruence(K, MOD, 1)
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
