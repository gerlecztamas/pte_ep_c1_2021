class Kutya:
    def __init__(self,nev:str,fajta:str):
        self.nev=nev
        self.fajta=fajta
    def __str__(self):
        return "a {} nevű kutya {} fajtaju".format(self.nev, self.fajta)

kutya1=Kutya("Lajos","okos")
kutya2=Kutya("Fity","rossz")
print(kutya1)
print(kutya2)