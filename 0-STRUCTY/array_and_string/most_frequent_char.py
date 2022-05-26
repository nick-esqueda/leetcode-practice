from collections import Counter

def most_frequent_char(s):
  char_map = Counter(s)
  
  max_char = None
  for char in char_map:
    if char_map[char] > char_map[max_char]:
      max_char = char
      
  return max_char

print(most_frequent_char('bookeeper'))
