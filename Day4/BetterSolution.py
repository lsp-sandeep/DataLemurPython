#%%

def trailing_zeroes(n):
  
  zeroes, multiple = 0, 5
  
  while n >= multiple:

    zeroes += n // multiple
    multiple *= 5

  return zeroes

#%%

print(trailing_zeroes(5))

print(trailing_zeroes(10))

#%%