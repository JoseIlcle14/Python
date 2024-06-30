# Crie uma matriz que tenha o valor 1 na sua diagonal principal,
# 2 na sua diagonal secundária e 0 no restante dos lugares.

# principal   # secundária

mat = [[0 for i in range(5)]for i in range(5)]

for l in range(5):
    for c in range(5):
        if c == l:
            mat[l][c] = 1
        if c + l == 4:
            mat[l][c] = 2
        print(f'[{mat[l][c]}]', end='')
    print()