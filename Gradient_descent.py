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

def gradient_descent(X, y, iteration=10000, lr=0.001):
    n = X.shape[1]
    weights = np.zeros(n)
    bias = 0
    
    for i in range(iteration):
        y_pred = np.dot(X, weights) + bias
        cost = 1/n * np.sum([val**2 for val in (y_pred - y)])
        if cost < lr:
            break
        dw = 1/n * np.dot(X.T, (y_pred - y))
        db = 1/n *  np.sum(y_pred - y)
        weights -= dw * lr
        bias -= db * lr
        print("\n Epoch: {},\n Weight: {},\n Bias: {},\n Cost: {}"
              .format(i, weights, bias, cost))

if __name__ == '__main__':
    # ví dụ: Hàm 4 biến với 5 giá trị mẫu để chạy thử
    X = np.array([[1,2,3,4], [0,2,4,6], [1,3,5,7], [5,10,15,20], [2,4,6,8]])
    y = np.array([15,20,25,75,100])
    #X = InputMatrix() # X có số hàng là m, số cột là n
    #y = InputMatrix() # y có số hàng là m, số cột là 1
    gradient_descent(X, y)
    