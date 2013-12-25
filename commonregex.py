import re


class CommonRegex:

    def __init__(self, text=""):
        self.text = text

        if text:
            self.dates    = self.dates()
            self.times    = self.times()
            self.phones   = self.phones()
            self.links    = self.links()
            self.emails   = self.emails()
            self.ip       = self.ip()
            self.money    = self.money()

    def _opt(self, regex):
        return u'(?:' + regex + u')?'

    def _group(self, regex):
        return u'(?:' + regex + ')'

    def _any(self, *regexes):
        return u'|'.join(regexes)

    def _strip(fn, *args, **kwargs):
        def new_fn(*args, **kwargs):
          return [x.strip() for x in fn(*args, **kwargs)]
        return new_fn

    @_strip
    def dates(self, text=None):
        text = text or self.text
        month_regex = u'(?:jan\.?|january|feb\.?|february|mar\.?|march|apr\.?|april|may|jun\.?|june|jul\.?|july|aug\.?|august|sep\.?|september|oct\.?|october|nov\.?|november|dec\.?|december)'
        day_regex = u'(?<!\:)(?<!\:\d)[0-3]?\d(?:st|nd|rd|th)?'
        year_regex = u'\d{4}'
        date_regex = self._group(self._any(day_regex + u'\s+(?:of\s+)?' + month_regex, month_regex + u'\s+' + day_regex)) + u'(?:\,)?\s*' + self._opt(year_regex) + u'|[0-3]?\d[-/][0-3]?\d[-/]\d{2,4}'
        return re.findall(date_regex, text, re.IGNORECASE)

    @_strip
    def times(self, text=None):
        text = text or self.text
        time_regex = u'\d{1,2}:\d{2} ?(?:[ap]\.?m\.?)?|\d[ap]\.?m\.?'
        return re.findall(time_regex, text, re.IGNORECASE)

    @_strip
    def phones(self, text=None):
        text = text or self.text
        phone_regex = u'(\d?\W*(?:\(?\d{3}\)?\W*)?\d{3}\W*\d{4})'
        return re.findall(phone_regex, text)

    @_strip
    def links(self, text=None):
        text = text or self.text
        link_regex = u'(?i)((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))*\))+(?:\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))'
        return re.findall(link_regex, text, re.IGNORECASE)

    @_strip
    def emails(self, text=None):
        text = text or self.text
        email_regex = u"([a-z0-9!#$%&'*+\/=?^_`{|}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"
        return re.findall(email_regex, text, re.IGNORECASE)

    @_strip
    def ip(self, text=None):
        text = text or self.text
        ip_regex = u'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
        return re.findall(ip_regex, text)

    @_strip
    def money(self, text=None):
        text = text or self.text
        money_regexp = u"\$\s?[+-]?[0-9]{1,3}(?:,?[0-9])*(?:\.[0-9]{1,2})?"
        return re.findall(money_regexp, text)

if __name__ == "__main__":
    parse = CommonRegex("8:00 5:00AM Jan 9th 2012 8/23/12 www.google.com $4891.75 http://hotmail.com (520) 820 7123, 1-230-241-2422 john_smith@gmail.com 127.0.0.1")
    print(parse.dates)
    print(parse.times)
    print(parse.phones)
    print(parse.links)
    print(parse.emails)
    print(parse.ip)
    print(parse.money)
