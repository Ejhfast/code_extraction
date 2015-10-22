# python regex trouble
>>> re.match("(get|post|put|head)\s+(\S+) ",'GET some-site.com HTTP/1.0 ...',re.IGNORECASE).groups()
('GET', 'some-site.com')
>>>
