# Need modification to regex to work in other situations
v6 = re.findall(r'(?s)----------\s*LOW VOLTAGE SUMMARY BY AREA.*?\r(ACTIVITY|\(VFSCAN\)).+?',wholefile)
