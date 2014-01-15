from types import MethodType
import re

date        = re.compile(u'(?:(?<!\:)(?<!\:\d)[0-3]?\d(?:st|nd|rd|th)?\s+(?:of\s+)?(?:jan\.?|january|feb\.?|february|mar\.?|march|apr\.?|april|may|jun\.?|june|jul\.?|july|aug\.?|august|sep\.?|september|oct\.?|october|nov\.?|november|dec\.?|december)|(?:jan\.?|january|feb\.?|february|mar\.?|march|apr\.?|april|may|jun\.?|june|jul\.?|july|aug\.?|august|sep\.?|september|oct\.?|october|nov\.?|november|dec\.?|december)\s+(?<!\:)(?<!\:\d)[0-3]?\d(?:st|nd|rd|th)?)(?:\,)?\s*(?:\d{4})?|[0-3]?\d[-/][0-3]?\d[-/]\d{2,4}', re.IGNORECASE)
time        = re.compile(u'\d{1,2}:\d{2} ?(?:[ap]\.?m\.?)?|\d[ap]\.?m\.?', re.IGNORECASE)
phone       = re.compile(u'((?<![\d-])(?:\d[-.\s*])?(?:\(?\d{3}\)?[-.\s*]?)?\d{3}[-.\s*]?\d{4}(?![\d-]))')
link        = re.compile(u'(?i)((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))', re.IGNORECASE)
email       = re.compile(u"([a-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)", re.IGNORECASE)
ip          = re.compile(u'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', re.IGNORECASE)
ipv6        = re.compile(u'\s*(?!.*::.*::)(?:(?!:)|:(?=:))(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)){6}(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)[0-9a-f]{0,4}(?:(?<=::)|(?<!:)|(?<=:)(?<!::):)|(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)){3})\s*', re.VERBOSE|re.IGNORECASE|re.DOTALL)
price       = re.compile(u'\$\s?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?')
hex_color   = re.compile(u'(#(?:[0-9a-fA-F]{8})|#(?:[0-9a-fA-F]{3}){1,2})\\b')
credit_card = re.compile(u'((?:(?:\\d{4}[- ]?){3}\\d{4}|\\d{16}))(?![\\d])')

regexes = {"dates"        : date,
           "times"        : time, 
           "phones"       : phone,
           "links"        : link,
           "emails"       : email,
           "ips"          : ip,
           "ipv6s"        : ipv6,
           "prices"       : price,
           "hex_colors"   : hex_color,
           "credit_cards" : credit_card}

class regex:

  def __init__(self, obj, regex):
    self.obj = obj
    self.regex = regex

  def __call__(self, *args):
    def regex_method(text=None):
      return [x.strip() for x in re.findall(self.regex, text or self.obj.text)]
    return regex_method

class CommonRegex(object):

    def __init__(self, text=""):
        self.text = text

        for k, v in regexes.items():
          setattr(self, k, regex(self, v)(self))

        if text:
            for key in regexes.keys():
                method = getattr(self, key)
                setattr(self, key, method())

if __name__ == "__main__":
    test = """"8:00 5:00AM Jan 9th 2012 8/23/12 www.google.com $4891.75
               2001:0db8::ff00:0042:8329 http://hotmail.com (520) 820 7123,
               1-230-241-2422 john_smith@gmail.com 127.0.0.1 #e9be4fff 1234567891011121
               1234-5678-9101-1121 """

    parse = CommonRegex(test)
    assert(parse.dates        == ['Jan 9th 2012', '8/23/12'])
    assert(parse.times        == ['8:00', '5:00AM', '00:00', '42:83'])
    assert(parse.phones       == ['(520) 820 7123', '1-230-241-2422'])
    assert(parse.links        == ['www.google.com', 'http://hotmail.com'])
    assert(parse.emails       == ['john_smith@gmail.com'])
    assert(parse.ips          == ['127.0.0.1'])
    assert(parse.ipv6s        == ['2001:0db8::ff00:0042:8329'])
    assert(parse.prices       == ['$4891.75'])
    assert(parse.hex_colors   == ['#e9be4fff'])
    assert(parse.credit_cards == ['1234567891011121', '1234-5678-9101-1121'])
