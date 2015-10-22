# change python to ruby, very basic
words = line.split(" ")
s = words.select {|w| words.length &gt;=4}
result = s[1...6].join(" ") + "\n" + s[6..-1].join(" ")
