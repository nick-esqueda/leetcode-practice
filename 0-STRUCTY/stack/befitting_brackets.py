def befitting_brackets(string):
  """
  push open brackets to a stack
  if you come across a closing bracket, check the top of stack to see if it matches
    (use hashmap to check matches)
    if so, pop top off
    if not, return False
  if the stack is empty before finishing the string, return False
  if anything is left on the stack, return False
  """
  brackets = {
    "(": ")",
    "[": "]",
    "{": "}"
  }

  sta = []
  for c in string:
    if c in brackets:
      sta.append(c)
    else:
      if len(sta) == 0:
        return False
      
      top = sta.pop()
      if brackets[top] != c:
        return False

  return len(sta) == 0


print(befitting_brackets('[][}'))



# 2
def befitting_brackets(string):
  map = {
    "(": ")",
    "[": "]",
    "{": "}"
  }
  
  sta = []
  for char in string:
    if char in map:
      sta.append(char)
    else:
      if not sta or char != map[sta.pop()]:
        return False
  return len(sta) == 0
  
  