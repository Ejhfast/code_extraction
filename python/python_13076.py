# Why doesn't rails need to be restarted after I modify the controllers? Does such thing exist in Python web framework?
scope :older_than_one_year, where('date &lt; ?', 1.year.ago)
