def token_replace(s, tokens):
  """
  iterate through s and concat to a res str until you see a $
  save the $ and every char following in a new var until the next $
  after hitting the 2nd $, use the var to look the key up
  concat that word to the res str
  keep iterating
  """
  res = ""
  token = ""
  is_token = False
  i = 0
  while i < len(s):
    char = s[i]
    
    if char == "$" and is_token is False:
      token += char
      is_token = True
      i += 1
      continue
    if char == "$" and is_token is True:
      token += char
      res += tokens[token]
      token = ""
      is_token = False
      i += 1
      continue
    
    if is_token:
      token += char
    else:
      res += char 
      
    i += 1

  return res

tokens = {
  '$second$': 'beta',
  '$first$': 'alpha',
  '$third$': 'gamma',
}
print(token_replace('$first$second$third$', tokens) )
