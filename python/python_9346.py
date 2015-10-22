# How to insert UTF8 literal in GtkTextView?
const char bullet_utf8[] = "\xe2\x80\xa2";
gtk_text_buffer_insert_at_cursor(textBuffer, bullet_utf8, strlen(bullet_utf8));
