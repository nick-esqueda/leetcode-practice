def paired_parentheses(string):
  """
  all parens must close
  start parens must come first before a closing paren
  the number of open and close parens must match
  
  if you come across an open paren, push it to a stack
  if you come across a close paren, pop the top of the stack
    if the stack is empty when you try to pop, return False
  after iterating through whole string, if stack has something one it, return False
  else, return True
  """
  if len(string) == 0:
    return True
  
  sta = []
  for c in string:
    if c == "(":
      sta.append(c)
    elif c == ")":
      if len(sta) == 0:
        return False
      else:
        sta.pop()
  
  return len(sta) == 0

print(paired_parentheses("()rose(jeff"))


def paired_parentheses(string):
  count = 0
  
  for c in string:
    if c == "(":
      count += 1
    elif c == ")":
      count -= 1
      if count < 0:
        return False
      
  return count == 0
      