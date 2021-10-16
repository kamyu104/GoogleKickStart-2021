# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round G - Problem D. Simple Polygon
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b36f9
#
# Time:  O(N)
# Space: O(1)
#

def simple_polygon():
    N, A = map(int, raw_input().strip().split())
    if N-A > 2:
        return "IMPOSSIBLE"
    if N == 3:
        result = [(0, 0), (0, 1), (A, 0)]
    else:
        assert(A-N+4 <= MAX_A)
        # if A-N+4 > MAX_A,
        # => 3 <= N < A-MAX_A+4 <= 4,
        # => N = 3
        # => -><-
        result = [(0, A-N+4)]
        for i in xrange(1, N//2):
            result.append((i, 1 if i%2 else 2))
        for i in reversed(xrange((N+1)//2)):
            result.append((i, 1 if not i%2 or (i == (N+1)//2-1 and N%4 == 3) else 0))
    return "POSSIBLE\n" + "\n".join(map(lambda x: "%s %s"%(x[0], x[1]), result))

MAX_A = 10**9
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, simple_polygon())

