# Python IMAP - Read Gmail with '+' in email address
result,data = self.M.uid('search', None, '(SENTSINCE {date})'.format(date=date),
    ('TO example+test1@gmail.com'))
