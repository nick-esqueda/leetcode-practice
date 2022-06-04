def detect_dictionary(dictionary, alphabet):
  w = 0
  while w < len(dictionary) - 1:
    word_1 = dictionary[w]
    word_2 = dictionary[w + 1]
    if not lexical_order(word_1, word_2, alphabet):
      return False
    w += 1
  return True

def lexical_order(word_1, word_2, alphabet):
  i = 0
  j = 0
  while i < len(word_1) and j < len(word_2):
    if word_1[i] != word_2[j]:
      return alphabet.index(word_1[i]) < alphabet.index(word_2[j])
    i += 1
    j += 1
  return i == len(word_1)
