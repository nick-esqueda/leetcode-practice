def fib(n, memo={}):
  if n <= 1:
    return n
  if n in memo:
    return memo[n]
  
  res = fib(n - 1, memo) + fib(n - 2, memo)
  memo[n] = res
  return res
