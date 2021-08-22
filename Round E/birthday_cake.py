# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round E - Problem B. Birthday Cake
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000043585c/000000000085a285
#
# Time:  O(1)
# Space: O(1)
#

def ceil_divide(a, b):
    return (a+(b-1))//b

def birthday_cake():
    R, C, K = map(int, raw_input().strip().split())
    r1, c1, r2, c2 = map(int, raw_input().strip().split())

    n, m = r2-r1+1, c2-c1+1
    save = ceil_divide(m, K)*(int(r1 == 1)+int(r2 == R)) + ceil_divide(n, K)*(int(c1 == 1)+int(c2 == C))
    partial = 2*ceil_divide(n, K)+2*ceil_divide(m, K)-save if save else \
              min(2*ceil_divide(m, K)+ceil_divide(n, K)+ceil_divide(min(r2, R-(r1-1)), K),
                  2*ceil_divide(n, K)+ceil_divide(m, K)+ceil_divide(min(c2, C-(c1-1)), K))
    full = (n*m-1) + (ceil_divide(n, K)-1)*(ceil_divide(m, K)-1)
    return partial+full  # cut of partially delicious cake and cut of fully delicious cake

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, birthday_cake())
