# Gmail email parsing with python when there are unicode characters in body
body = part.get_payload(decode=True).decode(part.get_content_charset())
