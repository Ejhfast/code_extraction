# Split string after hex values
new_string = re.split('\s+', re.sub('[\x01-\x1f\x7f]', ' ', str1))
