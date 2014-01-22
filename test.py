from commonregex import CommonRegex
import unittest

class TestDates(unittest.TestCase):

    def setUp(self):
        self.parser = CommonRegex()

    def test_numeric(self):
        matching = ["1-19-14", "1.19.14", "1.19.14", "01.19.14"]
        for s in matching:
            self.assertEqual(self.parser.dates(s), [s])

    def test_verbose(self):
        matching = ["January 19th, 2014", "Jan. 19th, 2014", "Jan 19 2014", "19 Jan 2014"]
        for s in matching:
            self.assertEqual(self.parser.dates(s), [s])

class TestTimes(unittest.TestCase):

    def setUp(self):
        self.parser = CommonRegex()

    def test_times(self):
        matching = ["09:45", "9:45", "23:45", "9:00am", "9am", "9:00 A.M.", "9:00 pm"]
        for s in matching:
            self.assertEqual(self.parser.times(s), [s])

class TestPhones(unittest.TestCase):

    def setUp(self):
        self.parser = CommonRegex()

    def test_phones(self):
        matching = ["12345678900", "1234567890", "+1 234 567 8900", "234-567-8900",
                   "1-234-567-8900", "1.234.567.8900", "5678900", "567-8900", 
                   "(123) 456 7890", "+41 22 730 5989", "(+41) 22 730 5989",
                   "+442345678900"]
        for s in matching:
            self.assertEqual(self.parser.phones(s), [s])

class TestLinks(unittest.TestCase):

    def setUp(self):
        self.parser = CommonRegex()

    def test_links(self):
        matching = ["www.google.com", "http://www.google.com", "www.google.com/?query=dog"
                   "sub.example.com", "http://www.google.com/%&#/?q=dog", "google.com"]
        non_matching = ["www.google.con"]
        for s in matching:
            self.assertEqual(self.parser.links(s), [s])
        for s in non_matching:
            self.assertNotEqual(self.parser.links(s), [s])


if __name__ == '__main__':
    test_cases = [TestDates, TestTimes, TestPhones, TestTimes, TestLinks]
    suites = []
    for case in test_cases:
        suites.append(unittest.TestLoader().loadTestsFromTestCase(case))

    all_tests = unittest.TestSuite(suites)
    unittest.TextTestRunner(verbosity=2).run(all_tests)