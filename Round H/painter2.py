# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round H - Problem B. Painter
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008d9a88
#
# Time:  O(N)
# Space: O(1)
#
# one-pass solution
#

def painter():
    N = input()
    P = raw_input().strip()
    result = curr = 0
    for c in P:
        x = COLORS[c]
        if not curr^x:
            continue
        if not curr&x:
            result += COUNT[x]
        elif (curr&x) == curr:
            result += COUNT[curr^x]
        elif (curr&x) != x:
            result += COUNT[x^(curr&x)]
        curr = x
    return result

COLORS = {'U':0b000,
          'R':0b001, 'Y':0b010, 'B':0b100,
          'O':0b011, 'P':0b101, 'G':0b110,
          'A':0b111}
COUNT = {0b000:0,
         0b001:1, 0b010:1, 0b100:1,
         0b011:2, 0b101:2, 0b110:2,
         0b111:3}
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, painter())
