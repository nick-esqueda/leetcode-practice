def quickest_concat(s, words):
  return _quickest_concat(s, words, {})

def _quickest_concat(s, words, memo):
  """
  need to count the length of the shortest path to word completion
  if s is "", return 0
  
  loop over words:
    take each word and see if s.startswith that word
      if it does, get the quickest_concat of the substring without that prefix
      compare that return val to a running min and replace if needed
      
  return the min val
  """
  if s in memo:
    return memo[s]
  if len(s) == 0:
    return 0

  curr_min = float('inf')
  for word in words:
    if s.startswith(word):
      attempt = _quickest_concat(s[len(word):], words, memo) + 1
      if attempt > 0:
        curr_min = min(attempt, curr_min)
      
  memo[s] = curr_min if isinstance(curr_min, int) else -1
  return memo[s]


print(quickest_concat('caution', ['ion', 'caut', 'caution']))



# 2 
def quickest_concat(s, words):
  return _quickest_concat(s, words, {})

def _quickest_concat(s, words, memo):
  if s in memo:
    return memo[s]
  if len(s) == 0:
    return 0
  
  quickest = float('inf')
  for word in words:
    if s.startswith(word):
      attempt = 1 + _quickest_concat(s[len(word):], words, memo)
      if attempt > 0:
        quickest = min(attempt, quickest)
  
  memo[s] = quickest if quickest != float('inf') else -1
  return memo[s]
