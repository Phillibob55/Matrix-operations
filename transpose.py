matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
order = len(matrix)
i=j=z=temp=0
while(z<order):
    i = z
    j = z
    while(i<order):
        while(j<order):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
            j+=1
        i+=1
    
    z+=1
print(matrix)

