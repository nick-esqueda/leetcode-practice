def decompress_braces(string):
  """
  declare stack
  push regular chars and numbers to stack
  if you come across {, do nothing
  if you come across }, enter a subroutine:
    pop off the stack until you've popped a number
    all of the things you popped need to be concatted to a string
    after you've popped the number, multiply that concatted string by num
    reverse the string at the end (can this be optimized?)
    ^ after all this, push the result to the stack and keep iterating after the }
  after iterating through string, the stack will be full
  return the joined stack
  """
  numbers = "123456789"
  stack = []
  for char in string:
    if char == '{':
      continue
    elif char == '}':
      group = ""
      while stack[-1] not in numbers:
        top = stack.pop()
        group = top + group
      num = stack.pop()
      group = group * int(num)
      stack.append(group)
    else:
      stack.append(char)
      
  return ''.join(stack)
  
  
print(decompress_braces("z3{a2{xy}b}"))
