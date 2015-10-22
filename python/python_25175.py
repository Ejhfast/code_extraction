# Why use an ampersand character (&) in PyQt Strings for GUI elements?
QLineEdit* phoneEdit = new QLineEdit(this);
QLabel* phoneLabel = new QLabel("&amp;Phone:", this);
phoneLabel-&gt;setBuddy(phoneEdit);
