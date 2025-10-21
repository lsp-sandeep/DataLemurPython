def convertToBase13(num):
  
  if num < 0:
    return "-" + convertToBase13(-num)
  
  ans = ""
  
  div, rem = num // 13, num % 13
  
  if rem == 10:
    ans += "A"
  elif rem == 11:
    ans += "B"
  elif rem == 12:
    ans += "C"
  else:
    ans += str(rem)
    
  if div > 0:
    return convertToBase13(div) + ans
  else:
    return ans