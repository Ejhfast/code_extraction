# match with overlapping - only 3 chars but not 4 - regex
(?&lt;=(?&lt;!\d)\d{3})[^\d]+(?=\d{3}(?!\d))
