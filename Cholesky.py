import numpy as np

def InputMatrix():
    m = int(input("Enter size of matrix: "))

    matrix = []
    for i in range(0,m):
        print("Enter row", i + 1, ":")
        temp = [float(input()) for j in range(0,m)]
        matrix.append(temp) 
    
    print("\nInput matrix:")
    for i in range(m):
        print(matrix[i])
    return matrix

def Check(a):
    a = np.array(a, float)
    # Check trị riêng không âm
    eig_values = np.linalg.eig(matrix)[0]
    for i in range(len(eig_values)):
        if(eig_values[i] < 0):
            return False
    # Check ma trận đối xứng
    for i in range(len(a)):
        for j in range(len(a)):
            if(j == i):
                continue
            if(a[i,j] != a[j,i]):
                return False
    return True

def Cholesky(a):
    a = np.array(a, float)
    L = np.zeros_like(a)
    n,_ = np.shape(a)
    for i in range(n):
        for j in range(i, n):
            if(j == i):
                L[j,i] = np.sqrt(a[j,i] - np.sum(L[j, :i]**2))
            else:
                L[j,i] = (a[j,i] - np.sum(L[j, :i] * L[i, :i])) / L[i,i]
    return L

matrix = InputMatrix()
if(Check(matrix)):    
    L = Cholesky(matrix)
    print("\nOutput - Matrix L:\n", L)
else:
    print("Ma tran A khong the phan ra theo phuong phap Cholesky!")
