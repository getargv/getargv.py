import os
import getargv
import unittest
import sys

class TestGetargv(unittest.TestCase):

    def setUp(self):
        self.expected = sys.argv.copy()
        if sys._framework:
            self.expected.insert(0, sys.base_exec_prefix+'/Resources/Python.app/Contents/MacOS/Python')
        else:
            self.expected.insert(0, sys.executable)

    def tearDown(self):
        if not self._outcome.result.wasSuccessful():
            print("\n\n\n", "framework: "+sys._framework, "executable: "+sys.executable, "\n\n\n", sep="\n")

    def test_as_list(self):
        actual = getargv.as_list(os.getpid())
        expected = list(map(lambda s: bytes(s,'utf-8'),self.expected))
        self.assertListEqual(actual, expected)

    def test_as_bytes_with_nuls(self):
        actual = getargv.as_bytes(os.getpid())
        expected = bytes('\0'.join(self.expected)+'\0','utf-8')
        self.assertEqual(actual, expected)

    def test_as_bytes_with_spaces(self):
        actual = getargv.as_bytes(os.getpid(),0,True)
        expected = bytes(' '.join(self.expected)+'\0','utf-8')
        self.assertEqual(actual, expected)

    def test_has_version(self):
        self.assertTrue(hasattr(getargv, '__version__'))

if __name__ == '__main__':
    unittest.main()
