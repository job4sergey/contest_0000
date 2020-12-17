import os
from typing import TextIO


class Solution:
    def do_it(self, road_len, time_left, holes):
        holes = set(holes)
        if road_len <= time_left:
            min_step = 1
        else:
            min_step = road_len // time_left
            min_step = (min_step + 1) if min_step * time_left < road_len else min_step

        # i = min_step
        # j = road_len

        def check(step):
            dp = [1 if ii in holes else 0 for ii in range(road_len + 1)]

            for i in range(1, road_len + 1):
                if i in holes:
                    continue
                dp[i] = 2
                for j in range(max(i - step, 0), i):
                    if dp[j] == 0:
                        dp[i] = 0
                        break

            return dp[-1] == 0

        for i in range(min_step, road_len):
            if check(i):
                return i

        # while i <= j:
        #     m = i + (j - i) // 2
        #
        #     if not check(m):
        #         # print('%s %s %s' % (i, j, False))
        #         i = m + 1
        #     else:
        #         # print('%s %s %s' % (i, j, True))
        #         j = m - 1  # y > x

        return road_len

    def process(self, sin: TextIO, sout: TextIO):
        road_len, time_left, _ = map(int, sin.readline().split())
        holes = list(map(int, sin.readline().split()))
        sout.write("%s\n" % Solution().do_it(road_len, time_left, holes))
        sout.flush()


if 'NOMAIN' not in os.environ:
    with open('tigerpower.in', 'r') as file_in:
        with open('tigerpower.out', 'w+') as file_out:
            Solution().process(file_in, file_out)
