# Cleaner regex for removing characters before dot or slash
re.sub(r"^[^.-]*[.-]\s*","",some_string)
