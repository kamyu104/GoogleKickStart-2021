# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round C - Problem C. Rock Paper Scissors
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec28e
#
# Time:  O(N^3)
# Space: O(N^3)
#

def rock_paper_scissors():
    W, E = map(float, raw_input().strip().split())

    dp = [[[0.0]*(N+1) for _ in xrange(N+1)] for _ in xrange(N+1)]
    dp[1][0][0] = dp[0][1][0] = dp[0][0][1] = W/3 + E/3
    max_r = max_s = -1
    for r in xrange(N+1):
        for s in xrange(N+1-r):
            for p in xrange(N+1-r-s):
                n = r+p+s
                if n-1 <= 0:
                    continue
                if r-1 >= 0:
                    if dp[r][s][p] < dp[r-1][s][p] + W*p/(n-1) + E*s/(n-1):
                        dp[r][s][p] = dp[r-1][s][p] + W*p/(n-1) + E*s/(n-1)
                if s-1 >= 0:
                    if dp[r][s][p] < dp[r][s-1][p] + W*r/(n-1) + E*p/(n-1):
                        dp[r][s][p] = dp[r][s-1][p] + W*r/(n-1) + E*p/(n-1)
                if p-1 >= 0:
                    if dp[r][s][p] < dp[r][s][p-1] + W*s/(n-1) + E*r/(n-1):
                        dp[r][s][p] = dp[r][s][p-1] + W*s/(n-1) + E*r/(n-1)
            if max_r == -1 or dp[max_r][max_s][N-max_r-max_s] < dp[r][s][N-r-s]:
                max_r, max_s = r, s
    result = []
    r, s, p = max_r, max_s, N-max_r-max_s
    n = r+s+p
    while n:
        if r and (n == 1 or dp[r][s][p] == dp[r-1][s][p] + W*p/(n-1) + E*s/(n-1)):
            result.append('R')
            r -= 1
        elif s and (n == 1 or dp[r][s][p] == dp[r][s-1][p] + W*r/(n-1) + E*p/(n-1)):
            result.append('S')
            s -= 1
        else:
            result.append('P')
            p -= 1
        n -= 1
    result.reverse()
    return "".join(result)
    
N = 60
T, X = input(), input()
for case in xrange(T):
    print 'Case #%d: %s' % (case+1, rock_paper_scissors())
