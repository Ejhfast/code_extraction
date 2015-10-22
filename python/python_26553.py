# Python: Skip 'for' loop interation
if current_index+1 &lt; len(file_content):
    if file_char == '/' and file_content[current_index+1] == '*':
        multi_line_comment = True
