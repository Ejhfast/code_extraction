# python 3.2 UnicodeEncodeError: 'charmap' codec can't encode character '\u2013' in position 9629: character maps to <undefined>
with open('filename', 'w', encoding='utf-8') as f:
    print(r['body'], file=f)
