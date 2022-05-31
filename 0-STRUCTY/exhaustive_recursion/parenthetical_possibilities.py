def parenthetical_possibilities(s):
  """
  if s is '', return [""]
  declare res = []
  go through each char in s
  if char is not in parens
    save the first char
    recurse without that char
    add that first char to the front of each of the return items
    append those return items to res
  if you reach parens
    loop through each item in paren
      save each char as 'first'
      recurse starting after the parens
      add that first char to the front of each of the return items
      append those to res
  return res
  """
  if len(s) == 0:
    return [""]
  
  res = []
  
  if s[0] == "(":
    chars = ""
    i = 1
    while s[i] != ")":
      chars += s[i]
      i += 1
    for c in chars:
      results = parenthetical_possibilities(s[i + 1:])
      for j in range(len(results)):
        results[j] = c + results[j]
      res += results
  else:
    first = s[0]
    results = parenthetical_possibilities(s[1:])
    for j in range(len(results)):
      results[j] = first + results[j]
    res += results
  
  return res
    
    
print(parenthetical_possibilities("(qr)ab(stu)c") )
