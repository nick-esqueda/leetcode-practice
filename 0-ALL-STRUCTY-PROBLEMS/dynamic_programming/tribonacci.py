def tribonacci(n, memo={}):
  if n in memo:
    return memo[n]
  if n <= 1:
    return 0
  if n == 2:
    return 1
  
  memo[n] = tribonacci(n - 1, memo) + tribonacci(n - 2, memo) + tribonacci(n - 3, memo)
  return memo[n]


# 2
def tribonacci(n):
  return _trib(n, {})

def _trib(n, memo):
  if n in memo:
    return memo[n]
  if n <= 1:
    return 0
  if n == 2:
    return 1
  
  memo[n] = _trib(n - 1, memo) + _trib(n - 2, memo) + _trib(n - 3, memo)
  return memo[n]
