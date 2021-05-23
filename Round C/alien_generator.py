# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round C - Problem B. Alien Generator
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec1cb
#
# Time:  O(sqrt(G))
# Space: O(1)
#

def alien_generator():
    G = input()
    result = 0
    x = 1
    while (1+x)*x//2 <= G:
        # K*x + (x+1)*x//2 = G
        if (G-(x+1)*x//2)%x == 0:
            result += 1
        x += 1
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, alien_generator())
