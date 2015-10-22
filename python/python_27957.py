# How can I perform a temporary assignment in a generator expression?
end = min(x for x in (fileStr.find(key) for key in keys)
          if x &gt; index)
