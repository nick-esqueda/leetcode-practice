def intersection(a, b):
  return list(set(a) & set(b))

def intersection(a, b):
  set_a = set(a)
  return [num for num in b if num in set_a]
