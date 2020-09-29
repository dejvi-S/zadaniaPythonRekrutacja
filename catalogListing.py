import os
path = r"C:\Users\Dawid\Desktop\PythonAutomation\zadaniaRekrutacyjne"
def catalogList(path):
    l = os.listdir(path)
    for item in l:
        if os.path.isdir(os.path.join(path, item)):
            print(item)
            catalogList(os.path.join(path, item))
        else:
            print(item)
    

catalogList(path)
