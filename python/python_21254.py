# Vim: Highlight a Single Character at Column 80
hi Bang ctermfg=red guifg=red
match Bang /\%&gt;79v.*\%&lt;81v/
