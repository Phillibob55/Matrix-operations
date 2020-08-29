def cofactors(matrix):
    cofactor = [[0,0],[0,0]]
    for x in range(3):
        for y in range(3):
            pass

def determinant(matrix):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return det

matrix = [[1,2],[3,4]]
det = determinant(matrix)
cofactors(matrix)
print(det)