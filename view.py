from tkinter import *
from configuracao import Configuracao
import menu, scroll

cf = Configuracao()

def inserir_aluno():
    janela_inserir = Toplevel()
    janela_inserir.title("INSERIR ALUNO")
    janela_inserir.geometry("500x500")
    janela_inserir.minsize(500, 500)
    janela_inserir.maxsize(500, 500)

    # Criando as labels
    label_nome = Label(janela_inserir, text="nome")
    label_nome.place(width=100, height=62, x=50 , y=1)

    label_nota_1 = Label(janela_inserir, text="1ª nota")
    label_nota_1.place(width=100, height=62, x=50, y=64)

    label_nota_2 = Label(janela_inserir, text="2ª nota")
    label_nota_2.place(width=100, height=62, x=50, y=113)

    # Variáveis para armazenar os dados solicitados
    nome = StringVar()
    nota1 = StringVar()
    nota2 = StringVar()

    # Criando as caixas de entrada de texto
    tx_nome = Entry(janela_inserir, justify="center", textvariable=nome, borderwidth=5, relief='ridge')
    tx_nome.place(width=250, height=40, x=150 , y=10)

    tx_nota1 = Entry(janela_inserir, justify="center", textvariable=nota1, borderwidth=5, relief='ridge')
    tx_nota1.place(width=50, height=40, x=150, y=74)

    tx_nota2 = Entry(janela_inserir, justify="center", textvariable=nota2, borderwidth=5, relief='ridge')
    tx_nota2.place(width=50, height=40, x=150, y=123)

    # Botão para confirmar a incersão
    bt_confirmar_insercao = Button(janela_inserir, bd=0, text="Inserir",
                                   command=lambda:confirma_insercao_aluno(tx_nome, tx_nota1, tx_nota2, janela_inserir))
    bt_confirmar_insercao.place(width=250, height=62, x=128 , y=192)

    janela_inserir.mainloop()

def confirma_insercao_aluno(tx_nome, tx_nota1, tx_nota2, janela_inserir):
    retorno = menu.inserir(tx_nome, tx_nota1, tx_nota2)
    tx_nome.delete(0, END)
    tx_nota1.delete(0, END)
    tx_nota2.delete(0, END)
    if retorno == 1:
        # Criando as labels
        label_aviso = Label(janela_inserir, text="Aluno cadastrado com sucesso!")
        label_aviso.place(width=250, height=62, x=128 , y=400)
    elif retorno == 400:
        # Criando as labels
        label_aviso = Label(janela_inserir, text="Dados inválidos. Não foi possível cadastar!")
        label_aviso.place(width=250, height=90, x=128, y=400)

def listar_aluno():
    janela_listar = Toplevel()
    janela_listar.title("LISTAR ALUNO")
    janela_listar.geometry("1080x600")
    janela_listar.minsize(1300, 600)
    janela_listar.maxsize(1300, 600)

    # Botão para sair da janela
    bt_voltar = Button(janela_listar, bd=0, bg="Red", text="Sair", command=lambda:sair(janela_listar))
    bt_voltar.place(width=250, height=62, x=1020, y=192)
    bt_atualizar = Button(janela_listar, bd=0, bg="Red", text="Atualizar", command=lambda:atualizar(janela_listar, 1))
    bt_atualizar.place(width=250, height=62, x=1020, y=100)

    # Foi criado uma classe para fazer o Scrollbar
    scroll.MyList(janela_listar)

    janela_listar.mainloop()

def atualizar(janela, id):
    janela.destroy()
    if id == 1:
        listar_aluno()
    elif id == 2:
        excluir_aluno()
    elif id == 3:
        media_turna()
    elif id == 4:
        pesquisar_aluno()
    elif id == 5:
        alterar_aluno()

def alterar_aluno():
    # Variáveis para armazenar os dados solicitados
    nome = StringVar()
    nota1 = StringVar()
    nota2 = StringVar()


    def alterar(matricula, janela_alterar_aluno):
        aluno_alterar = menu.alterar_checar_valor(matricula)
        alterar_plotar_valores(aluno_alterar, janela_alterar_aluno)


    def alterar_plotar_valores(aluno_alterar, janela_alterar_aluno):
        tx_nome = Entry(janela_alterar_aluno).delete(0, "end")
        tx_nota1 = Entry(janela_alterar_aluno).delete(0, "end")
        tx_nota2 = Entry(janela_alterar_aluno).delete(0, END)
        tx_excluir_aluno.delete(0, END)
        if aluno_alterar == 0:
            # Criando as labels
            label_informativa = Label(janela_alterar_aluno, justify="center", font=cf.font2, text="Matrícula não encontrada.")
            label_informativa.place(width=1300, height=250, x=1, y=10)
        elif aluno_alterar == 100:
            # Criando as labels
            label_informativa = Label(janela_alterar_aluno, justify="center", font=cf.font2, text="Informe uma matrícula válida.")
            label_informativa.place(width=1300, height=250, x=1, y=10)
        else:
            valor = []
            for key, valou in aluno_alterar.items():
                valor = valou

            # Criando as caixas de entrada de texto
            label_informativa = Label(janela_alterar_aluno, justify="center", font=cf.font2, text="")
            label_informativa.place(width=1300, height=150, x=1, y=10)

            tx_nome = Entry(janela_alterar_aluno, justify="center", textvariable=nome, borderwidth=5, relief='ridge')
            tx_nome.place(width=300, height=30, x=(1300 / 2) - (300 / 2), y=50)
            tx_nome.delete(0, END)
            tx_nome.insert(0, str(valor[0]))

            tx_nota1 = Entry(janela_alterar_aluno, justify="center", textvariable=nota1, borderwidth=5, relief='ridge')
            tx_nota1.place(width=50, height=30, x=(1300 / 2) - (50 / 2), y=124)
            tx_nota1.delete(0, END)
            tx_nota1.insert(0, str(valor[1]))

            tx_nota2 = Entry(janela_alterar_aluno, justify="center", textvariable=nota2, borderwidth=5, relief='ridge')
            tx_nota2.place(width=50, height=30, x=(1300 / 2) - (50 / 2), y=173)
            tx_nota2.delete(0, END)
            tx_nota2.insert(0, str(valor[2]))

            # Botão para confirmar a alualização do aluno
            bt_excluir_aluno = Button(janela_alterar_aluno, bd=0, bg='Red', text="Alterar",
                                      command=lambda:aluno_atualizado(nome, nota1, nota2, aluno_alterar, tx_nome, tx_nota1, tx_nota2))
            bt_excluir_aluno.place(width=250, height=62, x=420, y=(600 - 150))


    def aluno_atualizado(nome, nota1, nota2, aluno_alterar, tx_nome, tx_nota1, tx_nota2):
        valor = menu.alterar(nome, nota1, nota2, aluno_alterar)

        if valor == 0:
            # Criando as labels
            label_informativa = Label(janela_alterar_aluno, justify="center", font=cf.font2, text="Atualização Falhou")
            label_informativa.place(width=1300, height=250, x=1, y=10)
        else:
            # Criando as labels
            label_informativa = Label(janela_alterar_aluno, justify="center", font=cf.font2, text="Atualizado com sucesso!")
            label_informativa.place(width=1300, height=250, x=1, y=10)
            tx_nome.delete(0, "end")
            tx_nota1.delete(0, END)
            tx_nota2.delete(0, END)


    def alterar_nulo():
        # Criando as labels
        label_informativa = Label(janela_alterar_aluno, justify="center", font=cf.font2, text="Informe uma matrícula válida.")
        label_informativa.place(width=1300, height=250, x=1, y=10)
        tx_excluir_aluno.delete(0, END)


    janela_alterar_aluno = Toplevel()
    janela_alterar_aluno.title("ALTERAR CADASTRO")
    janela_alterar_aluno.geometry("800x500")
    janela_alterar_aluno.minsize(1300, 600)
    janela_alterar_aluno.maxsize(1300, 600)

    # Variável para armazenar a matrícula solicitada
    matricula = StringVar()

    # Criando as caixas de entrada de texto
    tx_excluir_aluno = Entry(janela_alterar_aluno, justify="center", bg='Gray', font=cf.font2, textvariable=matricula, borderwidth=5,
                             relief='ridge')
    tx_excluir_aluno.place(width=70, height=50, x=50, y=(600-150))

    # Botão para buscar o aluno
    bt_excluir_aluno = Button(janela_alterar_aluno, bd=0, bg='Red', text="Buscar", command=lambda:alterar(matricula, janela_alterar_aluno))
    bt_excluir_aluno.place(width=250, height=50, x=150, y=(600-150))

    # Botão para confirmar a alualização do aluno
    bt_excluir_aluno = Button(janela_alterar_aluno, bd=0, bg='Red', text="Alterar", command=alterar_nulo)
    bt_excluir_aluno.place(width=250, height=50, x=420, y=(600-150))

    # Botão para atualizar janela
    bt_voltar = Button(janela_alterar_aluno, bd=0, bg='Red', text="Atualizar", command=lambda: atualizar(janela_alterar_aluno, 5))
    bt_voltar.place(width=250, height=50, x=690, y=(600-150))

    # Botão para sair da janela
    bt_voltar = Button(janela_alterar_aluno, bd=0, bg='Red', text="Sair", command=lambda: sair(janela_alterar_aluno))
    bt_voltar.place(width=250, height=50, x=960, y=(600-150))

    janela_alterar_aluno.mainloop()




def excluir_aluno():
    janela_excluir_aluno = Toplevel()
    janela_excluir_aluno.title("DELETAR")
    janela_excluir_aluno.geometry("800x500")
    janela_excluir_aluno.minsize(1300, 600)
    janela_excluir_aluno.maxsize(1300, 600)


    # Variável para armazenar a matrícula solicitada
    matricula = StringVar()

    # Criando as caixas de entrada de texto
    tx_excluir_aluno = Entry(janela_excluir_aluno, justify="center", bg='Gray', font=cf.font2, textvariable=matricula, borderwidth=5, relief='ridge')
    tx_excluir_aluno.place(width=70, height=50, x=50, y=(600-150))

    # Botão para confirmar a a exclusão
    bt_excluir_aluno = Button(janela_excluir_aluno, bd=0, bg='Red', text="Deletar", command=lambda:excluir(matricula, janela_excluir_aluno, tx_excluir_aluno))
    bt_excluir_aluno.place(width=250, height=50, x=150, y=(600-150))

    # Botão para atualizar janela
    bt_voltar = Button(janela_excluir_aluno, bd=0, bg='Red', text="Atualizar", command=lambda: atualizar(janela_excluir_aluno, 2))
    bt_voltar.place(width=250, height=50, x=430, y=(600-150))

    # Botão para sair da janela
    bt_voltar = Button(janela_excluir_aluno, bd=0, bg='Red', text="Sair", command=lambda: sair(janela_excluir_aluno))
    bt_voltar.place(width=250, height=50, x=710, y=(600-150))

    janela_excluir_aluno.mainloop()

def excluir(matricula, janela_excluir_aluno, tx_excluir_aluno):
    msg1 = f"Essa matricula não exixit"
    valor = menu.excluir(matricula.get())
    tx_excluir_aluno.delete(0, END)
    if type(valor) is list:
        try:
            msg2 = f"{valor[0]} foi excluido com sucesso"
        except:
            msg = f"ID {valor}, não existe no banco de dados."
            label_excluir_aluno = Label(janela_excluir_aluno, bg='Yellow', font=cf.font1, text=msg)
            label_excluir_aluno.place(width=300, height=62, x=20, y=100)
        else:
            if valor == 0:
                label_excluir_aluno = Label(janela_excluir_aluno, bg='Yellow', font=cf.font1, text=msg1)
                label_excluir_aluno.place(width=300, height=62, x=20, y=100)
            else:
                label_excluir_aluno = Label(janela_excluir_aluno, bg='Yellow', font=cf.font1, text=msg2)
                label_excluir_aluno.place(width=300, height=62, x=20, y=100)
    else:
        msg = f"ID {valor}, não existe no banco de dados."
        label_excluir_aluno = Label(janela_excluir_aluno, bg='Yellow', font=cf.font1, text=msg)
        label_excluir_aluno.place(width=300, height=62, x=20, y=100)


def media_turna():
    janela_media_turma = Toplevel()
    janela_media_turma.title("MÉDIA DA TRUMA")
    janela_media_turma.geometry("500x500")
    janela_media_turma.minsize(500, 500)
    janela_media_turma.maxsize(500, 500)
    media_turma = menu.mediaTurma()

    msg = f"A média da truma é = {media_turma:.2f}"

    # Criando as labels
    label_media_turma = Label(janela_media_turma, font=('Arial', 15), text=msg)
    label_media_turma.place(width=250, height=62, x=10, y=1)

    # Botão para atualizar janela
    bt_voltar = Button(janela_media_turma, bd=0, bg='Red', text="Atualizar", command=lambda: atualizar(janela_media_turma, 3))
    bt_voltar.place(width=250, height=62, x=100, y=300)

    janela_media_turma.mainloop()

def pesquisar_aluno():
    janela_pesquisar_aluno = Toplevel()
    janela_pesquisar_aluno.title("PESQUISAR")
    janela_pesquisar_aluno.geometry("800x500")
    janela_pesquisar_aluno.minsize(1300, 600)
    janela_pesquisar_aluno.maxsize(1300, 600)

    # Variável para armazenar a matrícula solicitada
    valor = StringVar()
    # Criando as caixas de entrada de texto
    tx_pesquisar_aluno = Entry(janela_pesquisar_aluno, justify="center", bg='Gray', font=cf.font2, textvariable=valor, borderwidth=5, relief='ridge')
    tx_pesquisar_aluno.place(width=70, height=50, x=50, y=(600-150))

    # Botão para confirmar a pesquisa
    bt_confirmar_insercao = Button(janela_pesquisar_aluno, bd=0, bg='Red', text="Pesquisar", command=lambda:pesquisar(valor, janela_pesquisar_aluno, tx_pesquisar_aluno))
    bt_confirmar_insercao.place(width=250, height=50, x=150, y=(600-150))

    # Botão para atualizar janela
    bt_voltar = Button(janela_pesquisar_aluno, bd=0, bg='Red', text="Atualizar", command=lambda: atualizar(janela_pesquisar_aluno, 4))
    bt_voltar.place(width=250, height=50, x=430, y=(600-150))

    # Botão para sair da janela
    bt_voltar = Button(janela_pesquisar_aluno, bd=0, bg='Red', text="Sair", command=lambda:sair(janela_pesquisar_aluno))
    bt_voltar.place(width=250, height=50, x=710, y=(600-150))

    janela_pesquisar_aluno.mainloop()


def pesquisar(pesquisar, janela_pesquisar_aluno, tx_pesquisar_aluno):
    pesquisar_aluno = menu.pesquisar(pesquisar)
    try:
        msg2 = ""
        int(pesquisar.get())
        if pesquisar_aluno != 0:
            show_campos(janela_pesquisar_aluno)
        else:
            msg2 = f"Não foi encontrado o aluno referente a matricula: {pesquisar.get()}"
    except:
        msg = pesquisar_aluno
        label_pesquisar_aluno1 = Label(janela_pesquisar_aluno, font=cf.font1, text="")
        label_pesquisar_aluno1.place(width=1300, height=100, x=0, y=0)
        label_pesquisar_aluno2 = Label(janela_pesquisar_aluno, font=cf.font1, text=msg)
        label_pesquisar_aluno2.place(width=500, height=50, x=10, y=100)
    else:
        label_pesquisar_aluno1 = Label(janela_pesquisar_aluno, font=cf.font1, text="")
        label_pesquisar_aluno1.place(width=1300, height=100, x=0, y=0)
        label_pesquisar_aluno = Label(janela_pesquisar_aluno, font=cf.font1, text=msg2)
        label_pesquisar_aluno.place(width=500, height=50, x=10, y=100)
        if pesquisar_aluno != 0:
            for key, value in pesquisar_aluno.items():
                if int(pesquisar.get()) == key:
                    label_pesquisar_aluno_key = Label(janela_pesquisar_aluno, font=cf.font1, text=key)
                    label_pesquisar_aluno_key.grid(column=0, row=1)

                    for i in range(5):
                            label_pesquisar_aluno = Label(janela_pesquisar_aluno, font=cf.font1, text=value[i])
                            label_pesquisar_aluno.grid(column=i+1, row=1)
    tx_pesquisar_aluno.delete(0, "end")


def show_campos(janela_show_campos):
    font = Configuracao().font1
    Label(janela_show_campos, font=font, text=f" MATRÍCULA ").grid(column=0, row=0)
    Label(janela_show_campos, font=font, text=f"                 NOME               ").grid(column=1, row=0)
    Label(janela_show_campos, font=font, text=f" NOTA 01 ").grid(column=2, row=0)
    Label(janela_show_campos, font=font, text=f" NOTA 02 ").grid(column=3, row=0)
    Label(janela_show_campos, font=font, text=f" MÉDIA ").grid(column=4, row=0)
    Label(janela_show_campos, font=font, text=f" RESULTADO ").grid(column=5, row=0)

def sair(janela):
    menu.sair(janela)

def main():
    janela = Tk()
    janela.title("CADASTRO DE ALUNOS")
    janela.geometry("500x500")
    janela.minsize(500, 500)
    janela.maxsize(500, 500)

    bt_inserir = Button(janela, bd=0, text="Inserir",  command=inserir_aluno)
    bt_inserir.place(width=250, height=62, x=128 , y=64)

    bt_listar = Button(janela, bd=0, text="Listar",  command=listar_aluno)
    bt_listar.place(width=250, height=62, x=128 , y=113)

    bt_alterar = Button(janela, bd=0, text="Alterar",  command=alterar_aluno)
    bt_alterar.place(width=250, height=62, x=128 , y=192)

    bt_remover = Button(janela, bd=0, text="remover",  command=excluir_aluno)
    bt_remover.place(width=250, height=62, x=128 , y=256)

    bt_pesquisar = Button(janela, bd=0, text="Media da Turma",  command=media_turna)
    bt_pesquisar.place(width=250, height=62, x=128 , y=320)

    bt_pesquisar = Button(janela, bd=0, text="Pesquisar", command=pesquisar_aluno)
    bt_pesquisar.place(width=250, height=62, x=128, y=384)

    bt_media_turma = Button(janela, bd=0, text="Sair",  command=lambda:sair(janela))
    bt_media_turma.place(width=250, height=62, x=128 , y=458)

    janela.mainloop()

if __name__ == '__main__':
    main()
