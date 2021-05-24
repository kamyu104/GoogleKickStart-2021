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
def backtracing(W, E, dp):
    result = []
    r = s = p = 0
    while r+s+p < N:
        result.append(dp[r][s][p][1])
        if result[-1] == 'R':
            r += 1
        elif result[-1] == 'S':
            s += 1
        else:
            p += 1
    return "".join(result)

def solve(W, E):
    dp = [[[[0.0, ''] for _ in xrange(N+1)] for _ in xrange(N+1)] for _ in xrange(N+1)]
    for r in reversed(xrange(N+1)):
        for s in reversed(xrange(N+1-r)):
            for p in reversed(xrange(N+1-r-s-1)):
                dp[r][s][p] = max(dp[r][s][p], [dp[r+1][s][p][0] + ((W*p+E*s)/(r+s+p) if r+s+p != 0 else (W+E)/3), 'R'])
                dp[r][s][p] = max(dp[r][s][p], [dp[r][s+1][p][0] + ((W*r+E*p)/(r+s+p) if r+s+p != 0 else (W+E)/3), 'S'])
                dp[r][s][p] = max(dp[r][s][p], [dp[r][s][p+1][0] + ((W*s+E*r)/(r+s+p) if r+s+p != 0 else (W+E)/3), 'P'])
    return backtracing(W, E, dp)

# precompute
RESULT = [solve(1.0, 1.0/x) for x in [1, 2, 10, float("inf")]]
'''
RESULT = ['SRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRP', 'SPPRRRRSSSSSSSSPPPPPPPPPPPPPPPPRRRRRRRRRRRRRRRRRRRSSSSSSSSSS', 'SPPPPRRRRRRRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSSSSPPPPPPPPPPPPPPP', 'SPPPPPPPPPRRRRRRRRRRRRRRRRRRRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSS']
T, X = input(), input()
for case in xrange(T):
    print 'Case #%d: %s' % (case+1, rock_paper_scissors())
