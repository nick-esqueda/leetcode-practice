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


def subsets(elements):
  """
  subsets of any list are a combination of the subsets without an element, combined with 
    those subsets WITH the element
  """
  if len(elements) == 0:
    return [[]]
  
  last = elements.pop()
  subs_without_last = subsets(elements)
  
  subs_with_last = []
  for sub in subs_without_last:
    sub_copy = sub.copy()
    sub_copy.append(last)
    subs_with_last.append(sub_copy)
    
  return subs_without_last + subs_with_last
  
  
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
