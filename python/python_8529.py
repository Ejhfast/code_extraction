# How do I format text from a file in Python?
def print_table(lines, col_num, col_width):
    for line_ix in range(0, len(lines), col_num):
        print ' -- '.join([line.strip().ljust(col_width) for line in lines[line_ix:line_ix+col_num]])
