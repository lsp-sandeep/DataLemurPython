#%%
def is_same_stripes(matrix):

    diagonals = {}

    m, n = len(matrix), len(matrix[0])

    for r in range(0, m):

        for c in range(0, n):

            if c - r in diagonals:
                if matrix[r][c] != diagonals[c - r]:
                    return False
            else:
                diagonals[c - r] = matrix[r][c]
        
    return True

#%%

matrix = [[42, 7, 13, 99], [6, 42, 7, 13], [1, 6, 42, 7]]

print(is_same_stripes(matrix))

matrix = [[42, 7, 13, 99], [6, 42, 7, 13], [1, 6, 42, 8]]

print(is_same_stripes(matrix))


#%%
