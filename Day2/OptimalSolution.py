#%%
def is_same_stripes(matrix):

    m, n = len(matrix), len(matrix[0])

    for r in range(1, m):

        for c in range(1, n):

            if matrix[r][c] != matrix[r-1][c-1]:
                return False
        
    return True

#%%

matrix = [[42, 7, 13, 99], [6, 42, 7, 13], [1, 6, 42, 7]]

print(is_same_stripes(matrix))

matrix = [[42, 7, 13, 99], [6, 42, 7, 13], [1, 6, 42, 8]]

print(is_same_stripes(matrix))


#%%
