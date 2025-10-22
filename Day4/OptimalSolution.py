#%%

def trailing_zeroes(n):
  
  fives, twos = 0, 0
  
  for i in range(1, n+1):
    
    num = i
    
    while num % 5 == 0:
      
      fives += 1
      num //= 5
  
  return fives

#%%

print(trailing_zeroes(5))

print(trailing_zeroes(10))

#%%