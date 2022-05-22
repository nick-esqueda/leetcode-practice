def uncompress(s):
  """
  declare a hashset to store letters
  declare result string
  declare a "stop" pointer at 0
  iterate over s
  once you come across something that is in the letter hashset:
    take s from "stop" to prev i, typecast to num, multiply the letter by
      the num, and push that uncompressed version to a string
    move the stop var up to curr i
    keep iterating 
  return the new string at end
  """
  uncompressed = []
  letters = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
  stop = 0
  
  for i, c in enumerate(s):
    if c.lower() in letters:
      num = int(s[stop:i])
      uncompressed.append(c * num)
      stop = i + 1
  
  return ''.join(uncompressed)

print(uncompress("3n12e2z")) # -> 'ccaaat'
