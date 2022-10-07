from collections import deque

def merge_sort(nums):
  """
  find a midpoint in nums
  merge_sort both halves of nums
  return the merge of (listA, listB)
  """
  if len(nums) <= 1:
    return nums
  
  mid = len(nums) // 2
  left = merge_sort(nums[0:mid])
  right = merge_sort(nums[mid:])
  return merge(left, right)
  

def merge(listA, listB):
  """
  need to take the lesser index 0 val of the two lists and put it in a rtn arr
  if you run out of nums in one list, put the rest of the other list at the end of rtn arr
  """
  merged = []
  qA = deque(listA)
  qB = deque(listB)
  while qA and qB:
    if qA[0] < qB[0]:
      merged.append(qA.popleft())
    else:
      merged.append(qB.popleft())
  
  if qA:
    merged += qA
  if qB:
    merged += qB
    
  return merged
  
print(merge([1, 2, 6], [-2, 5, 7]))
