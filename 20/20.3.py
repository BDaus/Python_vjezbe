def je_prost(broj):
    if broj<=1:
        return False
    for i in range(2,broj//2):
        if broj % i==0:
            return False
        
