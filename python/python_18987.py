# regex capture everything except a word (break at a word not character)
loc = re.compile('(?:^|or)\s*([^,]+),\s([A-Z]+)')
