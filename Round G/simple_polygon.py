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

    # the last point and the first two points increase 1 unit,
    # each of the rest points increases 1 unit,
    # so the first point should be (0, 2+dy) to cover extra A,
    # where dy = A-(N-2) >= 0 iff possible
    if not (A-(N-2) >= 0):
        return "IMPOSSIBLE"
    # 2+dy = 2+(A-(N-2)) = A-N+4 <= MAX_A iff A != MAX_A or N != 3
    if A != MAX_A or N != 3:
        assert(2+(A-(N-2)) <= MAX_A)
        result = [(0, 2+(A-(N-2)))]
        for i in xrange(1, N//2):
            result.append((i, 1 if i%2 else 2))
        for i in reversed(xrange((N+1)//2)):
            result.append((i, 1 if not i%2 or (i == (N+1)//2-1 and N%4 == 3) else 0))
    else:
        result = [(0, A), (1, 0), (0, 0)]
    return "POSSIBLE\n" + "\n".join(map(lambda x: "%s %s"%(x[0], x[1]), result))

MAX_A = 10**9
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, simple_polygon())

