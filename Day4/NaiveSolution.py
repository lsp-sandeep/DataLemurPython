#%%

def trailing_zeroes(n):
  
  fives, twos = 0, 0
  
  for i in range(1, n+1):
    
    num = i
    
    while num % 5 == 0:
      
      fives += 1
      num //= 5

    num = i
    
    while num % 2 == 0:
      
      twos += 1
      num //= 2
  
  return min(fives, twos)

#%%

print(trailing_zeroes(5))

print(trailing_zeroes(10))

#%%