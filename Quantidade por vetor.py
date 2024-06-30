vetor= []
somaA = 0
somaB = 0
somaC = 0
#entrada de dados
for i in range(0,10):
    n = int(input("Digite um número: "))
    vetor.append(n)

a = int(input("digite o valor A: "))
b = int(input("digite o valor B: "))
c = int(input("digite o valor C: "))

#comparação dos dados coletados
for i in range(0,10):
    if vetor[i] == a:
        somaA = somaA+1
    if vetor[i] == b:
        somaB = somaB+1
    if vetor[i] == c:
        somaC = somaC+1
print(vetor)
#informará  quantas vezes um número X apareceu no vetor
print(f"Números em A:{somaA} em B:{somaB} em C:{somaC}")