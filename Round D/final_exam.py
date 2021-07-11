# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round D - Problem C. Final Exam
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082bffc
#
# Time:  O(NlogN + Mlog(N + M)), pass in PyPy2 but Python2
# Space: O(N + M)
#

from random import randint, seed

# Template:
# https://github.com/kamyu104/FacebookHackerCup-2020/blob/master/Round%202/log_drivin_hirin.py
class SkipNode(object):
    def __init__(self, level=0, val=None):
        self.val = val
        self.nexts = [None]*level
        self.prevs = [None]*level

class SkipList(object):
    P_NUMERATOR, P_DENOMINATOR = 1, 2  # P = 1/4 in redis implementation
    MAX_LEVEL = 32  # enough for 2^32 elements

    def __init__(self, end=(float("inf"), float("inf")), can_duplicated=False):
        seed(0)
        self.__head = SkipNode()
        self.__len = 0
        self.__can_duplicated = can_duplicated
        self.add(end)
        self.__end = self.find(end)

    def begin(self):
        return self.__head.nexts[0]
    
    def end(self):
        return self.__end

    def lower_bound(self, target, cmp=lambda x, y: x < y):
        return self.__lower_bound(self.__find_prev_nodes(target, cmp))

    def find(self, target):
        return self.__find(target, self.__find_prev_nodes(target))
        
    def add(self, val):
        if not self.__can_duplicated and self.find(val):
            return self.find(val), False
        node = SkipNode(self.__random_level(), val)
        if len(self.__head.nexts) < len(node.nexts): 
            self.__head.nexts.extend([None]*(len(node.nexts)-len(self.__head.nexts)))
        prevs = self.__find_prev_nodes(val)
        for i in xrange(len(node.nexts)):
            node.nexts[i] = prevs[i].nexts[i]
            if prevs[i].nexts[i]:
                prevs[i].nexts[i].prevs[i] = node
            prevs[i].nexts[i] = node
            node.prevs[i] = prevs[i]
        self.__len += 1
        return node if self.__can_duplicated else (node, True)

    def remove(self, it):
        prevs = it.prevs
        curr = self.__find(it.val, prevs)
        if not curr:
            return self.__end
        self.__len -= 1   
        for i in reversed(xrange(len(curr.nexts))):
            prevs[i].nexts[i] = curr.nexts[i]
            if curr.nexts[i]:
                curr.nexts[i].prevs[i] = prevs[i]
            if not self.__head.nexts[i]:
                self.__head.nexts.pop()
        return curr.nexts[0]
    
    def __lower_bound(self, prevs):
        if prevs:
            candidate = prevs[0].nexts[0]
            if candidate:
                return candidate
        return None

    def __find(self, val, prevs):
        candidate = self.__lower_bound(prevs)
        if candidate and candidate.val == val:
            return candidate
        return None

    def __find_prev_nodes(self, val, cmp=lambda x, y: x < y):
        prevs = [None]*len(self.__head.nexts)
        curr = self.__head
        for i in reversed(xrange(len(self.__head.nexts))):
            while curr.nexts[i] and cmp(curr.nexts[i].val, val):
                curr = curr.nexts[i]
            prevs[i] = curr
        return prevs

    def __random_level(self):
        level = 1
        while randint(1, SkipList.P_DENOMINATOR) <= SkipList.P_NUMERATOR and \
              level < SkipList.MAX_LEVEL:
            level += 1
        return level
    
    def __iter__(self):
        it = self.begin()
        while it != self.end():
            yield it.val
            it = it.nexts[0]

    def __len__(self):
        return self.__len-1  # excluding end node

    def __str__(self):
        result = []
        for i in reversed(xrange(len(self.__head.nexts))):
            result.append([])
            curr = self.__head.nexts[i]
            while curr:
                result[-1].append(str(curr.val))
                curr = curr.nexts[i]
        return "\n".join(map(lambda x: "->".join(x), result))

def find_contained_interval(sl, x):
    it = sl.lower_bound((x, float("inf")))
    if it == sl.begin():
        return None
    it = it.prevs[0]
    return it.val if it.val[0] <= x <= it.val[1] else None

def find_nearest_left(sl, x):
    it = sl.lower_bound((x, float("inf")))
    if it == sl.begin():
        return None
    it = it.prevs[0]
    return it.val[1]

def find_nearest_right(sl, x):
    it = sl.lower_bound((x, float("inf")))
    if it == sl.end():
        return None
    return it.val[0]

def remove(sl, x):
    p = find_contained_interval(sl, x)
    sl.remove(sl.find(p))
    if p[0] <= x-1:
        sl.add((p[0], x-1))
    if x+1 <= p[1]:
        sl.add((x+1, p[1]))

def final_exam():
    N, M = map(int, raw_input().strip().split())
    sl = SkipList()
    for l, r in (map(int, raw_input().strip().split()) for _ in xrange(N)):
        sl.add((l, r))
    result = []
    for x in map(int, raw_input().strip().split()):
        if find_contained_interval(sl, x):
            result.append(x)
        else:
            l, r = find_nearest_left(sl, x), find_nearest_right(sl, x)
            result.append(l if r is None or (l is not None and x-l <= r-x) else r)
        remove(sl, result[-1])
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, final_exam())
