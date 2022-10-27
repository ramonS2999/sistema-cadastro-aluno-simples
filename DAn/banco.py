import os

lista = []
matricula = 0


def menu():
    os.system("cls")

    print("+------ Menu ------+")
    print("+ 1. Cadastrar     +")
    print("+ 2. Remover       +")
    print("+ 3. Listar        +")
    print("+ 4. Sair          +")
    print("+------------------+")
    op = input("+ Insira uma opção: ")

    return op


def cadastro():
    os.system("cls")
    global lista, matricula

    nome = ""
    media = nota1 = nota2 = 0

    print("+------ Cadastro ------+")
    nome = input("+ Insira o nome: ")
    nota1 = float(input("+ Insira a 1º nota: "))
    nota2 = float(input("+ Insira a 2º nota:"))
    media = (nota1 + nota2) / 2
    if media >= 7:
        resultado = "Aprovado"
    elif media >= 4:
        resultado = "Exame Final"
    else:
        resultado = "Reprovado"

    matricula = matricula + 1
    aux = [matricula, nome, nota1, nota2, media]

    lista.append(aux)


def remover():
    os.system("cls")

    print("+------ Remover ------+")
    mat = float(input("+ Insira a Matricula: "))
    print("+                     +")
    print("+---------------------+")

    for i in range(0, len(lista)):
        if mat == lista[i][0]:
            print("Aluno " + lista[i][1] + " excĺuído!")
            lista.pop(i)
            input("+ 1. Voltar")
            return


def ler():
    global lista, matricula
    aux = []

    try:
        arq = open("dados.txt", "r")
    except:
        print("Arquivo não encontrado!")
        return

    linhas = arq.readlines()
    for linha in linhas:
        linha = linha.split(",")
        linha.pop()

        for dado in linha:
            try:
                dado = float(dado)
                aux.append(dado)
            except:
                aux.append(dado)
        lista.append(aux)
        aux = []

        matricula = lista[-1][0]


def listar():
    os.system("cls")
    print("+------ Todos os Alunos ------+")
    for aluno in lista:
        print("+ " + str(aluno[0]) + " - " + aluno[1])
    print("+-----------------------------+")
    input("1. Voltar: ")


def save():
    linha = ""
    arq = open("dados.txt", "w")

    for aluno in lista:
        for dado in aluno:
            linha += str(dado) + ","
        linha += "\n"
        arq.write(linha)
        linha = ""


def main():
    op = "1"

    while op == "1" or op == "2" or op == "3":
        op = menu()
        if op == "1":
            cadastro()
        elif op == "2":
           remover()
        elif op == "3":
           listar()


ler()
main()
save()
