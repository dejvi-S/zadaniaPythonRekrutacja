x = 10
def f():
    global x #używamy globalnej zmiennej zamiast tworzyć lokalną
    x = 111
    y = 12
    print(x, y)
f()
print(x)