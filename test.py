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

class TestPhones(unittest.TestCase):

    def setUp(self):
        self.parser = CommonRegex()

    def test_phones(self):
        formats = ["12345678900", "1234567890", "1 234 567 8900", "234-567-8900",
                   "1-234-567-8900", "1.234.567.8900", "5678900", "567-8900"]
        for f in formats:
            self.assertEqual(self.parser.phones(f), [f])

class TestLinks(unittest.TestCase):

    def setUp(self):
        self.parser = CommonRegex()

    def test_links(self):
        formats = ["www.google.com", "http://www.google.com", "www.google.com/?query=dog"
                   "sub.example.com", "http://www.google.com/%&#/?q=dog"]
        for f in formats:
            self.assertEqual(self.parser.links(f), [f])

if __name__ == '__main__':
    test_cases = [TestDates, TestTimes, TestPhones, TestLinks]
    suites = []
    for case in test_cases:
        suites.append(unittest.TestLoader().loadTestsFromTestCase(case))

    all_tests = unittest.TestSuite(suites)
    unittest.TextTestRunner(verbosity=2).run(all_tests)