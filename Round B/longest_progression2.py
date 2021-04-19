# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round B - Problem B. Longest Progression
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a3a5
#
# Time:  O(N)
# Space: O(1)
#

def longest_progression():
    N = input()
    A = map(int, raw_input().strip().split())

    dp = [0]*4
    dp_skip = [0]*4  # replace A[i-2]
    result = 0
    for i in xrange(N):
        dp[i%4] = min(i+1, 2)
        dp_skip[i%4] = min(i+1, 2+1)
        result = max(result, min(dp[i%4]+1, N), dp_skip[i%4])
        if i < 2:
            continue
        if A[i]-A[i-1] == A[i-1]-A[i-2]:  # no replace
            dp[i%4] = dp[(i-1)%4]+1
            dp_skip[i%4] = dp_skip[(i-1)%4]+1
            result = max(result, min(dp[i%4]+1, N), dp_skip[i%4])
        if i < 3:
            continue
        if A[i]-A[i-2] == 2*(A[i-2]-A[i-3]):  # replace A[i-1]
            result = max(result, dp[(i-2)%4]+1+1)
        if dp_skip[i%4] == 3 and 2*(A[i]-A[i-1]) == A[i-1]-A[i-3]:  # replace A[i-2]
            dp_skip[i%4] = 4
            result = max(result, dp_skip[i%4])
        if i < 4:
            continue
        if A[i]-A[i-1] == A[i-3]-A[i-4] and 2*(A[i]-A[i-1]) == A[i-1]-A[i-3]:  # replace A[i-2]
            dp_skip[i%4] = max(dp_skip[i%4], dp[(i-3)%4]+1+2)
            result = max(result, dp_skip[i%4])
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, longest_progression())
