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


# WHY DOES THIS NOT WORK WITH DEFAULT PARAMS FOR i AND memo? 
# 1ST TEST CASE PASSES BUT NOT 2ND
def array_stepper(numbers):
  return _array_stepper(numbers, 0, {})
  
def _array_stepper(numbers, i, memo):
  """
  arr[i] is the number of decisions we can make
  if i == len(nums) - 1 at any point, return True
  if arr[i] == 0, return False
  
  iterate arr[i] number of times starting at i + 1
    recurse with i as the new starting point
      if a true is returned on any iteration, return true
      
  return false if you make it through the loop
  """
  if i in memo:
    return memo[i]
  if i >= len(numbers) - 1:
    return True
  if numbers[i] == 0:
    return False
  
  for j in range(i + 1, numbers[i] + i + 1):
    if _array_stepper(numbers, j, memo) is True:
      memo[i] = True
      return True
    
  memo[i] = False
  return False



# 2 
def array_stepper(numbers):
  return _array_stepper(numbers, 0, {})

def _array_stepper(numbers, i, memo):
  if i in memo:
    return memo[i]
  if i >= len(numbers) - 1:
    return True
  if numbers[i] == 0:
    return False
  
  max_steps = numbers[i]
  for step_size in range(1, max_steps + 1):
    if _array_stepper(numbers, i + step_size, memo):
      memo[i] = True
      return True
  
  memo[i] = False
  return False
