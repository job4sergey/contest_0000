import os
from typing import TextIO


class Solution:
    def do_it(self, names, exits):
        class ListNode:
            def __init__(self, name):
                self.name = name
                self.pre = None
                self.next = None

            def __repr__(self):
                return '--%s--' % self.name

        head = ListNode(names[0])
        pre = head
        no2node = {1: head}

        for i, name in enumerate(names[1:], 1):
            node = ListNode(name)
            no2node[i + 1] = node
            node.pre = pre
            pre.next = node
            pre = node

        pre.next = head
        head.pre = pre

        res = []
        for j in exits:
            node = no2node[j]
            res.append('%s %s' % (node.pre.name, node.next.name))
            node.pre.next = node.next
            node.next.pre = node.pre

        return res

    def process(self, sin: TextIO, sout: TextIO):
        sin.readline()
        res = Solution().do_it(sin.readline().split(), list(map(int, sin.readline().split())))
        for shout in res:
            sout.write("%s\n" % shout)
        sout.flush()


if 'NOMAIN' not in os.environ:
    with open('meeting.in', 'r') as file_in:
        with open('meeting.out', 'w+') as file_out:
            Solution().process(file_in, file_out)
