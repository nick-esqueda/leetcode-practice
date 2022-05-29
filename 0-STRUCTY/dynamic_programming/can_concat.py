def can_concat(s, words):
  return _can_concat(s, words, 0, {})

def _can_concat(s, words, i, memo):
  """
  loop through words
    if s starts with word, recurse after incrementing i += len(word)
    if recursion returns True at any point, return True
  after looping, return False, because no word matched beginning of substring
  """
  if i in memo:
    return memo[i]
  if i == len(s):
    return True
  
  for word in words:
    if s[i:].startswith(word):
      if _can_concat(s, words, i + len(word), memo):
        memo[i] = True
        return True
      
  memo[i] = False
  return False
  
  
print(can_concat("oneisnone", ["on", "e", "is"]))
