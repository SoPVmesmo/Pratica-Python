a=["a","e","i","o","u"]
l=input("digite uma letra ")
if l in a:
    print(" a letra é vogal")
else:
    print("a letra é consoante")

n=[]
while len(n) != 4:
    f=int(input("Digite um numero: "))
    n.append(f)
n.sort()
n.reverse()
print(n)