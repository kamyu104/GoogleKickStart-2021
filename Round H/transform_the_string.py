# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round H - Problem A. Transform the String
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008da461
#
# Time:  O(N)
# Space: O(1)
#

def transform_the_string():
    S, F = [raw_input().strip() for _ in xrange(2)]

    dist = {c:min(min(abs((ord(f)-ord('a'))-(ord(c)-ord('a'))), 26-abs((ord(f)-ord('a'))-(ord(c)-ord('a')))) for f in F) for c in set(list(S))}
    return sum(dist[c] for c in S)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, transform_the_string())
