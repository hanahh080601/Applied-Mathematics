def ComputeGCD(a,b):
    if (b==0):
        return a
    else:
        return ComputeGCD(b, a%b)
n1 = int(input())
n2 = int(input())
print(ComputeGCD(n1,n2))