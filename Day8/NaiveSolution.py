# Naive Approach
def fizz_buzz_sum(target):
  '''
  Iterate from 1 to target-1 to sum the numbers divisible by 3 or 5
  
  Time Complexity : O(n)
  Space Complexity : O(1)
  '''
  res = 0
  
  for i in range(1, target):
    if i % 3 == 0 or i % 5 == 0:
      res += i
  
  return res