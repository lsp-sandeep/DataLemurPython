# Naive Approach

def intersection(a, b):
  '''
  Use list comprehension to check if an element exists in both lists
  
  Time Complexity: O(m*n)
  Space Complexity: O(1)
  '''
  
  
  res = [el for el in a if el in b]
  
  return res