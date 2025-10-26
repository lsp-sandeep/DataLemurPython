
# Solution

def weakest_strong_link(strength):
    '''
    Time Complexity : O(m*n)
    Space Complexity : O(m + n)
    '''
    m, n = len(strength), len(strength[0])
    min_rows = []
    max_cols = []
  
    for i in range(m):
        for j in range(n):
            if len(min_rows) <= i:
                min_rows.append(strength[i][j])
            else:
                min_rows[i] = min(min_rows[i], strength[i][j])

            if len(max_cols) <= j:
                max_cols.append(strength[i][j])
            else:
                max_cols[j] = max(max_cols[j], strength[i][j])
        
    res = [el for el in set(min_rows) if el in set(max_cols)]
        
    return -1 if len(res) == 0 else res[0]
    
