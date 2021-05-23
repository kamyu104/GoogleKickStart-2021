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

    dp = [[[0.0]*(ROUNDS+1) for _ in xrange(ROUNDS+1)] for _ in xrange(ROUNDS+1)]
    dp[1][0][0] = dp[0][1][0] = dp[0][0][1] = W/3 + E/3
    backtracing = [[[None]*(ROUNDS+1) for _ in xrange(ROUNDS+1)] for _ in xrange(ROUNDS+1)]
    backtracing[1][0][0] = 'R'
    backtracing[0][1][0] = 'S'
    backtracing[0][0][1] = 'P'
    max_r = max_s = -1
    for r in xrange(ROUNDS+1):
        for s in xrange(ROUNDS+1-r):
            for p in xrange(ROUNDS+1-r-s):
                n = r+p+s
                if n-1 <= 0:
                    continue
                if r-1 >= 0:
                    if dp[r][s][p] < dp[r-1][s][p] + W*p/(n-1) + E*s/(n-1):
                        dp[r][s][p] = dp[r-1][s][p] + W*p/(n-1) + E*s/(n-1)
                        backtracing[r][s][p] = 'R'
                if s-1 >= 0:
                    if dp[r][s][p] < dp[r][s-1][p] + W*r/(n-1) + E*p/(n-1):
                        dp[r][s][p] = dp[r][s-1][p] + W*r/(n-1) + E*p/(n-1)
                        backtracing[r][s][p] = 'S'
                if p-1 >= 0:
                    if dp[r][s][p] < dp[r][s][p-1] + W*s/(n-1) + E*r/(n-1):
                        dp[r][s][p] = dp[r][s][p-1] + W*s/(n-1) + E*r/(n-1)
                        backtracing[r][s][p] = 'P'
            if max_r == max_s == -1 or dp[max_r][max_s][ROUNDS-max_r-max_s] < dp[r][s][ROUNDS-r-s]:
                max_r, max_s = r, s
    result = []
    r, s, p = max_r, max_s, ROUNDS-max_r-max_s
    while backtracing[r][s][p] is not None:
        result.append(backtracing[r][s][p])
        if backtracing[r][s][p] == 'R':
            r -= 1
        elif backtracing[r][s][p] == 'S':
            s -= 1
        else:
            p -= 1
    result.reverse()
    return "".join(result)
    
ROUNDS = 60
T, X = input(), input()
for case in xrange(T):
    print 'Case #%d: %s' % (case+1, rock_paper_scissors())
