# pyqt: Get current line number of text cursor
QTextCursor cursor = ui.textEdit-&gt;textCursor();
int y = cursor.blockNumber() + 1;
int x = cursor.columnNumber() + 1;
