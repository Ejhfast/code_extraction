# Print search term that does not exist in list comprehension of a list comprension
list_comp = [value[0] for value in rpAttrs if not list(re.finditer(value[0], resourceProperties))]
&gt;&gt; ['ajgagag', 'ajgagag']
