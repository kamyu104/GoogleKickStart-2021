# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round F - Problem C. Star Trapper
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000888d45
#
# Time:  O(N^3)
# Space: O(N)
#

from fractions import gcd

def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def vector(a, b):
    return [a[0]-b[0], a[1]-b[1]]

def length(a):
    return (a[0]**2+a[1]**2)**0.5

def is_inside_triangle(t, a, b, c):
    d1, d2, d3 = ccw(t, a, b),  ccw(t, b, c),  ccw(t, c, a)
    return (d1 > 0 and d2 > 0 and d3 > 0) or (d1 < 0 and d2 < 0 and d3 < 0)

def star_trappers():
    N = input()
    points = [map(int, raw_input().strip().split()) for _ in xrange(N)]
    target = map(int, raw_input().strip().split())
    for point in points:
        point[0] -= target[0]
        point[1] -= target[1]
    target = [0, 0]

    result = float("inf")
    for i in xrange(N-2):  # Time: O(N^3)
        for j in xrange(i+1, N-1):
            for k in xrange(j+1, N):
                if is_inside_triangle(target, points[i], points[j], points[k]):
                    result = min(result, length(vector(points[i], points[j]))+length(vector(points[j], points[k]))+length(vector(points[k], points[i])))  # possible triangle
    slopes = {}
    for i, point in enumerate(points):
        g = abs(gcd(*point))
        s = (point[1]//g, point[0]//g)
        if s not in slopes or length(point) < length(points[slopes[s]]):
            slopes[s] = i
    diagonals = []
    for i in slopes.itervalues():  # Time: O(N)
        g = abs(gcd(*points[i]))
        s = (-points[i][1]//g, -points[i][0]//g)
        if s not in slopes:
            continue
        j = slopes[s]
        if i < j:
            diagonals.append((i, j))
    for i in xrange(len(diagonals)-1):  # Time: O((N/2)^2)
        a, c = diagonals[i]
        for j in xrange(i+1, len(diagonals)):
            b, d = diagonals[j]
            result = min(result, length(vector(points[a], points[b]))+length(vector(points[b], points[c]))+length(vector(points[c], points[d]))+length(vector(points[d], points[a])))  # possible quadrilateral
    return result if result != float("inf") else "IMPOSSIBLE"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, star_trappers())
