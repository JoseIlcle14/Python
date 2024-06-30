funcionarios = []
comissao = []
vendas = []
valor = []
func_maior = []
func_menor = []
maior = 0
menor = 0
pessoas =  2

for i in range(0,pessoas):
    n = str(input("Nome do funcionario: "))
    funcionarios.append(n)
for i in range(0,pessoas):
    v = int(input("Informe o valor de vendas de "+funcionarios[i]+" : "))
    vendas.append(v)
for i in range(0,pessoas):
    c = int(input("Informe a comissão de "+funcionarios[i]+" (%): "))
    comissao.append(c)
for i in range(0,pessoas):
    valor.append(i)
    valor[i]= vendas[i]*comissao[i]/100

for i in range(0,pessoas):
    maior = vendas[1]
    menor = vendas[1]
    if vendas[i] > maior:
        maior = vendas[i]
        func_maior = funcionarios[i]
    if vendas[i] < menor:
        menor = vendas[i]
        func_menor = funcionarios[i]

print("--"*30)

print("Melhor vendedor: ",func_maior,"|| Valor da venda R$: ",maior)
print("Pior vendedor: ",func_menor,"|| Valor da venda R$: ",menor)

    