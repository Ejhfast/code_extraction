# How to parse XML in Python and LXML?
print doc.xpath('//aws:weather/aws:ob/aws:temp',
                namespaces={'aws': 'http://www.aws.com/aws'})[0].text
