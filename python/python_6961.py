# Generating random Unicode between certain range
return unichr(random.choice((0x300, 0x2000)) + random.randint(0, 0xff))
