# other than combining the new_title statements,how do i refactor this code using Python3? please help:(
return ' '.join((new[0].upper() + new[1:]) if (ix == 0 or new not in small_words)
  else new for (ix, new) in enumerate(title.lower().split()))
