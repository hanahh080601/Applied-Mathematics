# BT1: viết chương trình tính a^m mod n (xét m = 0, chẵn, lẻ)

a, m, n = list(map(int, input("Enter a, m, n split by ' ': ").split()))
print(a, m, n)

def Mod(a, m, n):
    if (m == 0):
        return 1
    elif (m % 2 == 0):
        y = Mod(a, m/2, n)
        return (y * y) % n
    else:
        return ((a%n) * Mod(a, m-1, n)) % n
print(Mod(a,m,n))