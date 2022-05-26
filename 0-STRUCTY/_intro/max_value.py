def max_value(nums):
  curr_max = float('-inf')
  for num in nums:
    if num > curr_max:
      curr_max = num
      
  return curr_max
