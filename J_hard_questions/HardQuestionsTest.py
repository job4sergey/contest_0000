import io
import os

os.environ['NOMAIN'] = '1'
from com.codeforces.mamambo.contest_0000.J_hard_questions.Solution import Solution

from com.letcode.common.TestCaseBase import TestCaseBase


class HardQuestionsTest(TestCaseBase):
    def atest_file(self, in_file_path, e_out_file_path):
        self.assert_from_file(Solution(), in_file_path, e_out_file_path)

    def test(self):
        atest_file = self.atest_file

        atest_file('in03.txt', 'out03.txt')
        atest_file('in01.txt', 'out01.txt')
        atest_file('in02.txt', 'out02.txt')
