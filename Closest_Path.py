import math

def dist(p1, p2):
    return math.sqrt(((p2[1]-p1[1])**2)+((p2[0]-p1[0])**2))

def closest_brute_force(points):
    if(len(points) == 1):
        return "Program needs at least 2 points!"
    min_dist = float("inf")
    p1 = None
    p2 = None
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            d = dist(points[i], points[j])
            if d < min_dist:
                min_dist = d
                p1 = points[i]
                p2 = points[j]
    return p1, p2, min_dist


def rec(xsorted, ysorted):
    n = len(xsorted)
    if n <= 3:
        return closest_brute_force(xsorted)
    else:
        midpoint = xsorted[n//2]
        xsorted_left = xsorted[:n//2]
        xsorted_right = xsorted[n//2:]
        
        ysorted_left = []
        ysorted_right = []
        
        for point in ysorted:
            ysorted_left.append(point) if (point[0] <= midpoint[0]) else ysorted_right.append(point)
            
        (p1_left, p2_left, delta_left) = rec(xsorted_left, ysorted_left)
        (p1_right, p2_right, delta_right) = rec(xsorted_right, ysorted_right)
        
        (p1, p2, delta) = (p1_left, p2_left, delta_left) if (delta_left < delta_right) else (p1_right, p2_right, delta_right)
        in_band = [point for point in ysorted if midpoint[0]-delta < point[0] < midpoint[0]+delta]
        for i in range(len(in_band)):
            for j in range(i+1, min(i+7, len(in_band))):
                d = dist(in_band[i], in_band[j])
                if d < delta:
                    print(in_band[i], in_band[j])
                    (p1, p2, delta) = (in_band[i], in_band[j], d)
        return p1, p2, delta


def closest(points):
    xsorted = sorted(points, key=lambda point: point[0])
    ysorted = sorted(points, key=lambda point: point[1])
    return rec(xsorted, ysorted)

if __name__ == '__main__':
    P = []
    n = int(input("Nhap so diem n:"))
    for i in range(n):
        print("Diem thu", i + 1, ":")
        t1 = float(input())
        t2 = float(input())
        P.append([t1, t2])

    print("2 diem gan nhat va khoang cach nho nhat :\n",
          closest(P))