import numpy as np

def qr(A):
    m = A.shape[0]
    Q = np.eye(m)
    for i in range(m - 1):
        H = np.eye(m)
        #calculate Householder matrix i: rows and i: columns from A i: rows and ith column
        H[i:, i:] = make_householder(A[i:, i])
        Q = Q@H
        A = H@A
    return Q, A

def norm(a):
    rs = 0
    for i in range(len(a)):
        rs += np.sum(a[i]**2)
    return np.sqrt(rs)
 
def make_householder(a):
    #find prependicular vector to mirror
    u = a / (a[0] + np.copysign(norm(a), a[0]))
    u[0] = 1
    # Tạo ma trận đơn vị với kích thước là mxm
    H = np.eye(a.shape[0])
    #finding Householder projection
    H -= (2 / np.dot(u, u)) * u[:, None] @ u[None, :]
    return H

def find_eig_qr(A):
    pQ = np.eye(A.shape[0])
    X = A.copy()
    # cải thiện độ chính xác với số epoch là 100
    for i in range(100):
            Q,R = qr(X)
            pQ = pQ @ Q;
            X = R @ Q;
    return np.diag(X), pQ

m = int(input("Enter size of matrix: "))

matrix = []
for i in range(0,m):
    print("Enter row", i + 1, ":")
    temp = [int(input()) for j in range(0,m)]
    matrix.append(temp) 
    
print("----------------Input--------------------")
for i in range(m):
    print(matrix[i])
    
A = np.asarray(matrix, dtype='float')

Q, R = qr(A)
eigenvalues, eigenvectors = find_eig_qr(A)

print("---------------Output--------------------")
print("\nEigenvectors V:\n  v1       v2       v3\n", eigenvectors.round(3))
print("\nEigenvalues diag(lamda): \n  lamda1 lamda2 lamda3 \n", eigenvalues.round(3))
print("\nInverse Eigenvectors V-1:\n", np.linalg.inv(eigenvectors))
'''
 V-1 dùng thư viện numpy vì mục đích chính bài này là tìm vecto riêng (eigenvectors) 
 và giá trị riêng (eigenvalues). Bài tính ma trận nghịch đảo có gửi đính kèm.
'''