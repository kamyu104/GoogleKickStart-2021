# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round E - Problem D. Increasing Sequence Card Game
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000043585c/000000000085a709
#
# Time:  precompute: O(EPS^(-1))
#        runtime:    O(1)
# Space: O(EPS^(-1))
#

from math import log

def increasing_sequence_card_game():
    N = input()

    return DP[N] if N < len(DP) else DP[-1]+log(N+1)-log(len(DP))  # assumed log(x) is O(1) time

EPS = 1e-6
DP = [0.0]*(int(1/EPS)+1)
for i in xrange(1, len(DP)):
    DP[i] = DP[i-1]+1.0/i
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, increasing_sequence_card_game())
