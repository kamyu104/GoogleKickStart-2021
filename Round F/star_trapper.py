# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round F - Problem C. Star Trapper
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000888d45
#
# Time:  O(N^3), pass in PyPy2 but Python2
# Space: O(1)
#

def ccw(A, B, C):
    return (B[0]-A[0])*(C[1]-A[1]) - (B[1]-A[1])*(C[0]-A[0])

def vector(a, b):
    return [a[i]-b[i] for i in xrange(len(a))]

def length(a):
    return sum(x**2 for x in a)**0.5

def is_between(t, a, b):
    return t not in (a, b) and abs(length(vector(a, t))+length(vector(t, b)) - length(vector(a, b))) < EPS

def point_inside_triangle(T, A, B, C):
    d1, d2, d3 = ccw(T, A, B),  ccw(T, B, C),  ccw(T, C, A)
    return (d1 > 0 and d2 > 0 and d3 > 0) or (d1 < 0 and d2 < 0 and d3 < 0)

def star_trapper():
    N = input()
    points = [map(int, raw_input().strip().split()) for _ in xrange(N)]
    target = map(int, raw_input().strip().split())
    result = float("inf")
    for i in xrange(N):
        for j in xrange(i+1, N):
            is_two_triangles = is_between(target, points[i], points[j])
            min_perimeters = [float("inf"), float("inf")]
            for k in xrange(N):
                if k == i or k == j:
                    continue
                if point_inside_triangle(target, points[i], points[j], points[k]):
                    result = min(result, length(vector(points[i], points[j]))+length(vector(points[j], points[k]))+length(vector(points[k], points[i])))
                if is_two_triangles:
                    sign = ccw(points[i], points[j], points[k])
                    if sign:
                        min_perimeters[sign > 0] = min(min_perimeters[sign > 0], (length(vector(points[i], points[k]))+length(vector(points[j], points[k]))))
            result = min(result, sum(min_perimeters))
    return result if result != float("inf") else "IMPOSSIBLE"

EPS = 1e-9
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, star_trapper())
