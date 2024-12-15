import unittest
import xmlrunner
import os


class TestCase2(unittest.TestCase):
    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)


if __name__ == '__main__':
    if not os.path.exists('test-reports'):
        os.makedirs('test-reports')

    with open('test-reports/test_case2.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output))
