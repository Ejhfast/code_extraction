# Is there an easy way to abort with status code 429?
if requests_made &gt;= max_requests:
    return '429 error', 429
