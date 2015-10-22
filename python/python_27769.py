# Get text from Gtk3 TextView/TextBuffer with formatting tags included in Python
format = textbuffer.register_serialize_tagset('my-tagset')
exported = textbuffer.serialize(textbuffer, format, start, end)
