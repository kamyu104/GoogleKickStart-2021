# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round C - Problem C. Rock Paper Scissors
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec28e
#
# Time:  O(N)
# Space: O(1)
#

def rock_paper_scissors():
    W, E = map(int, raw_input().strip().split())

    if W == E:
        return RESULT[0]
    if W == E*2:
        return RESULT[1]
    if W == E*10:
        return RESULT[2]
    return RESULT[3]

N = 60
'''
def backtracing(W, E, dp, r, s, p):
    result = []
    while r+p+s:
        if r-1 >= 0 and dp[r][s][p] == (dp[r-1][s][p] + (W*p+E*s)/(r+p+s-1) if r+p+s-1 != 0 else (W+E)/3):
            result.append('R')
            r -= 1
        elif s-1 >= 0 and dp[r][s][p] == (dp[r][s-1][p] + (W*r+E*p)/(r+p+s-1) if r+p+s-1 != 0 else (W+E)/3):
            result.append('S')
            s -= 1
        else:
            result.append('P')
            p -= 1
    result.reverse()
    return "".join(result)

def solve(W, E):
    dp = [[[0.0]*(N+1) for _ in xrange(N+1)] for _ in xrange(N+1)]
    max_r = max_s = -1
    for r in xrange(N+1):
        for s in xrange(N+1-r):
            for p in xrange(N+1-r-s):
                if r-1 >= 0:
                    dp[r][s][p] = max(dp[r][s][p], dp[r-1][s][p] + (W*p+E*s)/(r+p+s-1) if r+p+s-1 != 0 else (W+E)/3)
                if s-1 >= 0:
                    dp[r][s][p] = max(dp[r][s][p], dp[r][s-1][p] + (W*r+E*p)/(r+p+s-1) if r+p+s-1 != 0 else (W+E)/3)
                if p-1 >= 0:
                    dp[r][s][p] = max(dp[r][s][p], dp[r][s][p-1] + (W*s+E*r)/(r+p+s-1) if r+p+s-1 != 0 else (W+E)/3)
            if max_r == -1 or dp[max_r][max_s][N-max_r-max_s] < dp[r][s][N-r-s]:
                max_r, max_s = r, s
    return backtracing(W, E, dp, max_r, max_s, N-max_r-max_s)

# precompute
RESULT = [solve(1.0, 1.0), solve(1.0, 1.0/2.0), solve(1.0, 1.0/10.0), solve(1.0, 1.0/float("inf"))]
'''
RESULT = ['PSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSR', 'PRRSSSSPPPPPPPPRRRRRRRRRRRRRRRRSSSSSSSSSSSSSSSSSSSPPPPPPPPPP', 'SPPPPRRRRRRRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSSSSPPPPPPPPPPPPPPP', 'PRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSSSSSSPPPPPPPPPPPPPPPPPPPPPPP']
T, X = input(), input()
for case in xrange(T):
    print 'Case #%d: %s' % (case+1, rock_paper_scissors())
