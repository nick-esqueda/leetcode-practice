def lexical_order(word_1, word_2, alphabet):
  """
  if the first letter of one word is before the other, return true
  if not, then you have to find the first discrepancy and see which one comes first
  if one word runs out of letters while trying to find diff, that word is first
  """
  i = 0
  j = 0
  while i < len(word_1) and j < len(word_2):
    if word_1[i] != word_2[j]:
      return alphabet.index(word_1[i]) < alphabet.index(word_2[j])
    i += 1
    j += 1

  return i == len(word_1)
