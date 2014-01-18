from commonregex import CommonRegex
import unittest

class TestDates(unittest.TestCase):

    def setUp(self):
        self.parser = CommonRegex()

    def test_numeric(self):
        formats = ["1-19-14", "1.19.14", "1.19.14", "01.19.14"]
        for f in formats:
            self.assertEqual(self.parser.dates(f), [f])

    def test_verbose(self):
        formats = ["January 19th, 2014", "Jan. 19th, 2014", "Jan 19 2014", "19 Jan 2014"]
        for f in formats:
            self.assertEqual(self.parser.dates(f), [f])

class TestTimes(unittest.TestCase):

    def setUp(self):
        self.parser = CommonRegex()

    def test_times(self):
        formats = ["09:45", "9:45", "23:45", "9:00am", "9am", "9:00 A.M.", "9:00 pm"]
        for f in formats:
            self.assertEqual(self.parser.times(f), [f])

if __name__ == '__main__':
    test_cases = [TestDates, TestTimes]
    suites = []
    for case in test_cases:
        suites.append(unittest.TestLoader().loadTestsFromTestCase(case))

    all_tests = unittest.TestSuite(suites)
    unittest.TextTestRunner(verbosity=2).run(all_tests)