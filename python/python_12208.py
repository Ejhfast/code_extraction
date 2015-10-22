# Accessing capture groups during substitution
re.sub(r'\d+\.\d*', lambda match: str(int(round(float(match.group(0))))), line)
