def ordenacao_selecao(lista):
    n = len(lista)
    for i in range(n - 1):
        min_index = i
        for j in range(i, + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        if lista[i] > lista[min_index]:
            lista[min_index] = aux


def ordenacao_insercao(lista):
    global chave, i
    n = len(lista)
    for j in range(1, n):
        chave = lista[j]
        i = j - 1
        while i >= 0 and lista[i] > chave:
            lista[i + 1] = lista[i]
        i = i - 1
    lista[i + 1] = chave


def ordenacao_bolha(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]


with open("numeros.txt", "r+") as file:
    arquivo = open("numeros.txt")
    lista = file.read()
    print(lista)

while True:
    print("---------- ORDENAÇÕES ----------")
    print("----------            -----------")
    print("-------------Opções:-------------------")
    print(" 1- Ordenação por Seleção")
    print(" 2- Ordenação por Inserção")
    print(" 3- Ordenação em Bolha")
    print("----------------------------------------")
    opcao = int(input("Digite a opção desejada: "))

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]

    if opcao == 1:
        print("Ordenação por Seleção")
    ordenacao_selecao(lista)
    print("\n", lista)

    if opcao == 2:
        print("Ordenação por Inserção")
    ordenacao_insercao(lista)
    print("\n", lista)

    if opcao == 3:
        print("Ordenação em Bolha")
    ordenacao_bolha(lista)
    print("\n", lista)

# Wallace dos Santos Queiros#
# Eng. Software#
# Matricula: 201810251#
