def max_palin_subsequence(string):
  return _max_palin_subsequence(string, 0, len(string) - 1, {})

def _max_palin_subsequence(string, start, end, memo):
  """
  use pointers for first and last letter
  
  if first and last letter are same:
    set palin_len to 2
    recurse with start + 1 AND end - 1 and add result to palin_len
  else:
    recurse with start + 1 and add result to palin_len
    recurse with end - 1 and add result to palin_len
    
  return palin_len
  """
  key = (start, end)
  if key in memo:
    return memo[key]
  if start > end:
    return 0
  if start == end:
    return 1
  
  palin_len = 0
  if string[start] == string[end]:
    palin_len = 2
    palin_len += _max_palin_subsequence(string, start + 1, end - 1, memo)
  else:
    no_start = _max_palin_subsequence(string, start + 1, end, memo)
    no_end = _max_palin_subsequence(string, start, end - 1, memo)
    palin_len = max(no_start, no_end)
  
  memo[key] = palin_len
  return memo[key]
  
  
  
print(max_palin_subsequence("luwxult")) # -> 5



# 2
def max_palin_subsequence(string):
  return _max_palin_subsequence(string, 0, len(string) - 1, {})

def _max_palin_subsequence(string, i, j, memo):
  key = (i, j)
  if key in memo:
    return memo[key]
  if j < i:
    return 0
  if j - i == 0:
    return 1

  count = 0
  if string[i] != string[j]:
    count = max(_max_palin_subsequence(string, i + 1, j, memo),
                _max_palin_subsequence(string, i, j - 1, memo))
  else:
    count = 2 + _max_palin_subsequence(string, i + 1, j - 1, memo)
  
  memo[key] = count
  return memo[key]
  