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
    return [a[i]-b[i] for i in xrange(len(a))]

def length(a):
    return sum(x**2 for x in a)**0.5

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
    for i in xrange(N-2):
        for j in xrange(i+1, N-1):
            for k in xrange(j+1, N):
                if is_inside_triangle(target, points[i], points[j], points[k]):
                    result = min(result, length(vector(points[i], points[j]))+length(vector(points[j], points[k]))+length(vector(points[k], points[i])))  # possible triangle
    slopes = {}
    for i, point in enumerate(points):
        g = abs(gcd(*point))
        if (point[1]//g, point[0]//g) not in slopes or length(point) < length(points[slopes[(point[1]//g, point[0]//g)]]):
            slopes[(point[1]//g, point[0]//g)] = i
    pairs = []
    for i in slopes.itervalues():
        g = abs(gcd(*points[i]))
        if (-points[i][1]//g, -points[i][0]//g) in slopes:
            j = slopes[-points[i][1]//g, -points[i][0]//g]
            if i < j:
                pairs.append((i, j))
    for i in xrange(len(pairs)-1):
        a, b = pairs[i]
        for j in xrange(i+1, len(pairs)):
            c, d = pairs[j]
            result = min(result, length(vector(points[a], points[c]))+length(vector(points[c], points[b]))+length(vector(points[b], points[d]))+length(vector(points[d], points[a])))
    return result if result != float("inf") else "IMPOSSIBLE"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, star_trappers())
