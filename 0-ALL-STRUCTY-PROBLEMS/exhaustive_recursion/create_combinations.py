def create_combinations(items, k):
  """
  if k == len(items), return the items in a list, because that is 1 combination of items
  branch off, removing an item and decrementing k
  branch off, removing an item and leaving k the same
  add the item that you removed back into each comb in the first branch
    add those with the other branch and return
  """
  if k == 0: 
    return [[]]
  if k > len(items):
    return []
  
  first = items[0]
  minus_one = create_combinations(items[1:], k - 1)
  minus_zero = create_combinations(items[1:], k)
  
  for comb in minus_one:
    comb.append(first)
  
  return minus_one + minus_zero
  
      

print(create_combinations(['q', 'r', 's', 't'], 3))
