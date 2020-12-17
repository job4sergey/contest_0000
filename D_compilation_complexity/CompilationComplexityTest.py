import io
import os

os.environ['NOMAIN'] = '1'
from com.codeforces.mamambo.contest_0000.D_compilation_complexity.Solution import Solution

from com.letcode.common.TestCaseBase import TestCaseBase


class CompilationComplexityTest(TestCaseBase):
    def atest(self, mc, deps, qs, e):
        so = Solution()
        self.assertEquals(so.do_it(mc, deps, qs), e)

    def atest_file(self, in_file_path, e_out_file_path):
        so = Solution()
        out_file = io.StringIO()

        with open(in_file_path, 'r') as in_file:
            so.process(in_file, out_file)

        out_file.seek(0)

        with open(e_out_file_path, 'r') as e_file:
            a_lines = out_file.readlines()
            e_lines = e_file.readlines()
            self.assertEquals(a_lines, e_lines)

    def test(self):
        atest_file = self.atest_file

        atest_file('in04.txt', 'out04.txt')
        atest_file('in01.txt', 'out01.txt')
        atest_file('in02.txt', 'out02.txt')
        atest_file('in03.txt', 'out03.txt')
