def five_sort(nums):
  i, j = -1, 0
  while j < len(nums):
    if nums[j] != 5:
      i += 1
      nums[i], nums[j] = nums[j], nums[i]
    j += 1
    
  return nums

print(five_sort([12, 5, 1, 5, 12, 7]))


def five_sort(nums):
  i, j = 0, len(nums) - 1
  while i < j:
    if nums[j] == 5:
      j -= 1
    elif nums[i] == 5:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
      
  return nums
    

print(five_sort([12, 5, 1, 5, 12, 7]))
