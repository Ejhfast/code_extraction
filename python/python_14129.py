# Regex to not match anything in brackets, only letters, numbers and spaces, and nothing after a dot
fileName = '[abc][def]Real Name[!].exe'
name = re.search('(\[[^]]*\])*([\w\s]+)', fileName).group(2)
print name
