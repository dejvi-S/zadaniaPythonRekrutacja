x = "myszydokazujągdykotanieczują"
count = dict()

for word in x:
    if word in count:
        count[word] +=1
    else:
        count[word] = 1
print(count)

#dickValues
if 4 in count.values():
    print(True)
else:
    print(False)