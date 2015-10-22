# XPath invalid expression when tag name has curly braces
el.xpath('//vuln:description',
    namespaces={'vuln': 'http://whitehatsec.com/XML-api-Vuln'})
