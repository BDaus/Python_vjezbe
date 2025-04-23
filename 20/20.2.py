def broj_rijeci(recenica):
    broj=1
    for slovo in recenica:
        if slovo == ' ':
            broj+=1
    return broj
broj=broj_rijeci('Python je bas bezveze samo nesto da pise.')
print(broj)
