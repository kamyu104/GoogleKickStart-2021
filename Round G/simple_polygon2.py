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

    # if N == 3:
    #   - the triangle formed by (0, 1), (1, 0), (0, 0) covers 1 unit
    # elif N >= 4:
    #   - the triangle formed by last point (0, 1) and the first two points (0, 2), (1, 1) covers 1 unit,
    #     each of the rest points forming a new triangle covers 1 unit in the zig-zag shape
    # thus, the uncovered A will be A-(N-2)
    #   => let dy = A-(N-2) and adjust the first point (x, y) to (x, y+dy) to cover the rest of A
    #   => it is possible if dy = A-(N-2) >= 0
    #   => by pick's theorem, i >= 0 and b >= N => A = 2*i+b-2 >= N-2, which means A < (N-2) is impossible
    #   => A-(N-2) >= 0 iff possible
    if not (A-(N-2) >= 0):
        return "IMPOSSIBLE"
    if N != 3:
        # if N >= 4 => 2+dy = 2+(A-(N-2)) = A-N+4 <= MAX_A
        assert(2+(A-(N-2)) == A-N+4 <= MAX_A)
        result = [(0, A-N+4)]
        for i in xrange(1, N//2):
            result.append((i, 1 if i%2 else 2))
        for i in reversed(xrange((N+1)//2)):
            result.append((i, 1 if not i%2 or (i == (N+1)//2-1 and N%4 == 3) else 0))
    else:
        # if N == 3 => 1+dy = 1+(A-(N-2)) = A <= MAX_A
        assert(1+(A-(N-2)) == A <= MAX_A)
        result = [(0, A), (1, 0), (0, 0)]
    return "POSSIBLE\n" + "\n".join(map(lambda x: "%s %s"%(x[0], x[1]), result))

MAX_A = 10**9
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, simple_polygon())

