# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round B - Problem A. Increasing Substring
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a882
#
# Time:  O(N^(1/4) * MAX_GAP)
# Space: O(1)
#

def is_prime(n):
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

def consecutive_primes():
    N = input()

    sqrt_N = int(N**(0.5))
    if sqrt_N**2 < N:
        sqrt_N += 1
    primes = []
    for i in reversed(xrange(max(sqrt_N-2*MAX_GAP, 2), sqrt_N+MAX_GAP+1)):
        if not is_prime(i):
            continue
        primes.append(i)
        if len(primes) >= 2 and primes[-1]*primes[-2] <= N:
            break 
    return primes[-1]*primes[-2]

# https://en.wikipedia.org/wiki/Prime_gap
MAX_GAP = 282  # MAX_N = 10^18, max prime >= 10^9 => p(n+1)-gn >= 10^9, min n = 30 => gn = 282
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, consecutive_primes())
