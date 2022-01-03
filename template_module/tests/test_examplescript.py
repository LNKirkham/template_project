
# PROJECT:
#       TEMPLATE PROJECT
#
# SUMMARY:
#       This script contains the tests for examplescript.py
#
# DOCS:
#       Link goes here
#
# LAST EDITED:
#       2022-01-03 --> Created
#
# CONTACT:
# 	    Louise Kirkham: louisek@gmail.com

import unittest
from pandas.util.testing import assert_frame_equal
from template_module.src import examplescript


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
