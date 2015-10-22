# How do you save each element of a list in a .txt file, one per line?
outfile = open("file_path", "w")
print &gt;&gt; outfile, "\n".join(str(i) for i in your_list)
outfile.close()
