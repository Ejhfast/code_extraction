# Issues writing beautifulsoup output to .txt
to_write = tag.get_text() + "\n"
f.write(to_write.encode("utf-8"))
