print("Podaj liczbę elementów n")

for i in range(1,int(input())+1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(str(i))
#Ewentualnie konkatenacja stringa