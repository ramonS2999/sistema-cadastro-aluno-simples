from Aluno import Aluno
vetor = []
matriculaTam = 0

def abrir():
	global matriculaTam
	arquivo = open("banco.txt", 'r+')
	v = arquivo.readlines()
	i=0
	while i<len(v):
		a = Aluno(int(v[i].rstrip("\n")),v[i+1].rstrip("\n"),float(v[i+2].rstrip("\n")), float(v[i+3].rstrip("\n")), float(v[i+4].rstrip("\n")), v[i+5].rstrip("\n"))
		if matriculaTam<a.matricula:
			matriculaTam = a.matricula
		vetor.append(a)
		i+=6
	arquivo.close()

def gravar():
	arquivo = open("banco.txt", 'w')
	arquivo.writelines("")
	for v in vetor:
		arquivo.write(str(v.matricula)+"\n")
		arquivo.write(v.nome+"\n")
		arquivo.write(str(v.nota1)+"\n")
		arquivo.write(str(v.nota2)+"\n")
		arquivo.write(str(v.media)+"\n")
		arquivo.write(v.resultado+"\n")
	arquivo.close()
def inserir():
	global matriculaTam
	nome = input("Digite o nome:").title()
	nota1 = float(input("Digite nota 1:"))
	nota2 = float(input("Digite nota 2:"))
	media = (nota1+nota2)/2
	if media>=7:
		resultado = "aprovado"
	elif media>=4:
		resultado = "exame final"
	else:
		resultado = "reprovado"
	matriculaTam= matriculaTam+1
	a = Aluno(matriculaTam, nome, nota1, nota2,media, resultado)
	vetor.append(a)
	print("Salvo com sucesso\n")

def alterar():
	mat = int(input('digite a matricua do auno: '))
	for v in vetor:
		if v.matricula == mat:
			v.nome = input("Digite o novo nome:").title()
			v.nota1 = float(input("Digite nota 1:"))
			v.nota2 = float(input("Digite nota 2:"))
			v.media = (v.nota1+v.nota2)/2
			if v.media>=7:
				v.resultado = "aprovado"
			elif v.media>=4:
				v.resultado = "exame final"
			else:
				v.resultado = "reprovado"
	print("Alterado com sucesso\n")

def excluir():
	opc = int(input('informe a matricula do aluno: '))
	nome = ""
	for v in vetor:
		if v.matricula == opc:
			vetor.remove(v)
			nome = v.nome
	print(f'{nome.upper()} foi Excluido com sucesso\n')

def pesquisar():
	opc = int(input('digite a matricula do aluno: '))
	for v in vetor:
		if v.matricula == opc:
			print(f""
				  f"Matricula: {v.matricula}\n"
				  f"Aluno: {v.nome}\n"
				  f"Nota 1: {v.nota1}\n"
				  f"Nota 2: {v.nota2}\n"
				  f"Media: {v.media}\n"
				  f"Status: {v.resultado}\n"
				  f"")

def mediaTurma():
	mediaTurma = 0
	cont = 0
	for v in vetor:
		if v.media == v.media:
			mediaTurma = mediaTurma + v.media
			cont = cont + 1
	mediaTurma= (mediaTurma)/cont
	print('Media da Turma: {:.2f}\n'.format(mediaTurma))

def listar():
	for v in vetor:
		print(f""
			  f"Matricula: {v.matricula}\n"
			  f"Nome: {v.nome}\n"
			  f"Nota 1: {v.nota1}\n"
			  f"Nota 2: {v.nota2}\n"
			  f"Media: {v.media}\n"
			  f"Statos: {v.resultado}\n"
			  f"")

def menu():
	op = 0
	abrir()
	while op != 7:
		op = int(input(""
					   "1-inserir \n"
					   "2-listar \n"
					   "3-alterar \n"
					   "4-Remover \n"
					   "5-Pesquisar \n"
					   "6-Media da Turma \n"
					   "7-sair "
					   "Digite uma opcao:\n"
					   ""))

		if op == 1:
				inserir()
		elif op == 2:
				listar()
		elif op == 3:
				alterar()
		elif op == 4:
				excluir()
		elif op == 5:
				pesquisar()
		elif op == 6:
				mediaTurma()
		elif op != 7:
				print("opcao invalida\n")
	gravar()

menu()











