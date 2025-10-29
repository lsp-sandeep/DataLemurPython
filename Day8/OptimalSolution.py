
# Optimal Approach
def fizz_buzz_sum(target):
  '''
  Let the dividend of target - 1 with n be div(n).
  Let the sum of integers from 1 to dividen of n be S(n)
  
  Result = 3 * S(div(3)) + 5 * S(div(5)) - 15 * S(div(15))
  
  Time Complexity : O(1)
  Space Complexity : O(1)
  '''
  res = 0
  div_3, div_5, div_15 = (target - 1) // 3, (target - 1) // 5, (target - 1) // 15
  sum_3 = 3 * div_3 * (div_3 + 1) // 2
  sum_5 = 5 * div_5 * (div_5 + 1) // 2
  sum_15 = 15 * div_15 * (div_15 + 1) // 2
  res = sum_3 + sum_5 - sum_15
  
  return res