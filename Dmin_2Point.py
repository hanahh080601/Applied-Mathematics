import math
import copy
 
# Lớp biểu diễn cho 1 điểm trên hệ Oxy 
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
# Hàm tính khoảng cách giữa 2 điểm
def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) *(p1.x - p2.x) +(p1.y - p2.y) *(p1.y - p2.y))
 
# Trả về giá trị khoảng cách nhỏ nhất giữa 2 điểm trong mảng P kích thước n 
def bruteForce(P, n):
    # khởi tạo min_val gần như dương vô cùng
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if distance(P[i], P[j]) < min_val:
                min_val = distance(P[i], P[j])
                pair = P[i], P[j]
    return min_val, pair
 
    
# Tìm khoảng cách gần nhất giữa 2 điểm trong dải strip và được sắp xếp theo trục y, có giới hạn trên
# là 1 khoảng d. Độ phức tạp sẽ là O(n) vì vòng lặp ở trong chỉ chạy nhiều nhất là 6 lần.
def stripClosest(strip, size, d):
    min_val = d
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y - strip[i].y) < min_val:
            min_val = distance(strip[i], strip[j])
            pair = strip[i], strip[j]
            j += 1
 
    return min_val, pair
 
# Hàm đệ quy tìm khoảng cách nhỏ nhất. Các phần tử trong P sắp xếp theo trục x
def closestUtil(P, Q, n):
    if n <= 3:
        return bruteForce(P, n)
 
    mid = n // 2
    midPoint = P[mid]
    P_left = P[:mid]
    P_right = P[mid:]
    
    dl = closestUtil(P_left, Q, mid)
    dr = closestUtil(P_right, Q, n - mid)
    d = min(dl, dr)
    
    stripP = []
    stripQ = []
    lr = P_left + P_right
    
    for i in range(n):
        if abs(lr[i].x - midPoint.x) < d:
            stripP.append(lr[i])
        if abs(Q[i].x - midPoint.x) < d:
            stripQ.append(Q[i])
 
    # Sắp xếp các điểm theo giá trị trên trục y
    stripP.sort(key=lambda point: point.y)
    min_a = min(d, stripClosest(stripP, len(stripP), d)[0])
    min_b = min(d, stripClosest(stripQ, len(stripQ), d)[0])
    return min(min_a, min_b)
 
# Hàm main để chạy:
def closest(P, n):
    # Sắp xếp các điểm theo giá trị trên trục x
    P.sort(key=lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key=lambda point: point.y)
    return closestUtil(P, Q, n)

if __name__ == '__main__':
    P = []
    n = int(input("Nhap so diem n:"))
    for i in range(n):
        print("Diem thu", i + 1, ":")
        t1 = float(input())
        t2 = float(input())
        P.append(Point(t1, t2))

    print("Khoang cach nho nhat la:",
          closest(P, n))