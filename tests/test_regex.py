# coding: utf-8
from commonregex import Document
import unittest


class TestDates(unittest.TestCase):

    def test_numeric(self):
        matching = ["1-19-14", "1.19.14", "1.19.14", "01.19.14"]
        for s in matching:
            self.assertEqual(Document(s).dates, [s])

    def test_verbose(self):
        matching = ["January 19th, 2014", "Jan. 19th, 2014", "Jan 19 2014", "19 Jan 2014"]
        for s in matching:
            self.assertEqual(Document(s).dates, [s])


class TestTimes(unittest.TestCase):

    def test_times(self):
        matching = ["09:45", "9:45", "23:45", "9:00am", "9am", "9:00 A.M.", "9:00 pm"]
        for s in matching:
            self.assertEqual(Document(s).times, [s])


class TestPhones(unittest.TestCase):

    def test_phones(self):
        matching = ["12345678900", "1234567890", "+1 234 567 8900", "234-567-8900",
                   "1-234-567-8900", "1.234.567.8900", "5678900", "567-8900",
                   "(123) 456 7890", "+41 22 730 5989", "(+41) 22 730 5989",
                   "+442345678900"]
        for s in matching:
            self.assertEqual(Document(s).phones, [s])

class TestPhonesWithExts(unittest.TestCase):

    def test_phones_with_extensions(self):
        matching = ["(523)222-8888 ext 527", "(523)222-8888x623", "(523)222-8888 x623",
                    "(523)222-8888 x 623", "(523)222-8888EXT623", "523-222-8888EXT623",
                    "(523) 222-8888 x 623"]
        non_matching = ["222-5555", "222-8888 x 623", '333-333-5555 dial 3']
        for s in matching:
            self.assertEqual(Document(s).phones_with_exts, [s])
        for s in non_matching:
            self.assertNotEqual(Document(s).links, [s])


class TestLinks(unittest.TestCase):

    def test_links(self):
        matching = ["www.google.com", "http://www.google.com", "www.google.com/?query=dog"
                   "sub.example.com", "http://www.google.com/%&#/?q=dog", "google.com"]
        non_matching = ["www.google.con"]
        for s in matching:
            self.assertEqual(Document(s).links, [s])
        for s in non_matching:
            self.assertNotEqual(Document(s).links, [s])


class TestEmails(unittest.TestCase):

    def test_emails(self):
        matching = ["john.smith@gmail.com", "john_smith@gmail.com", "john@example.net"]
        non_matching = ["john.smith@gmail..com"]
        for s in matching:
            self.assertEqual(Document(s).emails, [s])
        for s in non_matching:
            self.assertNotEqual(Document(s).emails, [s])


class TestIPs(unittest.TestCase):

    def test_ips(self):
        matching = ["127.0.0.1", "192.168.1.1", "8.8.8.8"]
        for s in matching:
            self.assertEqual(Document(s).ips, [s])


class TestIPv6s(unittest.TestCase):

    def test_ipv6s(self):
        matching = ["fe80:0000:0000:0000:0204:61ff:fe9d:f156", "fe80:0:0:0:204:61ff:fe9d:f156",
                    "fe80::204:61ff:fe9d:f156", "fe80:0000:0000:0000:0204:61ff:254.157.241.86",
                    "fe80:0:0:0:0204:61ff:254.157.241.86", "fe80::204:61ff:254.157.241.86", "::1"]
        for s in matching:
            self.assertEqual(Document(s).ipv6s, [s])


class TestPrices(unittest.TestCase):

    def test_prices(self):
        matching = ["$1.23", "$1", "$1,000", "$10,000.00"]
        non_matching = ["$1,10,0", "$100.000"]
        for s in matching:
            self.assertEqual(Document(s).prices, [s])
        for s in non_matching:
            self.assertNotEqual(Document(s).prices, [s])


class TestHexColors(unittest.TestCase):

    def test_hexcolors(self):
        matching = ["#fff", "#123", "#4e32ff", "#12345678"]
        for s in matching:
            self.assertEqual(Document(s).hex_colors, [s])


class TestCreditCards(unittest.TestCase):

    def test_creditcards(self):
        matching = ["0000-0000-0000-0000", "0123456789012345",
                    "0000 0000 0000 0000", "012345678901234"]
        for s in matching:
            self.assertEqual(Document(s).credit_cards, [s])

class TestBTCAddresses(unittest.TestCase):

    def test_btc_addresses(self):
        matching = ["1LgqButDNV2rVHe9DATt6WqD8tKZEKvaK2", "19P6EYhu6kZzRy9Au4wRRZVE8RemrxPbZP",
                    "1bones8KbQge9euDn523z5wVhwkTP3uc1", "1Bow5EMqtDGV5n5xZVgdpRPJiiDK6XSjiC"]
        non_matching = ["2LgqButDNV2rVHe9DATt6WqD8tKZEKvaK2", "19Ry9Au4wRRZVE8RemrxPbZP",
                        "1bones8KbQge9euDn523z5wVhwkTP3uc12939", "1Bow5EMqtDGV5n5xZVgdpR"]
        for s in matching:
            self.assertEqual(Document(s).btc_addresses, [s])
        for s in non_matching:
            self.assertNotEqual(Document(s).btc_addresses, [s])

class TestStreetAddresses(unittest.TestCase):

    def test_street_addresses(self):
        matching = ["checkout the new place at 101 main st.", "504 parkwood drive", "3 elm boulevard",
                    "500 elm street "]
        non_matching = ["101 main straight"]

        for s in matching:
            self.assertTrue(Document(s).street_addresses)
        for s in non_matching:
            self.assertFalse(Document(s).street_addresses)

class TestPoBoxes(unittest.TestCase):

    def test_po_boxes(self):
        matching = ["PO Box 123456",
                    "hey p.o. box 234234 hey"]
        non_matching = ["101 main straight"]
        

        for s in matching:
            self.assertTrue(Document(s).po_boxes)
        for s in non_matching:
            self.assertFalse(Document(s).po_boxes)

class TestZipCodes(unittest.TestCase):

    def test_zip_codes(self):
        matching = ["02540", "02540-4119"]
        non_matching = ["101 main straight", "123456"]

        for s in matching:
            self.assertTrue(Document(s).zip_codes)
        for s in non_matching:
            self.assertFalse(Document(s).zip_codes)
