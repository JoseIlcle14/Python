vet = [0]*10
vet2 = [0]*10
n = 10
for i in range(0,10):
    vet[i]= int(input("Digite um numero: "))

for i in range(0,10):
    n = n-1
    vet2[i] = vet[n]

print(vet)
print(vet2)