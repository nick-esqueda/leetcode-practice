def anagrams(s1, s2):
  return get_char_counts(s1) == get_char_counts(s2)

def get_char_counts(s):
  counts = {}
  for char in s:
    if char in counts:
      counts[char] += 1
    else:
      counts[char] = 1
  return counts
    
print(anagrams('cats', 'tocs')) # -> False
