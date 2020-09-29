class Pies:
    def __init__(self, imie = "Test", wiek = 14):
        self.imie = imie
        self.wiek = wiek
    def __str__(self):
        return " : ".join((self.imie, str(self.wiek)))
    def prt(self):
        print(self.imie, self.wiek)

dog1 = Pies("Burek", 15)
dog2 = Pies()
dog3 = Pies()
dog1.prt()
dog2.prt()
dog3.prt()
print(dog1.__str__())
print(True if dog2 is dog3 else False)