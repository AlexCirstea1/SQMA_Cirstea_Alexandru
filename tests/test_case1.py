import unittest
import xmlrunner
import os


class TestCase1(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)


if __name__ == '__main__':
    # Ensure the test-reports directory exists
    if not os.path.exists('test-reports'):
        os.makedirs('test-reports')

    # Run tests and output XML reports
    with open('test-reports/test_case1.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output))
