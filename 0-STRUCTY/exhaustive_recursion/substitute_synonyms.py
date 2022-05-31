def substitute_synonyms(sentence, synonyms):
  """
  declare result var = [] (array of strings)
  declare options var = []
  strip out the first "word" (a word stops at a space)
  if the first word is in the map:
    push each syn to the options var
  else it's not in the map:
    add that word to options var
    
  for each option: (can be optimized with memoization)
    recurse with the rest of the sentence (minus first word)
    add the syn to the beginning of each of those sentences
    push those modified sentences to the result var
    
  return result
  """
  if len(sentence) == 0:
    return [""]
  
  result = []
  options = []
  
  words = sentence.split()
  first_word = words[0]
  remainder = " ".join(words[1:])
    
  if first_word in synonyms:
    for syn in synonyms[first_word]:
      options.append(syn)
  else:
    options.append(first_word)
    
  for option in options:
    sentences = substitute_synonyms(remainder, synonyms)
    for sentence in sentences:
      if sentence == "":
        result.append(option)
      else:
        result.append(option + ' ' + sentence)
      
  return result
    
    
sentence = "follow the yellow brick road"
synonyms = {
  "follow": ["chase", "pursue"],
  "yellow": ["gold", "amber", "lemon"],
}

print(substitute_synonyms(sentence, synonyms))
# [
#   'chase the gold brick road',
#   'chase the amber brick road',
#   'chase the lemon brick road',
#   'pursue the gold brick road',
#   'pursue the amber brick road',
#   'pursue the lemon brick road'
# ]
    
