# Python sorting problem
m = re.match('Season ([0-9]+), Episode ([0-9]+): .*', s)
(season, episode) = (int(m.group(1)), int(m.group(2)))
