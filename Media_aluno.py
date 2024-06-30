aluno = [[0]*4]*5

for l in range(5):
    for c in range(3):
        print(f'[{l},{c}]')
        if c == 0:
            aluno[l][c] = int(input('Digite seu número de chamada: '))
        if c == 1:
            aluno[l][c] = int(input('Digite a média das provas: '))
        if c == 2:
            aluno[l][c] = int(input('Digite a média  dos trabalhos: '))

for l in range(5):
    for c in range(4):
        aluno[l][3] = aluno[l][1]+aluno[l][2]
        print(f'[{aluno[l][c]}]', end='')
    print()
#for l in range(5):
 #   for c in range(4):
  #      print(f' [{aluno[l][c]}] ', end='')
   # print()
