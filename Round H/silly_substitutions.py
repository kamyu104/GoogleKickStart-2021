# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Kick Start 2021 Round H - Problem C. Silly Substitution
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008d94f5
#
# Time:  O(n)
# Space: O(n)
#

from collections import defaultdict

class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def f(head):
    result = []
    curr = head
    while curr:
        result.append(str(curr.val))
        curr = curr.right
    return "".join(result)

def silly_substitutions():
    N = input()
    S = map(int, list(raw_input().strip()))
    cnt = 0
    tail = head = Node(S[0])
    lookup = defaultdict(set)
    for i in xrange(1, len(S)):
        node = Node(S[i], left=tail)
        node.left.right = node
        if (tail.val+1)%10 == node.val:
            lookup[tail.val].add(tail)
            cnt += 1
        tail = node
    while cnt:
        for i in xrange(10):
            if not lookup[i]:
                continue
            while lookup[i]:
                node = lookup[i].pop()
                cnt -= 1
                if node.left and node.left in lookup[node.left.val]:
                    lookup[node.left.val].remove(node.left)
                    cnt -= 1
                if node.right in lookup[node.right.val]:
                    lookup[node.right.val].remove(node.right)
                    cnt -= 1
                new_node = Node((i+2)%10, left=node.left, right=node.right.right)
                if new_node.left:
                    new_node.left.right = new_node
                else:
                    head = new_node
                if new_node.right:
                    new_node.right.left = new_node
                if new_node.left and (new_node.left.val+1)%10 == new_node.val:
                    if new_node.left not in lookup[new_node.left.val]:
                        lookup[new_node.left.val].add(new_node.left)
                        cnt += 1
                if new_node.right and (new_node.val+1)%10 == new_node.right.val:
                    if new_node not in lookup[new_node.val]:
                        lookup[new_node.val].add(new_node)
                        cnt += 1
    result = []
    curr = head
    while curr:
        result.append(str(curr.val))
        curr = curr.right
    return "".join(result)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, silly_substitutions())
