jezyki = ['Python', 'Java', 'C#', 'Ruby']

print("Odwrócona lista #1")
print(jezyki[::-1])
print("Odwrócona lista #2")
print(list(reversed(jezyki))) #zwraca iterator nie listę!
print("Odwrócona lista #3")
temp = jezyki.copy()
for i in range(len(temp)-1):
    temp.insert(i,temp[len(temp)-1])
    temp.pop()
print(temp)
print("Odwrócona lista #4")
jezyki.reverse()
print(jezyki)
