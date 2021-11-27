import datetime
import time

def bekeres() -> str:
    return input("Hogy hívnak?\n")

def koszon(nev="") -> None:
    print(f"szia {nev}")

koszon()
koszon(bekeres())

def pontos_ido():
    print(datetime.datetime.now())


def varakozas(masodperc: int):
    pontos_ido()
    time.sleep(masodperc)
    pontos_ido()
pontos_ido()
varakozas(10)

def get_afa(termek_ara: int,afa=27) -> float:
    return termek_ara*afa/100

def brutto(termek_ara: int, afa=27) -> float:
    return termek_ara+get_afa(termek_ara, afa)
ar=10000
print(get_afa(ar))
print(brutto(ar))