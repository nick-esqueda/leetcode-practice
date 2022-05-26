def non_adjacent_sum(nums, memo={}):
  """
  if nums has length of 1, return that num
  if nums has length of 2, return the max of those 2 nums
  
  need to take the max of you deciding to take the first number vs leaving the first num out
  add the first number to that max and store it inside memo with key of tuple(list)
  """
  key = tuple(nums)
  if key in memo:
    return memo[key]
  if len(nums) == 1:
    return nums[0]
  if len(nums) == 2:
    return max(nums)

  with_num = non_adjacent_sum(nums[2:], memo) + nums[0]
  without_num = non_adjacent_sum(nums[1:], memo)
  memo[key] = max(with_num, without_num)
  return memo[key]
