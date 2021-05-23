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
    result, l = 0, 1
    while (1+l)*l//2 <= G:
        # K*l + (1+l)*l//2 = G
        if (G-(l+1)*l//2)%l == 0:
            result += 1
        l += 1
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, alien_generator())
