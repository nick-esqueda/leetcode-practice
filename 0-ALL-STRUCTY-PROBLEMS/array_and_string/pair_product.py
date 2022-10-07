def pair_product(numbers, target_product):
  divisors = {}
  
  for i, num in enumerate(numbers):
    divisor = target_product / num
    
    if divisor in divisors:
      return (divisors[divisor], i)
    else: 
      divisors[num] = i
