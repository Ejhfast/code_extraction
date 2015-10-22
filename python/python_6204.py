# printing to right side or bottom side of terminal using (n)curses
mvprintw(COLS-length("msg"),1,"msg");
mvprintw(0,LINES-1,"message number 2");
mvprintw(COLS-length("here is more"),LINES-1,"here is more");
