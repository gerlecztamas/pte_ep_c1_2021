def rendzes(lista: list[int])->list[int]:
    rendzett_lista = lista.copy()
    for i in range(1, len(lista)):
        for j in range(len(lista)-i):
            if rendzett_lista[j] > rendzett_lista[j+1]:
                seged=rendzett_lista[j]
                rendzett_lista[j]=rendzett_lista[j+1]
                rendzett_lista[j+1]=seged
    return rendzett_lista


def minimum(lista: list[int],hanyadik=0) ->int:
    return rendzes(lista)[hanyadik]


def osszeg(lista: list[int])->int:
    osszeg=0
    for elem in lista:
        osszeg+=elem
    return osszeg

def atlag(lista: list[int])->float:
    return osszeg(lista)/len(lista)








lista=[42,12,76,23,51,23,36]
print(lista)
print(rendzes(lista))