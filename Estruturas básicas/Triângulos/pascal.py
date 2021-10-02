# Variáveis:
# first- 1a linha *n sei se é necessário, veremos
# last- última linha (n)
# first_row- lista da 1a linha
# last_row-lista da última linha
# row- variável de lista

def pascal_triangle(frist, last):
    row = [1]
    y = []
    for x in range(last + 1):
        y.append(row)
        row = getnextrow(row)  # new row
    printtriangle(y, frist, last)


def getnextrow(curr_row):
    nextrow = list(map(sum, zip([0] + curr_row, curr_row + [0])))
    return nextrow


def printtriangle(y, frist, last):
    last_line = y[-1]
    lenmax = len(
        ' '.join(map(str, last_line)))  # transforma uma lista de inteiros numa string e calcula número de caracteres
    for i in range(frist, last + 1):
        print(' '.join(map(str, y[i])).center(lenmax))


pascal_triangle(0, 10)

