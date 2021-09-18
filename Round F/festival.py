# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round F - Problem B. Festival
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887dba
#
# Time:  O(NlogN), pass in PyPy2 but Python2
# Space: O(N)
#

from random import randint, seed

# Template:
# https://github.com/kamyu104/GoogleKickStart-2021/blob/master/Round%20D/final_exam.py
class SkipNode(object):
    def __init__(self, level=0, val=None):
        self.val = val
        self.nexts = [None]*level
        self.prevs = [None]*level

class SkipList(object):
    P_NUMERATOR, P_DENOMINATOR = 1, 2  # P = 1/4 in redis implementation
    MAX_LEVEL = 32  # enough for 2^32 elements

    def __init__(self, end=float("inf"), can_duplicated=True):
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

def festival():
    D, N, K = map(int, raw_input().strip().split())
    intervals = []
    for _ in xrange(N):
        h, s, e = map(int, raw_input().strip().split())
        intervals.append((s, 1, h))
        intervals.append((e+1, -1, h))
    intervals.sort()

    topk_sl, others_sl = SkipList(), SkipList()
    result = curr = 0
    for _, e, h in intervals:
        if e == 1:
            topk_sl.add(h)
            curr += h
            if len(topk_sl) == K+1:  # keep topk_sl with k elements
                v = topk_sl.begin().val
                topk_sl.remove(topk_sl.begin())
                curr -= v
                others_sl.add(v)
            result = max(result, curr)
        else:
            it = others_sl.find(h)
            if it:
                others_sl.remove(it)
                continue
            topk_sl.remove(topk_sl.find(h))
            curr -= h
            if not others_sl:
                continue
            v = others_sl.end().prevs[0].val
            others_sl.remove(others_sl.end().prevs[0])
            topk_sl.add(v)  # keep topk_sl with k elements
            curr += v
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, festival())
