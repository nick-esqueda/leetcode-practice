def anagrams(s1, s2):
  if len(s1) != len(s2): return False

  s1_map = {}
  s2_map = {}
  i = 0
  while i < len(s1): 
    if s1[i] not in s1_map:
      s1_map[s1[i]] = 1
    else:
      s1_map[s1[i]] += 1
    if s2[i] not in s2_map:
      s2_map[s2[i]] = 1
    else:
      s2_map[s2[i]] += 1
    
    i += 1
      
  return s1_map == s2_map
    
print(anagrams('cats', 'tocs')) # -> False
