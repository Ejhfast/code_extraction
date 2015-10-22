# Django + Haystack + ElasticSearch advanced lookup
title_sq.add(SQ(title__icontains=word), SQ.OR)
full_text_sq.add(SQ(full_text__icontains=word), SQ.OR)
