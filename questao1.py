from math import ceil

def calcSeculo(ano):
    return int(ceil(ano/100.0))

ano = int(input())
print(calcSeculo(ano))