vet=[]
n = 101
j = 1
while j <= 10:
    cont = 0
    for i in range(1,n):
        if n%i == 0:
            cont = cont+ 1
    if cont == 2:
        vet.append(n)
        j = j+1
    n = n +1
print(vet)
    

