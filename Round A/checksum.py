# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round A - Problem B. L Shaped Plots
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509
#
# Time:  O(N^2), pass in PyPy2 but Python2
# Space: O(N^2)
#

def max_prim(adj):  # Time: O(N^2), Space: O(N)
    if not adj:
        return 0
    result = 0
    nodes = list(set(i for i, _ in adj.iterkeys()))
    lookup = [False]*len(nodes)
    max_e = [0]*len(nodes)
    for i in xrange(len(nodes)):
        u = -1
        for v in xrange(len(nodes)):
            if lookup[v]:
                continue
            if u == -1 or max_e[v] > max_e[u]:
                u = v
        lookup[u] = True
        result += max_e[u]
        for v in xrange(len(nodes)):
            if (nodes[u], nodes[v]) in adj:
                max_e[v] = max(max_e[v], adj[nodes[u], nodes[v]])
    return result

def checksum():
    N = input()
    A = [map(int, raw_input().strip().split()) for _ in xrange(N)]
    B = [map(int, raw_input().strip().split()) for _ in xrange(N)]
    R = map(int, raw_input().strip().split())
    C = map(int, raw_input().strip().split())

    total = 0
    adj = {}
    for i in xrange(len(A)):
        for j in xrange(len(A[0])):
            if A[i][j] == -1:
                adj[i, N+j] = adj[N+j, i] = B[i][j]  # Space: O(N^2)
                total += B[i][j]
    return total - max_prim(adj)

INF = float("inf")
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, checksum())
