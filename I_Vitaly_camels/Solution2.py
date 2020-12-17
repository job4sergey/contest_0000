import os
from typing import TextIO
import itertools


class Solution:
    def do_it(self, ns):
        if len(ns) == 1:
            return [ns]
        ns.sort(key=lambda x: (x % 2, -x if x % 2 else x))
        res = []

        even_cn = next(filter(lambda e: e[1] % 2, enumerate(ns)), (-1, -1))[0]
        if even_cn == -1 or even_cn == len(ns):
            return res
        odd_cn = len(ns) - even_cn
        if abs(odd_cn - even_cn) > 1:
            return res

        def merge(ii, jj, res):
            res.append(list(filter(None, itertools.chain.from_iterable(itertools.zip_longest(ii, jj)))))

        if odd_cn <= even_cn:
            merge(itertools.islice(ns, 0, even_cn), itertools.islice(ns, even_cn, len(ns)), res)
        if odd_cn >= even_cn:
            merge(itertools.islice(ns, even_cn, len(ns)), itertools.islice(ns, 0, even_cn), res)

        return res

    def process(self, sin: TextIO, sout: TextIO):
        sin.readline()
        res = Solution().do_it(list(map(int, sin.readline().split())))
        sout.write("%s\n" % len(res))
        for a in res:
            sout.write("%s\n" % ' '.join(map(str, a)))
        sout.flush()


if 'NOMAIN' not in os.environ:
    with open('camels.in', 'r') as file_in:
        with open('camels.out', 'w+') as file_out:
            Solution().process(file_in, file_out)
