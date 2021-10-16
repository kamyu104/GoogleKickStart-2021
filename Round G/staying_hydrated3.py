# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round G - Problem B. Staying Hydrated
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004362d6/00000000008b3a1c
#
# Time:  O(K) on average
# Space: O(K)
#

from random import randint

def nth_element(nums, n, compare=lambda a, b: a < b):
    def tri_partition(nums, left, right, target, compare):
        mid = left
        while mid <= right:
            if nums[mid] == target:
                mid += 1
            elif compare(nums[mid], target):
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
        return left, right

    left, right = 0, len(nums)-1
    while left <= right:
        pivot_idx = randint(left, right)
        pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx], compare)
        if pivot_left <= n <= pivot_right:
            return
        elif pivot_left > n:
            right = pivot_left-1
        else:  # pivot_right < n.
            left = pivot_right+1

def min_pos(arr):
    # let f(x) be the distance function for x in arr:
    #   - when x starts from smallest to largest in arr,
    #     f(x) will be strictly decreasing at the begining, then constant,
    #     and finally strictly increasing
    #   - since the 2 medians of arr are the exact endpoints where f(x) either starts or ends to be constant,
    #     so the answer is the smaller median which meets the problem constraints
    nth_element(arr, (len(arr)+1)//2-1)
    return arr[(len(arr)+1)//2-1]

def staying_hydrated():
    K = input()
    X, Y = [], []
    for _ in xrange(K):
        X1, Y1, X2, Y2 = map(int, raw_input().strip().split())
        X.extend([X1, X2])
        Y.extend([Y1, Y2])

    return "%s %s" % (min_pos(X), min_pos(Y))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, staying_hydrated())
