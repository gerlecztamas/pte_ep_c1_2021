"""
def megtalal():
    szoveg=input("Adjon meg egy szöveget!")
    k=input("Adja meg a keresett karaktert! ")
    x=0
    for a in szoveg:
        x+=1
        if a==k:
            return x
        else:
            return -1
print(megtalal())
"""

def megtalal(karakter: str, szoveg: str)->int:
    pozicio = -1
    i=0
    while pozicio==-1 and i < len(szoveg):
    #for i in range(len(szoveg)):
        if szoveg[i]==karakter and pozicio==-1:
            pozicio=i
        i+=1
    return pozicio

def kacsanevek(prefixes='JKLMNOPQ', suffix= 'ack') ->list[str]:
    nevek=[]
    for kezdo_betu in prefixes:
        nevek.append(kezdo_betu+suffix)
    return nevek

print(megtalal("a","Indul a pap aludni"))
print("Indul a pap aludni".find("a"))
print(kacsanevek())