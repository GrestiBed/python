from math import ceil,floor

pikkus = input("Sisesta pikkus tükkides: ")
laius = input("Sisesta laius tükkides: ")
h = input("Sisesta kõrgus tükkides: ")
tk_pakis = input("Mitu tükki on ühes pakis: ")

def pakke():
    tk_arv = int(pikkus) * int(laius) * int(h)
    pakk_arv = tk_arv / int(tk_pakis)
    #print("Sul on vaja " + str(round(pakk_arv + 0.49)) + " pakki")
    print("Sul on vaja " + str(floor(pakk_arv)) + " pakki")

pakke()
