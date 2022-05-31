def subsets(elements):
  """
  iterating through elements, you can either:
    make a decision to include the element
    make a decision to exclude the element
  """
  all_subsets = []
  get_subsets(elements, 0, [], all_subsets)
  return all_subsets
  

def get_subsets(elements, i, subset, all_subsets):
  if i == len(elements):
    all_subsets.append(subset)
    return
  
  get_subsets(elements, i + 1, subset, all_subsets)
  new_subset = subset[:]
  new_subset.append(elements[i])
  get_subsets(elements, i + 1, new_subset, all_subsets)
  
  
print(subsets(['a', 'b', 'c'])) # ->
# [
#   [],
#   [ 'c' ],
#   [ 'b' ],
#   [ 'b', 'c' ],
#   [ 'a' ],
#   [ 'a', 'c' ],
#   [ 'a', 'b' ],
#   [ 'a', 'b', 'c' ]
# ]
