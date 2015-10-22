# Why can't I addstr() to last row/col in python curses window?
screen.addstr(ScreenH - 1, ScreenW - 1 - cloclen, cloc,  curses.color_pair(1))
                                   ^^^
