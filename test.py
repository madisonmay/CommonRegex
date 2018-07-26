# coding: utf-8
import pytest

from commonregex import CommonRegex


@pytest.fixture(scope='function')
def parser():
    return CommonRegex()


@pytest.mark.parametrize('date', [
    "1-19-14",
    "1.19.14",
    "1.19.14",
    "01.19.14"
])
def test_numeric_date(date):
    assert parser().dates(date) == [date]


@pytest.mark.parametrize('date', [
    "January 19th, 2014",
    "Jan. 19th, 2014",
    "Jan 19 2014",
    "19 Jan 2014"
])
def test_verbose_date(date):
    assert parser().dates(date) == [date]


@pytest.mark.parametrize('time', [
    "09:45",
    "9:45",
    "23:45",
    "9:00am",
    "9am",
    "9:00 A.M.",
    "9:00 pm"
])
def test_times(time):
    assert parser().times(time) == [time]


@pytest.mark.parametrize('phone_number', [
    "12345678900",
    "1234567890",
    "+1 234 567 8900",
    "234-567-8900",
    "1-234-567-8900",
    "1.234.567.8900",
    "5678900",
    "567-8900",
    "(123) 456 7890",
    "+41 22 730 5989",
    "(+41) 22 730 5989",
    "+442345678900"
])
def test_phone_number(phone_number):
    assert parser().phones(phone_number) == [phone_number]


@pytest.mark.parametrize('phone_number', [
    "(523)222-8888 ext 527",
    "(523)222-8888x623",
    "(523)222-8888 x623",
    "(523)222-8888 x 623",
    "(523)222-8888EXT623",
    "523-222-8888EXT623",
    "(523) 222-8888 x 623"
])
def test_phones_with_extensions(phone_number):
    assert parser().phones_with_exts(phone_number) == [phone_number]


@pytest.mark.parametrize('link', [
    "www.google.com",
    "http://www.google.com",
    "www.google.com/?query=dog"
    "sub.example.com",
    "http://www.google.com/%&#/?q=dog",
    "google.com"
])
def test_links(link):
    assert parser().links(link) == [link]


@pytest.mark.parametrize('email', ["john.smith@gmail.com", "john_smith@gmail.com", "john@example.net"])
def test_email(email):
    assert parser().emails(email) == [email]


@pytest.mark.parametrize('ip', ["127.0.0.1", "192.168.1.1", "8.8.8.8"])
def test_ipv4(ip):
    assert parser().ips(ip) == [ip]


@pytest.mark.parametrize('ip', [
    "fe80:0000:0000:0000:0204:61ff:fe9d:f156",
    "fe80:0:0:0:204:61ff:fe9d:f156",
    "fe80::204:61ff:fe9d:f156",
    "fe80:0000:0000:0000:0204:61ff:254.157.241.86",
    "fe80:0:0:0:0204:61ff:254.157.241.86",
    "fe80::204:61ff:254.157.241.86", "::1"
])
def test_ipv6(ip):
    assert parser().ipv6s(ip) == [ip]


@pytest.mark.parametrize('price', ["$1.23", "$1", "$1,000", "$10,000.00"])
def test_price(price):
    assert parser().prices(price) == [price]


@pytest.mark.parametrize('color', ["#fff", "#123", "#4e32ff", "#12345678"])
def test_hex_color(color):
    assert parser().hex_colors(color) == [color]


@pytest.mark.parametrize('card_number', [
    "0000-0000-0000-0000",
    "0123456789012345",
    "0000 0000 0000 0000",
    "012345678901234"]
)
def test_credit_card(card_number):
    assert parser().credit_cards(card_number) == [card_number]


@pytest.mark.parametrize('btc', [
    "1LgqButDNV2rVHe9DATt6WqD8tKZEKvaK2",
    "19P6EYhu6kZzRy9Au4wRRZVE8RemrxPbZP",
    "1bones8KbQge9euDn523z5wVhwkTP3uc1",
    "1Bow5EMqtDGV5n5xZVgdpRPJiiDK6XSjiC"
])
def test_btc_addresses(btc):
    assert parser().btc_addresses(btc) == [btc]


@pytest.mark.parametrize('address', [
    "checkout the new place at 101 main st.",
    "504 parkwood drive",
    "3 elm boulevard",
    "500 elm street "
])
def test_street_addresses(address):
    assert parser().street_addresses(address)


@pytest.mark.parametrize('po_box', ["PO Box 123456", "hey p.o. box 234234 hey"])
def test_po_boxes(po_box):
    assert parser().po_boxes(po_box)


@pytest.mark.parametrize('zip_code', ["02540", "02540-4119"])
def test_zip_codes(zip_code):
    assert parser().zip_codes(zip_code)
