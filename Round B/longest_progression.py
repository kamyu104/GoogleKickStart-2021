# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round B - Problem B. Longest Progression
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a3a5
#
# Time:  O(N)
# Space: O(N)
#

def longest_progression():
    N = input()
    A = map(int, raw_input().strip().split())

    left, right = {}, {}
    result, last, d, count = 1, 0, None, 0
    for i in xrange(N-1):
        if A[i+1]-A[i] == d:
            count += 1
            continue
        if d is not None:
            left[last] = right[i] = (d, count)
            last = i
        result = max(result, count)
        d = A[i+1]-A[i]
        count = 2
    left[last] = right[N-1] = (d, count)
    result = max(result, count)
    for i in xrange(N):
        if i+1 in left:
            result = max(result, int(i-1 >=0 and A[i+1]-A[i-1] == 2*left[i+1][0])+1+left[i+1][1])
        if i-1 in right:
            result = max(result, right[i-1][1]+1+int(i+1 < N and A[i+1]-A[i-1] == 2*right[i-1][0]))
        if i+1 in left and i-1 in right and \
           left[i+1][0] == right[i-1][0] and A[i+1]-A[i-1] == 2*right[i-1][0]:
           result = max(result, right[i-1][1]+1+left[i+1][1])
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, longest_progression())
