import math
import numpy as np
'''
c = [1, 1, 0, 0, 0]
A = [
    [-1, 1, 1, 0, 0],
    [ 1, 0, 0, 1, 0],
    [ 0, 1, 0, 0, 1]
]
b = [2, 4, 4]

c = [5, 8, 0, 0]
b = [1, 2]
A=[[1, 2, 1, 0], [1, 1, 0, 1]]
'''
c = [-2, -3, 1, 1, 0, 0]
b = [10, 8, 20]
A = [[1, -1, 1, 0.5, 0, 0], [0, 1, -4, 8, 1, 0], [0, -2, 2, 3, 0, 1]]

# Hàm đơn hình
def simplex(c, A, b):
    tableau = to_tableau(c, A, b)
    while can_be_improved(tableau):
        pivot_position = get_pivot_position(tableau)
        print("aaa:", pivot_position)
        tableau = pivot_step(tableau, pivot_position)
        print("bbb", tableau)
    return get_solution(tableau)

# Chuyển c, A, b thành tableau
def to_tableau(c, A, b):
    xb = [eq + [x] for eq, x in zip(A, b)]
    print("xb: ", xb);
    z = c + [0]
    print("z: ", z)
    print("xb + [z]: ", xb + [z])
    return xb + [z]

# Kiểm tra hàng z có phần tử nào lớn hơn 0 nữa hay không (còn có thể improved)
def can_be_improved(tableau):
    z = tableau[-1]
    return any(x > 0 for x in z[:-1])

# Trả về chỉ số hàng, cột của Xi có hệ số 1
def get_pivot_position(tableau):
    # Lấy chỉ số cột mà có giá trị của z lớn hơn 0 (theo chiều ngược lại)
    z = tableau[-1]
    print("z: ", z)
    column = next(i for i, x in enumerate(z[:-1]) if x > 0)
    print("comlumn: ", column)
    print("tableau[:-1]: ", tableau[:-1])
    
    # Lấy giá trị của cột thứ column
    restrictions = []
    for eq in tableau[:-1]:
        el = eq[column]
        print("el: ", el)
        restrictions.append(math.inf if el <= 0 else eq[-1] / el)
    print("restrictions: ", restrictions)

    # Lấy chỉ số của phần tử có giá trị nhỏ nhất trong restrictions
    row = restrictions.index(min(restrictions))
    print("row: ", row)
    return row, column

# Chuyển cột và tạo tableau mới
def pivot_step(tableau, pivot_position):
    new_tableau = [[] for eq in tableau]
    
    i, j = pivot_position
    pivot_value = tableau[i][j]
    new_tableau[i] = np.array(tableau[i]) / pivot_value
    print(new_tableau[i])
    
    for eq_i, eq in enumerate(tableau):
        if eq_i != i:
            multiplier = np.array(new_tableau[i]) * tableau[eq_i][j]
            print("multiplier: ", multiplier)
            new_tableau[eq_i] = np.array(tableau[eq_i]) - multiplier
   
    return new_tableau

# Kiểm tra các cột có đúng 1 giá trị = 1, các giá trị còn lại = 0
def is_basic(column):
    return sum(column) == 1 and len([c for c in column if c == 0]) == len(column) - 1

# Lấy kết quả
def get_solution(tableau):
    columns = np.array(tableau).T
    solutions = []
    for column in columns[:-1]:
        solution = 0
        if is_basic(column):
            one_index = column.tolist().index(1)
            solution = columns[-1][one_index]
        solutions.append(solution)
    return solutions

solution = simplex(c, A, b)
print('Solution: ', solution)