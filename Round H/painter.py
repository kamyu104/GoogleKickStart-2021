# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round H - Problem B. Painter
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008d9a88
#
# Time:  O(N)
# Space: O(1)
#

def f(P, x):
    result, last = 0, -2
    for i, c in enumerate(P):
        if x not in COLORS[c]:
            continue
        if last != i-1:
            result += 1
        last = i
    return result

def painter():
    N = input()
    P = raw_input().strip()
    return f(P, 'R')+f(P, 'Y')+f(P, 'B')

COLORS = {'U':set(),
          'R':{'R'}, 'Y':{'Y'}, 'B':{'B'},
          'O':{'R', 'Y'}, 'P':{'R', 'B'}, 'G':{'Y', 'B'},
          'A':{'R', 'Y', 'B'}}
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, painter())
