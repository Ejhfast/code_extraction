# Regular Expression Get US Zip Code
&gt;&gt;&gt; postal_code = re.search(r'.*(\d{5}(\-\d{4})?)$', address)
&gt;&gt;&gt; postal_code.groups()
('84532', None)
