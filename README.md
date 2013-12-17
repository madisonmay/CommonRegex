CommonRegex
===========

Find all times, dates, links, phone numbers, and emails in a string. 
I did the hard work so you don'thave to. 

Note that this library is English language specific.  

Usage
------

    >>> from commonregex import CommonRegex
    >>> parsed_text = CommonRegex("John, please get that article on www.linkedin.com to me by 5:00PM 
                                   on Jan 9th 2012. 4:00 would be ideal, actually. If you have any 
                                   questions, You can reach me at (519)-236-2723 or get in touch with
                                   my associate at harold.smith@gmail.com")
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
    
Alternatively, you can generate a single CommonRegex instance and use it to parse multiple segments of text.

    >>> parser = CommonRegex()
    >>> parser.times("When are you free?  Do you want to meet up for coffee at 4:00?")
    ['4:00']
    

