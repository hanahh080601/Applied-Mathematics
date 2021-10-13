
# Lớp biểu diễn cho 1 điểm trên hệ Oxy 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
def Left_index(points):
     
    minn = 0
    for i in range(1,len(points)):
        if points[i].x < points[minn].x:
            minn = i
        elif points[i].x == points[minn].x:
            if points[i].y > points[minn].y:
                minn = i
    return minn
 
def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - \
          (q.x - p.x) * (r.y - q.y)
 
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2
 
def convexHull(points, n):
     
    if n < 3:
        return
 
    # Tìm điểm trái nhất
    l = Left_index(points)
 
    hull = []
     
    p = l
    q = 0
    while(True):
         
        # Thêm p hiện tại vào hull
        hull.append(p)
        q = (p + 1) % n
 
        for i in range(n):
            # nếu i ngược chiều so với q thì gán q = i
            if(orientation(points[p],
                           points[i], points[q]) == 2):
                q = i
        p = q
        if(p == l):
            break
 
    # In kết quả
    i = 1
    print("Cac diem bao loi la:")
    for each in hull:
        print("Diem", i, ": (", points[each].x, ",", points[each].y, ")")
        i += 1
 
if __name__ == '__main__':
    P = []
    n = int(input("Nhap so diem n:"))
    for i in range(n):
        print("Diem thu", i + 1, ":")
        t1 = float(input())
        t2 = float(input())
        P.append(Point(t1, t2))
    convexHull(P, len(P))