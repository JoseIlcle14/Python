vetor=[]
maior = 0
menor = 0
soma = 0
media = 0
pares = []
cont = 0

for i in range(0,10):
    n = int(input("Digite um número: "))
    vetor.append(n)
    soma = soma+vetor[i]
    media = soma/10
    if i == 0:
        maior = vetor[i]
        menor = vetor[i]
    if vetor[i]>maior:
        maior = vetor[i]
    if vetor[i]< menor:
        menor = vetor[i]
for i in range(0,10):
    if vetor[i]%2==0:
        pares.append(vetor[i])
    
    if vetor[i] > media:
       cont = cont+1
print(vetor)
print("Pares ",pares)
print(f"Maior:{maior} e Menor:{menor}")
print("Maiores que a media: ",cont)
print("Média: ",media)