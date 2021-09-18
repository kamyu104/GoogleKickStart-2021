# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round F - Problem C. Star Trapper
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000888d45
#
# Time:  O(N^3), pass in PyPy2 but Python2
# Space: O(1)
#

def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def vector(a, b):
    return [a[i]-b[i] for i in xrange(len(a))]

def length(a):
    return sum(x**2 for x in a)**0.5

def inner_product(a, b):
    return sum(a[i]*b[i] for i in xrange(len(a)))

def is_between(t, a, b):
    return ccw(t, a, b) == 0 and 0 < inner_product(vector(a, t), vector(a, b)) < inner_product(vector(a, b), vector(a, b))

def is_inside_triangle(t, a, b, c):
    d1, d2, d3 = ccw(t, a, b),  ccw(t, b, c),  ccw(t, c, a)
    return (d1 > 0 and d2 > 0 and d3 > 0) or (d1 < 0 and d2 < 0 and d3 < 0)

def star_trappers():
    N = input()
    points = [map(int, raw_input().strip().split()) for _ in xrange(N)]
    target = map(int, raw_input().strip().split())

    result = float("inf")
    for i in xrange(N):
        for j in xrange(i+1, N):
            is_between_edge = is_between(target, points[i], points[j])
            min_perimeters = [float("inf")]*2
            for k in xrange(N):
                if k == i or k == j:
                    continue
                if is_inside_triangle(target, points[i], points[j], points[k]):
                    result = min(result, length(vector(points[i], points[j]))+length(vector(points[j], points[k]))+length(vector(points[k], points[i])))  # possible triangle
                if is_between_edge:
                    sign = ccw(points[i], points[j], points[k])
                    if sign:
                        min_perimeters[sign > 0] = min(min_perimeters[sign > 0], (length(vector(points[i], points[k]))+length(vector(points[j], points[k]))))
            if is_between_edge:
                result = min(result, sum(min_perimeters))  # possible quadrilateral
    return result if result != float("inf") else "IMPOSSIBLE"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, star_trappers())
