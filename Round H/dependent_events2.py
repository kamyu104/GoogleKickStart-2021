# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round H - Problem D. Dependent Events
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008d9970
#
# Time:  O(NlogN + QlogN)
# Space: O(NlogN)
#

from functools import partial

# Template:
# https://github.com/kamyu104/FacebookHackerCup-2021/blob/main/Round%202/chainblock.py
class TreeInfos(object):  # Time: O(NlogN), Space: O(NlogN), N is the number of nodes
    def __init__(self, children, cb=lambda *x:None, cb2=lambda *x:None):  # modified
        def preprocess(curr, parent):
            # depth of the node i
            D[curr] = 1 if parent == -1 else D[parent]+1
            # ancestors of the node i
            if parent != -1:
                P[curr].append(parent)
            i = 0
            while i < len(P[curr]) and i < len(P[P[curr][i]]):
                cb(P, curr, i)
                P[curr].append(P[P[curr][i]][i])
                i += 1
            cb2(curr, parent)  # added
            # the subtree of the node i is represented by traversal index L[i]..R[i]
            C[0] += 1
            L[curr] = C[0]

        def divide(curr, parent):
            stk.append(partial(postprocess, curr))
            for i in reversed(xrange(len(children[curr]))):
                child = children[curr][i]
                if child == parent:
                    continue
                stk.append(partial(divide, child, curr))
            stk.append(partial(preprocess, curr, parent))

        def postprocess(curr):
            R[curr] = C[0]

        N = len(children)
        L, R, D, P, C = [0]*N, [0]*N, [0]*N, [[] for _ in xrange(N)], [-1]
        stk = []
        stk.append(partial(divide, ROOT, -1))
        while stk:
            stk.pop()()
        assert(C[0] == N-1)
        self.L, self.R, self.D, self.P = L, R, D, P

    # Template:
    # https://github.com/kamyu104/FacebookHackerCup-2019/blob/master/Final%20Round/little_boat_on_the_sea.py
    def is_ancestor(self, a, b):  # includes itself
        return self.L[a] <= self.L[b] <= self.R[b] <= self.R[a]

    def lca(self, a, b):
        if self.D[a] > self.D[b]:
            a, b = b, a
        if self.is_ancestor(a, b):
            return a
        for i in reversed(xrange(len(self.P[a]))):  # O(logN)
            if i < len(self.P[a]) and not self.is_ancestor(self.P[a][i], b):
                a = self.P[a][i]
        return self.P[a][0]

def combine(a, b):
    return (a[0]*(1-b)+a[1]*b)%MOD

def calc_p_exp(p_exp, P, curr, i):
    p_exp[curr].append([combine(p_exp[curr][i], p_exp[P[curr][i]][i][k]) for k in xrange(2)])

def calc_p(p, p_exp, curr, parent):
    if curr != ROOT:
        p[curr] = combine(p_exp[curr][0], p[parent])

def calc_prob(p_exp, tree_infos, curr, lca):  # Time: O(logN)
    prob = [0, 1]
    for i in reversed(xrange(len(tree_infos.P[curr]))):  # O(logN)
        if i < len(tree_infos.P[curr]) and tree_infos.D[tree_infos.P[curr][i]] >= tree_infos.D[lca]:
            prob = [combine(prob, p_exp[curr][i][k]) for k in xrange(2)]
            curr = tree_infos.P[curr][i]
    assert(curr == lca)
    return prob

def dependent_events():
    N, Q = map(int, raw_input().strip().split())
    K = input()
    adj = [[] for _ in xrange(N)]
    p_exp = [[] for _ in xrange(N)]
    for c in xrange(1, N):
        P, A, B = map(int, raw_input().strip().split())
        adj[P-1].append(c)
        p_exp[c].append([(B*INV_DENOMINATOR)%MOD, (A*INV_DENOMINATOR)%MOD])
    p = [-1 for _ in xrange(N)]
    p[ROOT] = (K*INV_DENOMINATOR)%MOD
    tree_infos = TreeInfos(adj, cb=partial(calc_p_exp, p_exp), cb2=partial(calc_p, p, p_exp))
    result = []
    for _ in xrange(Q):
        u, v = map(int, raw_input().strip().split())
        u, v = u-1, v-1
        l = tree_infos.lca(u, v)
        pul, pvl = calc_prob(p_exp, tree_infos, u, l), calc_prob(p_exp, tree_infos, v, l)
        result.append(str(combine([(pul[k]*pvl[k])%MOD for k in xrange(2)], p[l])))
    return " ".join(result)

MOD = 10**9+7
DENOMINATOR = 10**6
INV_DENOMINATOR = pow(DENOMINATOR, MOD-2, MOD)  # Euler's Theorem, Fermat's Little Theorem
ROOT = 0
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, dependent_events())
