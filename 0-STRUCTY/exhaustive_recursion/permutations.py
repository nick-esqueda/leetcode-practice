def permutations(items):
  """
  to get the permutations for items, you can get the permutations of the items minus an item,
  and then add the item to each of those child permutations, and iterate the item over by 1
  all the way through the item. each iteration is a new permutation
  
  if len of items is 0, return [[]] (a list of 0 permutations)
  remove an item from items and get the permutations of that altered list
  for each permutation that comes back:
    add the item to the permutation
    add a copy of that perm to a running list of perms
    for the length of the perms with the item:
      swap the item backwards by one
      add a copy of that perm to the running list of perms
  return the list of perms
  """
  if len(items) == 0:
    return [[]]
  
  last = items.pop()
  perms = permutations(items)
  
  all_perms = []
  for perm in perms:
    perm.append(last)
    all_perms.append(perm.copy())
    i = len(perm) - 1
    while i > 0:
      perm[i], perm[i - 1] = perm[i - 1], perm[i]
      all_perms.append(perm.copy())
      i -= 1
  
  return all_perms
      
  
print(permutations(['a', 'b', 'c'])) # -> 
# [ 
#   [ 'a', 'b', 'c' ], 
#   [ 'b', 'a', 'c' ], 
#   [ 'b', 'c', 'a' ], 
#   [ 'a', 'c', 'b' ], 
#   [ 'c', 'a', 'b' ], 
#   [ 'c', 'b', 'a' ] 
# ] 
