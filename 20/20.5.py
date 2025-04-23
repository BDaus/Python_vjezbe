def izracunaj_prosjek(lista):
    zbroj=0
    for broj in lista:
        zbroj+=broj
    
    if len(lista) > 0:
        prosjek=zbroj/len(lista)
        return prosjek
    else:
        return 0
print(izracunaj_prosjek([1, 2, 3, 4, 5]))
