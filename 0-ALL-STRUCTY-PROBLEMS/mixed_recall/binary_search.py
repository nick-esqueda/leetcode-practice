def binary_search(numbers, target):
  lo = 0
  hi = len(numbers) - 1
  
  while lo <= hi:
    mid = (hi + lo) // 2
    
    if target < numbers[mid]:
      hi = mid - 1
    elif target > numbers[mid]:
      lo = mid + 1
    else:
      return mid
  
  return -1
