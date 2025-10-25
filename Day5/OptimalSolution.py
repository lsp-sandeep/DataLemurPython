# Optimal Solution

def intersection(a, b):
  '''
  Use sets to reduce the search time complexity to O(1),
  and then use list comprehension to find the elements in both sets
  
  Time Complexity: O(min(m, n))
  Space Complexity: O(m + n)
  '''
  
  a_set, b_set = set(a), set(b)
  
  if len(a_set) <= len(b_set):
    return [el for el in a_set if el in b_set]
  else:
    return [el for el in b_set if el in a_set]
  
