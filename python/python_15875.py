# Restricting the area of text that is searched by python
relevant = re.search(r"MAIN FISHERMAN(.*)SECONDARY FISHERMAN", html, re.DOTALL).group(1)
found = relevant.count("SEA BASS")
