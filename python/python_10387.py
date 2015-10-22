# Looping within a regex search
corelist = [m.group(1) for m in
            re.finditer(r"\b([0-9]+)ProcessorsRequested\b", output)]
