def fibrek(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibrek(n-1) + fibrek(n-2)

def fibIter(n):
    a = 0
    b = 1
    if n==0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(2,n+1):
            temp = b
            b += a
            a = temp
        return b
print(fibrek(10))
print(fibIter(10))