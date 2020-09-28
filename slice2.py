def check(word):
    if word[0:6] == "python" and word[-3:] == ".py":
        return True
    return False


a = "python_moj_kod.py"
b = "python_notatki.txt"


print(check(a))
print(check(b))