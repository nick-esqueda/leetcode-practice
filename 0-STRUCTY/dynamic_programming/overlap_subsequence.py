def overlap_subsequence(string_1, string_2, i=0, j=0, memo={}):
  """
  if either string is empty, return 0
  
  decisions:
    delete first char from s1
    delete first char from s2
    if first chars mach, delete both, keep count, and keep going
    
  keep a running count
  if s1[0] == s2[0], set count to 1, and add the result of recursing without the first chars
  else, count = max of recursing without s1[0], and without s2[0]
  
  return the count
  """
  key = (i, j)
  if key in memo:
    return memo[key]
  if i >= len(string_1) or j >= len(string_2):
    return 0
  
  count = 0
  if string_1[i] == string_2[j]:
    count = 1 + overlap_subsequence(string_1, string_2, i + 1, j + 1, memo)
  else:
    without_1 = overlap_subsequence(string_1, string_2, i + 1, j, memo)
    without_2 = overlap_subsequence(string_1, string_2, i, j + 1, memo)
    count = max(without_1, without_2)
    
  memo[key] = count
  return memo[key]
  
