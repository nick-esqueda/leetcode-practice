def pair_sum(numbers, target_sum):
  compliments = {}
  
  for i, num in enumerate(numbers):
    compliment = target_sum - num
    
    if compliment in compliments:
      return (compliments[compliment], i)
    else:
      compliments[num] = i
