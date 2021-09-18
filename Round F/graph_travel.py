# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round F - Problem D. Graph Travel
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000888764
#
# Time:  O(N * 2^N + M)
# Space: O(2^N)
#

def graph_travel():
    N, M, K = map(int, raw_input().strip().split())
    shields = [map(int, raw_input().strip().split()) for _ in xrange(N)]
    adj = [0]*N
    for _ in xrange(M):
        X, Y = map(int, raw_input().strip().split())
        adj[X] |= 1<<Y
        adj[Y] |= 1<<X

    dp = [0]*(1<<N)
    bit = 1
    for _ in xrange(N):
        dp[bit] = 1
        bit <<= 1
    result = 0
    for mask in xrange(1, len(dp)):
        total = all_reachables = 0
        bit = 1
        for i in xrange(N):
            if mask&bit:
                total += shields[i][2]
                all_reachables |= adj[i]
            bit <<= 1
        if total == K:
            result += dp[mask]
        bit = 1
        for i in xrange(N):
            if not (mask&bit) and (all_reachables&bit) and shields[i][0] <= total <= shields[i][1]:
                dp[mask|bit] += dp[mask]
            bit <<= 1
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, graph_travel())
