class Matrix:
    def __init__(self, m , n):
        self.m = m
        self.n = n
        self.create()
    
    @classmethod
    def create(cls):
        values_for_matrix = input("Give values for the matrix in the format, <row 1 > <row 2> <row 3>..... Use spaces for separation. e.g values for a matrix with 3 x 3 order: 1 2 3 4 5 6 7 8 9:" )
        values_for_matrix = values_for_matrix.split()
        print(values_for_matrix)
        for x in values_for_matrix:
            for y in range(0,m):
                for z in range(0,n):
                    a = x + y + z
                    
        return a

'''
Add using dunder __add__()
    @classmethod
    def add(cls, mat1, mat2):
        mat1_size = Matrix.contents(mat1)
        mat2_size = Matrix.contents(mat2)
        
        if (mat1_size == mat2_size) and (len(mat1) == len(mat2)):
            # add matrices mat1 and mat2
            rows = len(mat1)
            columns = mat1_size/rows
            mat3 = mat1
            i = j = 0
            while (i < rows):
                j = 0
                while(j < columns):
                    mat3[i][j] = mat1[i][j] + mat2[i][j]
                    j+=1
                i+=1
            return mat3
        else:
            print("Matrices donot have the same order!")
'''
'''
    @classmethod
    def subtract(cls, mat1, mat2):
        mat1_size = Matrix.contents(mat1)
        mat2_size = Matrix.contents(mat2)
        
        if (mat1_size == mat2_size) and (len(mat1) == len(mat2)):
            rows = len(mat1)
            columns = mat1_size/rows
            mat3 = mat1
            i = j = 0

            while (i < rows):
                j = 0
                while(j < columns):
                    mat3[i][j] = mat1[i][j] + mat2[i][j]
                    j+=1
                i+=1
            return mat3
        else:
            print("Matrices donot have the same order!")
'''
'''
    @classmethod
    def contents(cls, mat):
        count = 0
        for x in len(mat):
            count += len(x)
        return count

'''
'''
Out put using dunder __str__()
    @classmethod
    def output(cls, mat):
        for x in mat:
            print(x)
'''

'''
Make multiplicaion possible by using dunder __mul__() and __rmul__()
    @classmethod
    def multiply(cls, mat1, mat2):
        if isinstance(mat1,Matrix) and isinstance(mat2,Matrix):
            return Matrix.matrix_product(mat1, mat2)

        elif isinstance(mat1,Matrix) or isinstance(mat2,Matrix):
            return Matrix.scalar_product(mat1,mat2)

    @classmethod
    def scalar_product(cls, mat1, mat2):
        pass
    
    @classmethod
    def matrix_product(cls, mat1, mat2):
        pass
'''
    
    @classmethod
    def transpose(cls, mat):
        pass
    
    @classmethod
    def determinant(cls, mat):
        pass

    # ***** Adjoint before determinant*****

    @classmethod
    def adjoint(cls, mat):
        pass

    @classmethod
    def inverse(cls, mat):
        pass


if __name__ == "__main__":

    # declare a matrix in the form of [[row 1],[row 2],[row 3]]
    # m = number of rows, n = number of rows.
    # Accept values of x and y e.g 
    # Enter the order of the matrix in this format => rows coloumn: 2 3
    try:
        order = input("Enter the order of the matrix in this format => rows coloumn:")
        order_list = order.split()
        n = int(order_list.pop())
        m = int(order_list.pop())
    except:
        print("Improper input!")
        exit()

    if(len(order_list) != 0):
        print("Improper Input!")
        exit()
    matrix1 = Matrix(m,n)
    pass