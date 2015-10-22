# Python/imaplib - How to get messages' labels?
t, d = imapconn.uid('FETCH', uid, '(X-GM-LABELS)')
or
t, d = imapconn.fetch(uid, '(X-GM-LABELS)')
