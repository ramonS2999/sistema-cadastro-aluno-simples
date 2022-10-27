class Aluno(object):
	def __init__(self,matricula, nome, nota1, nota2, media=0, resultado=""):
		self.matricula = matricula
		self.nome=nome
		self.nota1= nota1
		self.nota2= nota2
		self.media= media
		self.resultado = resultado
