CommonRegex
===========

Find all times, dates, links, phone numbers, emails, ip addresses, prices, hex colors, and credit card numbers in a string. 
We did the hard work so you don't have to.

Pull requests welcome!

Installation
-------
Install via pip

    sudo pip install commonregex
    
or via setup.py

    python setup.py install


Usage
------

```python    
>>> from commonregex import CommonRegex
>>> parsed_text = CommonRegex("""John, please get that article on www.linkedin.com to me by 5:00PM 
                               on Jan 9th 2012. 4:00 would be ideal, actually. If you have any 
                               questions, You can reach me at (519)-236-2723 or get in touch with
                               my associate at harold.smith@gmail.com""")
>>> parsed_text.times
['5:00PM', '4:00']
>>> parsed_text.dates
['Jan 9th 2012']
>>> parsed_text.links
['www.linkedin.com']
>>> parsed_text.phones
['(519)-236-2727']
>>> parsed_text.emails
['harold.smith@gmail.com']
```
    
Alternatively, you can generate a single CommonRegex instance and use it to parse multiple segments of text.

```python
>>> parser = CommonRegex()
>>> parser.times("When are you free?  Do you want to meet up for coffee at 4:00?")
['4:00']
```
    
Finally, all regular expressions used are publicly exposed.

```python
>>> from commonregex import email
>>> import re
>>> text = "...get in touch with my associate at harold.smith@gmail.com"
>>> re.sub(email, "anon@example.com", text)
'...get in touch with my associate at anon@example.com'
```
    
Please note that this module is currently English/US specific.

Supported Methods/Attributes
-----------------------------

  - obj.dates, obj.dates()
  - obj.times, obj.times()
  - obj.phones, obj.phones()
  - obj.links, obj.links()
  - obj.emails, obj.emails()
  - obj.ips, obj.ips()
  - obj.ipv6s, obj.ipv6s()
  - obj.prices, obj.prices()
  - obj.hex_colors, obj.hex_colors()
  - obj.credit_cards, obj.credit_cards()

CommonRegex Ports:
----------------------------------------
[CommonRegexJS] (https://github.com/talyssonoc/CommonRegexJS)

[CommonRegexScala] (https://github.com/everpeace/CommonRegexScala)    

[CommonRegexJava] (https://github.com/talyssonoc/CommonRegexJava)

License
-------------
The MIT License (MIT)

Copyright (c) 2014 Madison May

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

[![Analytics](https://ga-beacon.appspot.com/UA-46923950-1/CommonRegex/readme?pixel)](https://github.com/igrigorik/ga-beacon)

