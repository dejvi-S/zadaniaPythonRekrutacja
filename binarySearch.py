P = [-10, -7, -5, -3, 0, 3, 5, 21, 68, 341, 500]

def binSearch(P, key):
    temp = len(P)//2
    if len(P) == 1:
        return temp if P[temp] == key else None
    elif P[temp] == key:
        return temp
    else:
        if P[temp] < key:
            callback = binSearch((P[temp:]), key)
            return temp + callback if callback is not None else None
        else:
            return binSearch((P[:temp]), key)
P.sort()
print(P)
print(binSearch(P, 21))
print(binSearch(P, -10))
print(binSearch(P, 3))
print(binSearch(P, 211))