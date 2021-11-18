# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round H - Problem C. Silly Substitutions
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008d94f5
#
# Time:  O(N)
# Space: O(N)
#

from collections import defaultdict

class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def silly_substitutions():
    N = input()
    S = map(int, list(raw_input().strip()))
    tail = head = Node(S[0])
    lookup = defaultdict(set)
    cnt = 0
    for i in xrange(1, len(S)):
        node = Node(S[i], left=tail)
        node.left.right = node
        if (tail.val+1)%10 == node.val:
            lookup[tail.val].add(tail)
            cnt += 1
        tail = node
    i = 0
    while cnt:
        while lookup[i]:
            node = lookup[i].pop()
            cnt -= 1
            if node.left and node.left in lookup[node.left.val]:
                lookup[node.left.val].remove(node.left)
                cnt -= 1
            if node.right in lookup[node.right.val]:
                lookup[node.right.val].remove(node.right)
                cnt -= 1
            node = Node((i+2)%10, left=node.left, right=node.right.right)
            if node.left:
                node.left.right = node
            else:
                head = node
            if node.right:
                node.right.left = node
            # the number of inital nodes of interest is at most O(N).
            # we will remove at most O(N) nodes.
            # for each remove, at most 1 node of interest is needed to add.
            # the total number of added nodes of interest will be at most O(2N)
            if node.left and (node.left.val+1)%10 == node.val and \
               (not node.left.left or (node.left.left.val+1)%10 != node.left.val):
                # assume current replace is (01), and both two possible interests (12) and (23) exist
                # - (^|[1-9])1(01)3 => (^|[1-9])1(2)3,
                #   since (12) is prior to (23), (^|[1-9])(1(2))3 => (^|[1-9])(3)3,
                #   only need to mark (12) as interest
                # - 01(01)3 => 01(2)3,
                #   since (01) is prior to (12) and (23), (01)(2)3 => (2)(2)3,
                #   only need to mark (23) as interest
                lookup[node.left.val].add(node.left)
                cnt += 1
            elif node.right and (node.val+1)%10 == node.right.val:
                lookup[node.val].add(node)
                cnt += 1
        i = (i+1)%10
    result = []
    curr = head
    while curr:
        result.append(str(curr.val))
        curr = curr.right
    return "".join(result)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, silly_substitutions())
