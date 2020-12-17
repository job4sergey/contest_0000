import io
import os

os.environ['NOMAIN'] = '1'
from com.codeforces.mamambo.contest_0000.C_Lesha_linal.Solution import Solution

from com.letcode.common.TestCaseBase import TestCaseBase


class VitalyCamelsTest(TestCaseBase):
    def atest_file(self, in_file_path, e_out_file_path):
        self.assert_from_file(Solution(), in_file_path, e_out_file_path)

    def test(self):
        atest_file = self.atest_file