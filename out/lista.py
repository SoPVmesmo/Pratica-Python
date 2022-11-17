import os
from glob import glob
"""
lista=[1,2,3,4]
nova=[x*x for x in lista]
print(nova)


lista02=[2,3,6,7,8,9,10,11]
nova02=[str(y) for y in lista02 if(y%2==0)]
print(nova02)


texto='eu não sei oque to fazendo aq'.split()#deixa as pavavras juntas
nova03=[(p.upper(), len(p))for p in texto]
print(nova03)


texto="eu não sei oque to fazendo aqui".split()
nova=[]
for i in texto:
    nova.append ((i.upper(),len(i)))
print(nova)
"""
file=[f for f in glob('*.py')]
print(file)