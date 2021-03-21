# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round A - Problem B. L Shaped Plots
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509
#
# Time:  O(R * C)
# Space: O(min(R, C))
#

def count(x, y):
    return max((min(x//2, y)-1) + (min(x, y//2)-1), 0)

def grid(G, i, j):
    return G[i][j] if len(G) > len(G[0]) else G[j][i]

def l_shaped_plots():
    R, C = map(int, raw_input().strip().split())
    G = [map(int, raw_input().strip().split()) for _ in xrange(R)]

    result = 0
    for direction in (lambda x: x, reversed):
        dp = [0]*min(R, C)
        for i in direction(xrange(max(R, C))):
            for direction in (lambda x:x, reversed):
                curr = 0
                for j in direction(xrange(min(R, C))):
                    if not grid(G, i, j):
                        dp[j] = 0
                        curr = 0
                        continue
                    dp[j] += 1
                    curr += 1
                    result += count(curr, (dp[j]+1)//2)
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, l_shaped_plots())
