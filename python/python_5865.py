# Using the difflib.HtmlDiff class - showing single chars
print html_diff.make_table(previous_contents.split('\n'),
                           fetch_url.page_contents.split('\n'))
