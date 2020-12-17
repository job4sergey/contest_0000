import os
import sys
from collections import defaultdict, deque
from typing import TextIO


class Solution:
    def do_it(self, mc, deps, qs):
        ind = [0] * (mc + 1)
        leaves = set(range(1, mc + 1))
        all_deps = defaultdict(set)
        res = defaultdict(int)

        g = defaultdict(list)
        for u, v in deps:
            g[v].append(u)
            ind[u] += 1
            leaves.discard(u)

        front = deque(leaves)
        qs_set = set(qs)

        while front and qs_set:
            u = front.popleft()
            res[u] = len(all_deps[u])
            qs_set.discard(u)
            for v in g[u]:
                all_deps[v].update(all_deps[u], {u})
                ind[v] -= 1
                if ind[v] == 0:
                    front.append(v)
            all_deps.pop(u)

        return (-1 if ind[u] else res[u] for u in qs)

    def process(self, sin: TextIO, sout: TextIO):
        mc, deps_cnt = map(int, sin.readline().split())
        deps = [list(map(int, sin.readline().split())) for _ in range(deps_cnt)]

        qs_cnt = int(sin.readline())
        qs = [int(sin.readline()) for _ in range(qs_cnt)]

        for cmp in Solution().do_it(mc, deps, qs):
            sout.write('%s\n' % cmp)

        sout.flush()


if 'NOMAIN' not in os.environ:
    Solution().process(sys.stdin, sys.stdout)
