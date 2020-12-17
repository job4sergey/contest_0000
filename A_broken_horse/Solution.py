import os
from typing import TextIO


class Solution:
    def do_it(self, n):
        dp = [[[0] * n for _ in range(3)] for __ in range(2)]
        dp[0][0][0] = 1

        MX = 10 ** 9 + 7

        for r in range(3):
            for c in range(n):
                for dr, dc in ((-1, -2), (1, -2), (-2, -1), (2, -1)):
                    r2, c2 = r + dr, c + dc
                    if r2 < 0 or c2 < 0 or r2 >= 3 or c2 >= n:
                        continue

                    dp[0][r][c] += dp[0][r2][c2]
                    dp[0][r][c] %= MX

                if r > 0 and c > 0:
                    dp[1][r - 1][c - 1] += dp[0][r][c]
                    dp[1][r - 1][c - 1] %= MX

                if r < 2 and c > 0:
                    dp[1][r + 1][c - 1] += dp[0][r][c]
                    dp[1][r + 1][c - 1] %= MX

        for r in range(3):
            for c in range(n):
                for dr, dc in ((-1, -2), (1, -2), (-2, -1), (2, -1)):
                    r2, c2 = r + dr, c + dc
                    if r2 < 0 or c2 < 0 or r2 >= 3 or c2 >= n:
                        continue

                    dp[1][r][c] += dp[1][r2][c2]
                    dp[1][r][c] %= MX

        return (dp[0][2][-1] + dp[1][2][-1]) % MX

    def process(self, sin: TextIO, sout: TextIO):
        res = Solution().do_it(int(sin.readline()))
        sout.write("%s\n" % res)
        sout.flush()


if 'NOMAIN' not in os.environ:
    with open('broken-horse.in', 'r') as file_in:
        with open('broken-horse.out', 'w+') as file_out:
            Solution().process(file_in, file_out)
