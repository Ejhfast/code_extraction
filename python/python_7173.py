# Django or python manipulate email addresses and reason about domains
&gt;&gt;&gt; import tldextract
&gt;&gt;&gt; tldextract.extract('foo@bar.baz.org.uk')
ExtractResult(subdomain='bar', domain='baz', tld='org.uk')
