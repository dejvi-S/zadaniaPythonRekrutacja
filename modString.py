#String jest niemutowalny = niezmienny
a = 'abcdefg'
a = list(a)
a[1] = 'X'
print("".join(a))
