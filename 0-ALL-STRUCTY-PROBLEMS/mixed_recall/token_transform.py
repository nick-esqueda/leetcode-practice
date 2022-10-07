def token_transform(s, tokens):
  output = []
  i = 0 
  j = 1
  while i < len(s):
    if s[i] != "$":
      output.append(s[i])
      i += 1
      j += 1
    elif s[j] != "$":
      j += 1
    else:
      key = s[i:j + 1]
      if "$" in tokens[key]:
        tokens[key] = token_transform(tokens[key], tokens)
      output.append(tokens[key])
      i = j + 1
      j = i + 1
  return ''.join(output)

        
tokens = {
  '$ADJECTIVE_1$': "quick",
  '$ADJECTIVE_2$': "eager",
  '$ADVERBS$': "$ADJECTIVE_1$ly and $ADJECTIVE_2$ly",
  '$VERB$': "hopped $DIRECTION$",
  '$DIRECTION$': "North",
}
print(token_transform("the $ADJECTIVE_1$ fox $ADVERBS$ $VERB$ward", tokens))
