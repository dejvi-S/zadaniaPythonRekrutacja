word = "kajak"

i = 0
bol = True
while i <= len(word) // 2:
    if word[i] != word[-i-1]:
        bol = False
    i+=1
print(bol)