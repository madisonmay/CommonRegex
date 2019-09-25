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
                               questions, You can reach me at (519)-236-2723x341 or get in touch with
                               my associate at harold.smith@gmail.com""")
>>> parsed_text.times
['5:00PM', '4:00']
>>> parsed_text.dates
['Jan 9th 2012']
>>> parsed_text.links
['www.linkedin.com']
>>> parsed_text.phones
['(519)-236-2727']
>>> parsed_text.phones_with_exts
['(519)-236-2723x341']
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

```python
>>> from commonregex import time
>>> for m in time.finditer("Does 6:00 or 7:00 work better?"):
>>>     print m.start(), m.group()     
5 6:00 
13 7:00 
```

    
Please note that this module is currently English/US specific.

Supported Methods/Attributes
-----------------------------

  - `obj.dates`, `obj.dates()`
  - `obj.times`, `obj.times()`
  - `obj.phones`, `obj.phones()`
  - `obj.phones_with_exts`, `obj.phones_with_exts()`
  - `obj.links`, `obj.links()`
  - `obj.emails`, `obj.emails()`
  - `obj.ips`, `obj.ips()`
  - `obj.ipv6s`, `obj.ipv6s()`
  - `obj.prices`, `obj.prices()`
  - `obj.hex_colors`, `obj.hex_colors()`
  - `obj.credit_cards`, `obj.credit_cards()`
  - `obj.btc_addresses`, `obj.btc_addresses()`
  - `obj.street_addresses`, `obj.street_addresses()`
  - `obj.zip_codes`, `obj.zip_codes()`
  - `obj.po_boxes`, `obj.po_boxes()`
  - `obj.ssn_number`, `obj.ssn_number()`

CommonRegex Ports:
----------------------------------------
[CommonRegexRust](https://github.com/hskang9/CommonRegexRust)

[CommonRegexJS] (https://github.com/talyssonoc/CommonRegexJS)

[CommonRegexScala] (https://github.com/everpeace/CommonRegexScala)    

[CommonRegexJava] (https://github.com/talyssonoc/CommonRegexJava)

[CommonRegexCobra] (https://github.com/PurityLake/CommonRegex-Cobra)

[CommonRegexDart] (https://github.com/aufdemrand/CommonRegexDart)

[CommonRegexRuby] (https://github.com/talyssonoc/CommonRegexRuby)

[CommonRegexPHP] (https://github.com/james2doyle/CommonRegexPHP)

[![Analytics](https://ga-beacon.appspot.com/UA-46923950-1/CommonRegex/readme?pixel)](https://github.com/igrigorik/ga-beacon)

