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

'''
N = 60
def backtracing(W, E, dp, r, s, p):
    result = []
    while r+s+p:
        if r-1 >= 0 and dp[r][s][p] == (dp[r-1][s][p] + (W*p+E*s)/((r-1)+p+s) if (r-1)+s+p != 0 else (W+E)/3):
            result.append('R')
            r -= 1
        elif s-1 >= 0 and dp[r][s][p] == (dp[r][s-1][p] + (W*r+E*p)/(r+(s-1)+p) if r+(s-1)+p != 0 else (W+E)/3):
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
            for p in xrange(N+1-r-s-1):  # skip r+s+p = N
                dp[r+1][s][p] = max(dp[r+1][s][p], dp[r][s][p] + (W*p+E*s)/(r+s+p) if r+s+p != 0 else (W+E)/3)
                dp[r][s+1][p] = max(dp[r][s+1][p], dp[r][s][p] + (W*r+E*p)/(r+s+p) if r+s+p != 0 else (W+E)/3)
                dp[r][s][p+1] = max(dp[r][s][p+1], dp[r][s][p] + (W*s+E*r)/(r+s+p) if r+s+p != 0 else (W+E)/3)
            if max_r == -1 or dp[max_r][max_s][N-max_r-max_s] < dp[r][s][N-r-s]:
                max_r, max_s = r, s
    return backtracing(W, E, dp, max_r, max_s, N-max_r-max_s)

# precompute
RESULT = [solve(1.0, 1.0/x) for x in [1, 2, 10, float("inf")]]
'''
RESULT = ['PSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSR', 'PRRSSSSPPPPPPPPRRRRRRRRRRRRRRRRSSSSSSSSSSSSSSSSSSSPPPPPPPPPP', 'SPPPPRRRRRRRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSSSSPPPPPPPPPPPPPPP', 'PRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSSSSSSPPPPPPPPPPPPPPPPPPPPPPP']
T, X = input(), input()
for case in xrange(T):
    print 'Case #%d: %s' % (case+1, rock_paper_scissors())
