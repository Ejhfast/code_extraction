# Python regex match escaped char
p = re.compile(r':((\\:|[^:])+):')
print p.match(":abc'e12\:3\:text:").group(0)
