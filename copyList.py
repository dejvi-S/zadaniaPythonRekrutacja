A = [1,2,3,4,5]
B = A
C = A[:] # C = list(A) przy użyciu slice
D = A.copy() # copy()
B[0] = 111
print(A, B, C, D)

#referencja danych a nie dokładna kopia