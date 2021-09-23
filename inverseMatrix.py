from copy import deepcopy
m = int(input("Enter size of matrix: "))

matrix = []
for i in range(0,m):
    print("Enter row", i + 1, ":")
    temp = [int(input()) for j in range(0,m)]
    matrix.append(temp) 
    
print("Original matrix:")
for i in range(m):
    print(matrix[i])

def smaller_matrix(a, row, col):
    a_copy = deepcopy(a)
    a_copy.remove(a[row])
    for i in range(len(a_copy)):
        a_copy[i].remove(a_copy[i][col])
    return a_copy
    
def det(a):
    num_rows = len(a)
    if(num_rows == 1):
        return a[0][0]
    if(num_rows == 2):
        simple_det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
        return simple_det
    else:
        ans = 0
        for j in range(len(a)):
            cofactor = (-1) ** (0+j) * a[0][j] * det(smaller_matrix(a, 0, j))
            ans += cofactor
        return ans
            
def algeComplement(a, row, col):
    if ((row + col) % 2 == 0):
        return det(smaller_matrix(a, row, col))
    return -det(smaller_matrix(a, row, col))

def inverse(a):
    if (det(a) == 0):
        return "Invalid value!"
    else:
        b = deepcopy(a)
        for i in range(len(a)):
            for j in range(len(a)):
                b[i][j] = algeComplement(a,i,j) / det(a)
        for i in range(len(a)):
            for j in range(len(a)):
                temp = b[i][j]
                b[i][j] = b[j][i]
                b[j][i] = temp
        return b

print("Inverse matrix: ")
for i in range(len(matrix)):
    print(inverse(matrix)[i])
        