try:
    with open("test.txt", 'w') as f:
        for x in range(100):
            f.write(str(x+1))
            f.write(' ')
except:
    print("Excepetion rised")

try:
    l = []
    with open("test.txt", 'r') as f:
        l = f.readlines()
        l = l[0].split()
        print(l)
except:
    print("Exception rised")