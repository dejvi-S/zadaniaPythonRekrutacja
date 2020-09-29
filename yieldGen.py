def word(w):
    for s in w:
        yield s

w = "testowe"
t = word(w)
for _ in range(len(w)):
    print(next(t))