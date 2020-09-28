print("Podaj liste elementow oddzielając spacją: ")
l = list(input().split())

print("Lista unikalnych elementów sposób 1")
print(list(set(l)))

b = list()

for n in l:
    if n not in b:
        b.append(n)

print("Lista unikalnych elementów sposób 2")
print(b)