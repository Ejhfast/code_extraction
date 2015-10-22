# Remove sequential characters from the start of a string
title = re.sub(r'^([a-z]\s)*', '', 'a b c d Wikipedia Reference')
