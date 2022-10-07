def positioning_plants(costs):
  """
  on each call, you will iterate through each flower type and choose one of those
    but you can only choose the ones that have not been previously been chosen
      (this means passing in 'j' as 'prev')
  when you recurse, pass in the next row: 'i + 1' so that we can look the next position
  need to add the value at a certain position + the other choices (recursive calls)
    [if i is out of bounds, return 0 so doesn't contribute to running total]
  need min logic
    take the min total of curr pos + child calls
  return the min total after iterating through all flower types
  """
  return _positioning_plants(costs, 0, None, {})

def _positioning_plants(costs, i, prev_plant_type, memo):
  key = (i, prev_plant_type)
  if key in memo:
    return memo[key]
  if i >= len(costs):
    return 0
  
  min_cost = float('inf')
  for plant_type, cost in enumerate(costs[i]):
    if plant_type is not prev_plant_type:
      min_cost = min(
        cost + _positioning_plants(costs, i + 1, plant_type, memo),
        min_cost
      )
      
  memo[key] = min_cost
  return memo[key]
      

    
print(positioning_plants([
  [4, 3, 7],
  [6, 1, 9],
  [2, 5, 3]
]))
