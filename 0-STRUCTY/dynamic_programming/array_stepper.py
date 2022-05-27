def array_stepper(numbers):
  """
  if numbers had a len of 1, you return True, because you need to take 0 steps
    in other words - if the index == len(numbers) - 1, return True
  if you're at a 0 and you're not on the last index, return False
  
  arr[i] is the amount of steps/decisions that you can make
  of all of the decisions that you can make, you should always choose the greatest value
  
  1. take all of the nums that are arr[i] indices away from the starting point
  2. find the index that holds the max number
  3. move i to that index
  """
  
  i = 0
  while i < len(numbers) - 1:
    steps = numbers[i]
    
    if steps == 0 and i != len(numbers) - 1:
      return False
    
    max_option_i = i
    max_option = float('-inf')
    for j in range(i + 1, i + steps + 1):
      if j == len(numbers) - 1:
        return True
      elif j >= len(numbers):
        break
        
      if numbers[j] > max_option:
        max_option = numbers[j]
        max_option_i = j
        
    i = max_option_i
      

print(array_stepper([2, 4, 2, 0, 0, 1]))
