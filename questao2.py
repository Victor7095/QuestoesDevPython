from math import ceil

def isPrimo(n):
    if n in [0, 1]: return False
    cont = 2
    while cont < n:
        if n % cont == 0: return False
        cont += 1
    return True
    

def somatorioPrimos(n):
    if n <= 0: return 0
    contPrimos = 0
    acm = 0
    numAtual = 1
    while contPrimos < n:
        if isPrimo(numAtual):
            acm+=numAtual
            contPrimos+=1
        numAtual+=1
    return acm

n = int(input())
print(somatorioPrimos(n))