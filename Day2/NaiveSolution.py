#%%
def is_same_stripes(matrix):

    m, n = len(matrix), len(matrix[0])

    for ir in range(0, m):
        
        r, c = ir, 0
        
        val = matrix[r][c]
        while r < m and c < n:

            if matrix[r][c] != val:
                return False

            r, c = r + 1, c + 1

    for ic in range(0, n):

        r, c = 0, ic

        val = matrix[r][c]
        while r < m and c < n:

            if matrix[r][c] != val:
                return False

            r, c = r + 1, c + 1

    return True

#%%

matrix = [[42, 7, 13, 99], [6, 42, 7, 13], [1, 6, 42, 7]]

print(is_same_stripes(matrix))

matrix = [[42, 7, 13, 99], [6, 42, 7, 13], [1, 6, 42, 8]]

print(is_same_stripes(matrix))


#%%
