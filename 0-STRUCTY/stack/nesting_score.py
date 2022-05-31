def nesting_score(string):
  """
  [[][][[][]]] -> 12
  i
  sta = [0,0]
  
  declare sta with a 0 on top
  if you come across an open, add another 0 to the top
  if you come across a close, pop off the top
    if popped is 0, add 1 to what's on the top of the stack
    if popped is non-0, multiply that num by 2 and add that to the new top of stack
  after iterating through string, return the num on the stack
  """
  stack = [0]
  
  for brack in string:
    if brack == "[":
      stack.append(0)
    else:
      top = stack.pop()
      if top == 0:
        stack[-1] += 1
      else:
        stack[-1] += top * 2
        
  return stack[0]
      
