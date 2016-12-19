# coding: utf-8
from commonregex import CommonRegex
import unittest


class RegexTestCase(unittest.TestCase):

    def setUp(self):
        self.parser = CommonRegex()


class TestDates(RegexTestCase):

    def test_numeric(self):
        matching = ["1-19-14", "1.19.14", "1.19.14", "01.19.14"]
        for s in matching:
            self.assertEqual(self.parser.dates(s), [s])

    def test_verbose(self):
        matching = ["January 19th, 2014", "Jan. 19th, 2014", "Jan 19 2014", "19 Jan 2014"]
        for s in matching:
            self.assertEqual(self.parser.dates(s), [s])


class TestTimes(RegexTestCase):

    def test_times(self):
        matching = ["09:45", "9:45", "23:45", "9:00am", "9am", "9:00 A.M.", "9:00 pm"]
        for s in matching:
            self.assertEqual(self.parser.times(s), [s])


class TestPhones(RegexTestCase):

    def test_phones(self):
        matching = ["12345678900", "1234567890", "+1 234 567 8900", "234-567-8900",
                   "1-234-567-8900", "1.234.567.8900", "5678900", "567-8900",
                   "(123) 456 7890", "+41 22 730 5989", "(+41) 22 730 5989",
                   "+442345678900"]
        for s in matching:
            self.assertEqual(self.parser.phones(s), [s])

class TestPhonesWithExts(RegexTestCase):

    def test_phones_with_extensions(self):
        matching = ["(523)222-8888 ext 527", "(523)222-8888x623", "(523)222-8888 x623",
                    "(523)222-8888 x 623", "(523)222-8888EXT623", "523-222-8888EXT623",
                    "(523) 222-8888 x 623"]
        non_matching = ["222-5555", "222-8888 x 623", '333-333-5555 dial 3']
        for s in matching:
            self.assertEqual(self.parser.phones_with_exts(s), [s])
        for s in non_matching:
            self.assertNotEqual(self.parser.links(s), [s])


class TestLinks(RegexTestCase):

    def test_links(self):
        matching = ["www.google.com", "http://www.google.com", "www.google.com/?query=dog"
                   "sub.example.com", "http://www.google.com/%&#/?q=dog", "google.com"]
        non_matching = ["www.google.con"]
        for s in matching:
            self.assertEqual(self.parser.links(s), [s])
        for s in non_matching:
            self.assertNotEqual(self.parser.links(s), [s])


class TestEmails(RegexTestCase):

    def test_emails(self):
        matching = ["john.smith@gmail.com", "john_smith@gmail.com", "john@example.net"]
        non_matching = ["john.smith@gmail..com"]
        for s in matching:
            self.assertEqual(self.parser.emails(s), [s])
        for s in non_matching:
            self.assertNotEqual(self.parser.emails(s), [s])


class TestIPs(RegexTestCase):

    def test_ips(self):
        matching = ["127.0.0.1", "192.168.1.1", "8.8.8.8"]
        for s in matching:
            self.assertEqual(self.parser.ips(s), [s])


class TestIPv6s(RegexTestCase):

    def test_ipv6s(self):
        matching = ["fe80:0000:0000:0000:0204:61ff:fe9d:f156", "fe80:0:0:0:204:61ff:fe9d:f156",
                    "fe80::204:61ff:fe9d:f156", "fe80:0000:0000:0000:0204:61ff:254.157.241.86",
                    "fe80:0:0:0:0204:61ff:254.157.241.86", "fe80::204:61ff:254.157.241.86", "::1"]
        for s in matching:
            self.assertEqual(self.parser.ipv6s(s), [s])


class TestPrices(RegexTestCase):

    def test_prices(self):
        matching = ["$1.23", "$1", "$1,000", "$10,000.00"]
        non_matching = ["$1,10,0", "$100.000"]
        for s in matching:
            self.assertEqual(self.parser.prices(s), [s])
        for s in non_matching:
            self.assertNotEqual(self.parser.prices(s), [s])


class TestHexColors(RegexTestCase):

    def test_hexcolors(self):
        matching = ["#fff", "#123", "#4e32ff", "#12345678"]
        for s in matching:
            self.assertEqual(self.parser.hex_colors(s), [s])


class TestCreditCards(RegexTestCase):

    def test_creditcards(self):
        matching = ["0000-0000-0000-0000", "0123456789012345",
                    "0000 0000 0000 0000", "012345678901234"]
        for s in matching:
            self.assertEqual(self.parser.credit_cards(s), [s])

class TestBTCAddresses(RegexTestCase):

    def test_btc_addresses(self):
        matching = ["1LgqButDNV2rVHe9DATt6WqD8tKZEKvaK2", "19P6EYhu6kZzRy9Au4wRRZVE8RemrxPbZP",
                    "1bones8KbQge9euDn523z5wVhwkTP3uc1", "1Bow5EMqtDGV5n5xZVgdpRPJiiDK6XSjiC"]
        non_matching = ["2LgqButDNV2rVHe9DATt6WqD8tKZEKvaK2", "19Ry9Au4wRRZVE8RemrxPbZP",
                        "1bones8KbQge9euDn523z5wVhwkTP3uc12939", "1Bow5EMqtDGV5n5xZVgdpR"]
        for s in matching:
            self.assertEqual(self.parser.btc_addresses(s), [s])
        for s in non_matching:
            self.assertNotEqual(self.parser.btc_addresses(s), [s])

class TestStreetAddresses(RegexTestCase):

    def test_street_addresses(self):
        matching = ["checkout the new place at 101 main st.", "504 parkwood drive", "3 elm boulevard",
                    "500 elm street "]
        non_matching = ["101 main straight"]

        for s in matching:
            self.assertTrue(self.parser.street_addresses(s))
        for s in non_matching:
            self.assertFalse(self.parser.street_addresses(s))

class TestPoBoxes(RegexTestCase):

    def test_po_boxes(self):
        matching = ["PO Box 123456",
                    "hey p.o. box 234234 hey"]
        non_matching = ["101 main straight"]
        

        for s in matching:
            self.assertTrue(self.parser.po_boxes(s))
        for s in non_matching:
            self.assertFalse(self.parser.po_boxes(s))

class TestZipCodes(RegexTestCase):

    def test_zip_codes(self):
        matching = ["02540", "02540-4119"]
        non_matching = ["101 main straight"]

        for s in matching:
            self.assertTrue(self.parser.zip_codes(s))
        for s in non_matching:
            self.assertFalse(self.parser.zip_codes(s))
            
if __name__ == '__main__':
    # Auto-detect test classes to reduce friction of adding a new one.
    test_cases = [clas for name, clas in locals().items() if name.startswith('Test')]
    suites = []
    for case in test_cases:
        suites.append(unittest.TestLoader().loadTestsFromTestCase(case))

    all_tests = unittest.TestSuite(suites)
    unittest.TextTestRunner(verbosity=2).run(all_tests)
