# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round H - Problem A. Transform the String
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008da461
#
# Time:  O(N)
# Space: O(1)
#

def transform_the_string():
    S, F = [map(lambda x: ord(x)-ord('a'), list(raw_input().strip())) for _ in xrange(2)]
    dist = {c:min(min(abs(f-c), 26-abs(f-c)) for f in F) for c in set(S)}
    return sum(dist[c] for c in S)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, transform_the_string())
