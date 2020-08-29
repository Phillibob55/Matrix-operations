matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[9,8,7],[6,5,4],[3,2,1]]

matrix3 = matrix1
order = len(matrix1)
i = j = 0
while (i < 3):
    j = 0
    while(j < 3):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
        j+=1
    i+=1
print(matrix3)
