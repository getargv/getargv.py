import os
import getargv
import unittest
import sys

def expected_args(make_bytes=False):
    expected = sys.argv.copy()
    expected.insert(0, sys.base_exec_prefix+'/Resources/Python.app/Contents/MacOS/Python')
    if make_bytes:
        expected = list(map(lambda s: bytes(s,'utf-8'),expected))
    return expected

class TestGetargv(unittest.TestCase):

    def test_as_list(self):
        actual = getargv.as_list(os.getpid())
        expected = expected_args(True)
        self.assertEqual(actual, expected)

    def test_as_bytes_with_nuls(self):
        actual = getargv.as_bytes(os.getpid())
        expected = expected_args()
        expected = bytes('\0'.join(expected)+'\0','utf-8')
        self.assertEqual(actual, expected)

    def test_as_bytes_with_spaces(self):
        actual = getargv.as_bytes(os.getpid(),0,True)
        expected = expected_args()
        expected = bytes(' '.join(expected)+'\0','utf-8')
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
