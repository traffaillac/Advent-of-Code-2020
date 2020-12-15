# https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_des_restes_chinois#Algorithme
from functools import reduce

T = int(input())
#wait, ID = min(((-T)%int(ID), int(ID)) for ID in input().split(',') if ID!='x')
#print(wait*ID)
buses = [(a, int(n)) for a, n in enumerate(input().split(',')) if n!='x']
N = reduce(lambda n, b: n*b[1], buses, 1)
print(sum(N//n * pow(N//n, -1, n) * -a for a, n in buses) % N)
