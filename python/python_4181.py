# Rewrite string formatting without format function
'&amp;category=%s&amp;v=2' % '%2C+'.join(tag.strip() for tag in tags_list)
