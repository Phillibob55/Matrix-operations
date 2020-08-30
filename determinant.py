def cofactors(matrix):
    cofactor = [[0,0],[0,0]]
    for x in range(2):
        for y in range(2):
            cofactor[x][y] = 1
    return cofactor

def determinant(matrix):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return det

matrix = [[1,4,7],[2,5,8],[3,6,9]]
#det = determinant(matrix)
print(cofactors(matrix))
#print(det)