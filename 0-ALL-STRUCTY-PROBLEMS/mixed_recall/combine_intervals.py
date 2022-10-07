def combine_intervals(intervals):
  """
  sort the intervals by start time
  push the start to a return list []
  loop through the rest of the intervals
  if a start time is less than the ending time of the last combined inter:
    make a new inter with the start of the last comb inter and
      the end of whichever end is greater - comb inter or curr inter
    reassign the last idx in the comb list to the inter you just created 
    keep iterating
  else:
    push that inter to the comb inter list
  return list
  """
  intervals.sort(key=lambda inter: inter[0])
  
  merged = []
  for cur_inter in intervals:
    if len(merged) == 0:
      merged.append(cur_inter)
      
    last_merged = merged[-1]
    
    if cur_inter[0] <= last_merged[1]:
      new_start = last_merged[0]
      new_end = cur_inter[1] if cur_inter[1] > last_merged[1] else last_merged[1]
      merged[-1] = (new_start, new_end)
    else:
      merged.append(cur_inter)
      
  return merged
  
  
intervals = [
  (1, 4),
  (12, 15),
  (3, 7),
  (8, 13),
]
print(combine_intervals(intervals))
