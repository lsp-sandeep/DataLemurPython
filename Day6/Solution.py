# Optimal Approach

def another_one(digits):
    '''
    1) Check each digit if adding one makes it >9
    2) If >9 then make it 0 and carry forward 1 until the next digit is <9
    3) If all are 9 then append a 1 at the start of the digits which are made 0
    4) If found a digit <9 then just add 1 and return the array
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    
    carry = 0
    
    for i in range(len(digits)-1,-1,-1):
    
      if digits[i] + 1 > 9:
        digits[i] = 0
        carry = 1
    
      else:
        digits[i] += 1
        carry = 0
        break
    
    if carry == 1:
      digits = [carry] + digits

    return digits