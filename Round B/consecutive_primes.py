# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round B - Problem C. Consecutive Primes
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a8e6
#
# Time:  O(N^(1/4) * MAX_GAP)
# Space: O(1)
#

def is_prime(n):
    if n <= 3:
        return n > 1
    if n%2 == 0 or n%3 == 0:
        return False
    return all(n%i and n%(i+2) for i in xrange(5, int(n**(0.5))+1, 6))

def consecutive_primes():
    N = input()

    sqrt_N = int(N**(0.5))
    primes = []
    for i in reversed(xrange(max(sqrt_N-(2*MAX_GAP-1), 2), sqrt_N+(MAX_GAP-1)+1)):
        if not is_prime(i):
            continue
        primes.append(i)
        if len(primes) == 2:
            if primes[-1]*primes[-2] <= N:
                break
            primes = primes[1:]
    return primes[-1]*primes[-2]

# https://en.wikipedia.org/wiki/Prime_gap
MAX_GAP = 282  # MAX_N = 10^18, max prime >= 10^9 => p(n+1)-gn >= 10^9, min n = 30 => gn = 282
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, consecutive_primes())
