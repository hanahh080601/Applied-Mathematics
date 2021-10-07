import numpy as np

def InputMatrix():
    m = int(input("Enter rows number of matrix: "))
    n = int(input("Enter columns number of matrix: "))

    matrix = []
    for i in range(0,m):
        print("Enter row", i + 1, ":")
        temp = [float(input()) for j in range(0,n)]
        matrix.append(temp) 
    
    print("\nInput matrix:")
    for i in range(m):
        print(matrix[i])
    return np.asarray(matrix, dtype='float64')

def eigenvalue(A, v):
    val = A @ v / v
    return val[0]

def svd_dominant_eigen(A, epsilon=0.01):
    """returns dominant eigenvalue and dominant eigenvector of matrix A"""
    n, m = A.shape
    k=min(n,m)
    v = np.ones(k) / np.sqrt(k)
    if n > m:
        A = A.T @ A
    elif n < m:
        A = A @ A.T
    
    ev = eigenvalue(A, v)

    while True:
        Av = A @ v
        v_new = Av / np.linalg.norm(Av)
        ev_new = eigenvalue(A, v_new)
        if np.abs(ev - ev_new) < epsilon:
            break

        v = v_new
        ev = ev_new

    return ev_new, v_new

def svd(A, k=None, epsilon=1e-10):
    """returns k dominant eigenvalues and eigenvectors of matrix A"""
    A = np.array(A, dtype=float)
    n, m = A.shape
        
    svd_so_far = []
    if k is None:
        k = min(n, m)

    for i in range(k):
        matrix_for_1d = A.copy()

        for singular_value, u, v in svd_so_far[:i]:
            matrix_for_1d -= singular_value * np.outer(u, v)

        if n > m:
            _, v = svd_dominant_eigen(matrix_for_1d, epsilon=epsilon)  # next singular vector
            u_unnormalized = A @ v
            sigma = np.linalg.norm(u_unnormalized)  # next singular value
            u = u_unnormalized / sigma
        else:
            _, u = svd_dominant_eigen(matrix_for_1d, epsilon=epsilon)  # next singular vector
            v_unnormalized = A.T @ u
            sigma = np.linalg.norm(v_unnormalized)  # next singular value
            v = v_unnormalized / sigma

        svd_so_far.append((sigma, u, v))

    singular_values, us, vs = [np.array(x) for x in zip(*svd_so_far)]
    return singular_values, us.T, vs

if __name__== "__main__":
    matrix = InputMatrix()
    print(matrix.shape)
    singular_values,_,V = svd(matrix, min(matrix.shape))
    n0, U_T, n1 = svd(matrix, max(matrix.shape))
    print("\nSingular values:\n", singular_values)
    print("\nVector U.T:\n", U_T)
    print("\nVector V:\n", V)