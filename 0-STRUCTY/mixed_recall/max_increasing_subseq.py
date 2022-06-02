def max_increasing_subseq(numbers):
  return _max_increasing_subseq(numbers, 0, float('-inf'), {})

def _max_increasing_subseq(numbers, i, prev, memo):
  key = (i, prev)
  if key in memo:
    return memo[key]
  if i == len(numbers):
    return 0
  
  cur = numbers[i]
  
  remove_num = _max_increasing_subseq(numbers, i + 1, prev, memo)
  keep_num = float('-inf')
  if cur > prev:
    keep_num = 1 + _max_increasing_subseq(numbers, i + 1, cur, memo)
    
  memo[key] = max(remove_num, keep_num)
  return memo[key]


numbers = [42, 50, 51, 60, 55, 70, 4, 5, 70]
print(max_increasing_subseq(numbers))
