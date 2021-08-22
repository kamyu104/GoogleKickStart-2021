# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round E - Problem A. Shuffled Anagrams
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000043585c/000000000085a152
#
# Time:  O(N)
# Space: O(N)
#

from collections import defaultdict

def shuffled_anagrams():
    S = raw_input().strip()

    lookup = defaultdict(list)
    for i, c in enumerate(S):
        lookup[c].append(i)
    max_shift = len(max(lookup.itervalues(), key=len))
    if max_shift*2 > len(S):
        return "IMPOSSIBLE"
    idxs_grouped_by_char = []
    for idxs in lookup.itervalues():
        idxs_grouped_by_char.extend(idxs)
    result = [0]*len(S)
    for i in xrange(len(S)):
        result[idxs_grouped_by_char[i]] = S[idxs_grouped_by_char[(i+max_shift)%len(S)]]
    return "".join(result)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, shuffled_anagrams())
