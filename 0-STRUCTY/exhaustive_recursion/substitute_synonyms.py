def substitute_synonyms(sentence, synonyms):
  words = sentence.split()
  subs = get_subs(words, synonyms)
  return subs

def get_subs(words, synonyms):
  if len(words) == 0:
    return [""]
  
  first = words[0]
  remainder = words[1:]
  
  possibilities = get_subs(remainder, synonyms)
  
  res = []
  options = []
  if first in synonyms:
    for syn in synonyms[first]:
      options.append(syn)
  else:
    options.append(first)
    
  for option in options:
    for sent in possibilities:
      if sent == "":
        res.append(option)
      else:
        res.append(option + ' ' + sent)
      
  return res
    

    
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
    