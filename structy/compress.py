def compress(s):
  """
  start i and j at 0
  iterate through s
  if j is the same as i, keep iterating
  if j is different than i, store "num" as j - 1
  append that num and the char at i to a result string
    UNLESS the num is 1. if so, just push the letter
  move i to j
  keep iterating
  """
  s += "!"
  res = ""
  i, j = 0, 0
  while j < len(s):
    if s[j] == s[i]:
      j += 1
    else:
      count = j - i
      if count > 1:
        res += f"{count}{s[i]}"
      else:
        res += f"{s[i]}"
      i = j
      j += 1
      
  return res
