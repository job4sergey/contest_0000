import os
import sys
from collections import Counter
from typing import TextIO


class Solution:
    def do_it(self, s):
        fqs = Counter(s)

        res = []

        for c, cn in fqs.items():
            if cn % 2:
                return '-1'

            res.append(('%s' % c) * (cn // 2))

        s2 = ''.join(res)
        return '%d %s' % (len(s2), s2)

    def process(self, sin: TextIO, sout: TextIO):
        sout.write('%s' % Solution().do_it(sin.readline().strip()))
        sout.flush()


if 'NOMAIN' not in os.environ:
    Solution().process(sys.stdin, sys.stdout)
