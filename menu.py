import tkinter.messagebox

dicionario = {}
matriculaTam = 0

def abrir():
	global matriculaTam
	with open("banco.txt", 'r+') as arquivo:
		arquivo_linha = arquivo.readlines()

		i=0
		while i < len(arquivo_linha):
			dicionario[int(arquivo_linha[i].strip())] = \
				[
					str(arquivo_linha[i+1].strip().title()),
					float(arquivo_linha[i+2].strip()),
					float(arquivo_linha[i+3].strip()),
					float(arquivo_linha[i+4].strip()),
					str(arquivo_linha[i+5].strip().title())
				]

			if matriculaTam < int(arquivo_linha[i].strip()):
				matriculaTam = int(arquivo_linha[i].strip())

			i += 6


def gravar():
	try:
		with open("banco.txt", 'w') as arquivo:
			arquivo.writelines("")
			for key, value in dicionario.items():
				arquivo.write(str(key)+"\n")
				arquivo.write(str(value[0])+"\n")
				arquivo.write(str(value[1])+"\n")
				arquivo.write(str(value[2])+"\n")
				arquivo.write(str(value[3])+"\n")
				arquivo.write(value[4]+"\n")
	except:
		print("Erro, não foi possível gravar!")
	else:
		print("Salvo com Sucesso!")


def verifica_notas(nota1: float or int, nota2: float or int ) -> bool:
	if  (0 <= nota1 <= 10) and (0 <= nota2 <= 10):
		return  True
	else:
		return False

def inserir(tx_nome, tx_nota1, tx_nota2):
	"""Função que inseri o cadastro do aluno no banco de dados."""

	# Abrindo o arquivo onde estão so dados e, tranzendo a variável global.
	abrir()
	global matriculaTam

	nome = tx_nome.get()
	nota1 = tx_nota1.get()
	nota2 = tx_nota2.get()

	# Verificando se os dados invformados são válidos.
	try:
		nome = str(nome)
		nota1 = float(nota1)
		nota2 = float(nota2)
	except:
		msg = f"Dados inválidos.\n" \
			  f"Não foi possível cadastar!\n\n" \
			  f"Nome: {tx_nome}.\n" \
			  f"Nota1: {tx_nota1}\n" \
			  f"Nota2: {tx_nota2}\n\n" \
			  f"Verifica os campos e tente novamente."
		tkinter.messagebox.askokcancel(title='Erro de cadastro', message=msg)
		return 0
	else:
		if verifica_notas(float(nota1), float(nota2)):
			# Calculando a média do aluno
			nota1 = retorna_duas_casa_decimais(nota1)
			nota2 = retorna_duas_casa_decimais(nota2)
			media = (nota1 + nota2) / 2
			media = retorna_duas_casa_decimais(media)

			# Verificando o estado do aluno.
			if media >= 7:
				resultado = "aprovado"
			elif media >= 4:
				resultado = "exame final"
			else:
				resultado = "reprovado"

			# Adicionando mais 1 a matrícula, para sempre colocar o último.
			matriculaTam += 1

			# Inserindo aluno ao dicionario que será salva.
			dicionario[matriculaTam] = \
				[
					nome.title(),
					nota1,
					nota2,
					media,
					resultado.title()
				]
			gravar()
			return 1
		else:
			return 400

def retorna_duas_casa_decimais(valor: float or int) -> float:
	auxiliar = f"{valor:.2f}"
	valor = float(auxiliar)
	return valor


def alterar_checar_valor(matricula):
	abrir()
	mat = matricula.get()
	try:
		mat = float(mat)
		mat = int(mat)
	except:
		return 100 # O valor coloca não é inteiro
	else:
		if mat in dicionario.keys():
			return {mat: dicionario[mat]}
		else:
			return 0 # Matricula não encontrada

def alterar(nome_var, nota1_var, nota2_var, aluno_var):
	nome = nome_var.get()
	nota1 = nota1_var.get()
	nota2 = nota2_var.get()

	try:
		aluno = [key for key, valou in aluno_var.items()]
		nota1 = float(nota1)
		nota2 = float(nota2)
	except:
		return 0
	else:
		for key, value in dicionario.items():
			if key == aluno[0]:
				value[0] = nome.title()
				value[1] = nota1
				value[2] = nota2
				value[3] = (value[1] + value[2]) / 2
				if value[3] >= 7:
					value[4] = "aprovado"
				elif value[3] >= 4:
					value[4] = "exame final"
				else:
					value[4] = "reprovado"
				dicionario[key] = [value[0], value[1], value[2], value[3], value[4]]
				print("Alterado com sucesso\n")
				gravar()
				return dicionario[key]


def excluir(matr):
	abrir()

	try:
		int(matr)
	except:
		matricula = matr
	else:
		matricula = int(matr)

	try:
		if type(matricula) is int:
			for key, value in dicionario.items():
				if key == matricula:
					valor = dicionario.pop(key, 0)
					gravar()
					return valor
			if not (matricula in dicionario.keys()):
				gravar()
				print(matricula)
				return matricula
		else:
			gravar()
			return matricula
	except:
		gravar()
		return matricula



def pesquisar(matricula):
	abrir()
	aluno = {}
	try:
		int(matricula.get())
		for key, value in dicionario.items():
			if key == int(matricula.get()):
				aluno[key] = \
					[
						value[0],
						value[1],
						value[2],
						value[3],
						value[4]
					]

			elif not int(matricula.get()) in dicionario:
				aluno = 0
				return aluno
	except:
		return f"Não foi encontrado o aluno referente a matricula: {matricula.get()}"
	else:
		return aluno


def mediaTurma():
	abrir()
	mediaTurma = 0
	cont = 0
	for value in dicionario.values():
		if value[3] == value[3]:
			mediaTurma += value[3]
			cont = cont + 1
	mediaTurma = mediaTurma / cont
	return mediaTurma


def listar():
	abrir()
	sorted(dicionario)
	return dicionario


def sair(janela):
	janela.destroy()
