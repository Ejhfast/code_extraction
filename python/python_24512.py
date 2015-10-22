# Python regex: Finding input not matching a specific (variable-defined) length
re.findall('(^[0-9]{0,%d}$|[0-9]{%d}[0-9])' % (columns, columns), s)
