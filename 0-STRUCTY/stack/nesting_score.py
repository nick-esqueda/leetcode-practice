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
      


# 2
def nesting_score(string):
  sta = []
  for brack in string:
    if brack == "[":
      sta.append(0)
    elif brack == "]":
      if sta[-1] == 0:
        sta[-1] += 1
      else:
        pop_sum = 0
        while sta[-1] != 0:
          pop_sum += sta.pop()
        sta[-1] += pop_sum * 2
  return sum(sta)

def nesting_score(string):
  sta = [0]
  for brack in string:
    if brack == "[":
      sta.append(0)
    elif brack == "]":
      top = sta.pop()
      if top == 0:
        sta[-1] += 1
      else:
        sta[-1] += top * 2
  return sta[0]
