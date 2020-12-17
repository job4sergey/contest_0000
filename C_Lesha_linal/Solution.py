import os
from typing import TextIO


class Solution:
    def do_it(self, n):
        # for d in range(2, int(n ** 0.5) + 1):
        #     if n % d == 0:
        #         return '%d*%d' % (d, n // d)

        return n

    def process(self, sin: TextIO, sout: TextIO):
        sout.write('%s' % Solution().do_it(int(sin.readline().strip())))
        sout.flush()


if 'NOMAIN' not in os.environ:
    with open('elephant.in', 'r') as file_in:
        with open('elephant.out', 'w+') as file_out:
            Solution().process(file_in, file_out)
