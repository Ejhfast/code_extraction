# How to pack bits into variable length words in python?
def vectorize_key(key,word_size=32):
    return (reduce(lambda p, (e,f) : p | (e &lt;&lt; f),((x[i],i*8) for i in range(word_size/8)),0) for x in split((ord(k) for k in key),word_size/8))
