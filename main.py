from tkinter import *
from tkinter import ttk
from tkinter import messagebox
alunos=[
    {"matricula": 1,
     "nome": "Jonas Lopes",
     "idade": 18,
     "curso": "Javascript",
     "novato":False}]
matricula_atual = 1
index = 0

def atualizarTabela()-> None:
    for linha in tabela.get_children():
        tabela.delete(linha)


    for aluno in alunos:
        tabela.insert("",END,values=(aluno["matricula"],aluno["nome"],aluno["idade"],aluno["curso"],aluno["novato"]))
def adicionarAluno() -> None:
    global matricula_atual
    matricula_atual +=1
    nome=txtNome.get()
    idade= int(txtIdade.get())
    curso=comboCursos.get()
    novato=opcao.get()

    aluno={
        "matricula": matricula_atual,
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "novato":novato
    }
    messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso!")
    alunos.append(aluno)
    limparCampos()
    atualizarTabela()
def limparCampos() -> None:
    txtMatricula.config(state=NORMAL)
    txtMatricula.delete(0,END,)
    txtMatricula.config(state=DISABLED)
    txtNome.delete(0, END)
    txtIdade.delete(0, END)
    comboCursos.set("")
    opcao.set(False)

def preencherCampos(event) -> None:
    linha_selecionada = tabela.selection()
    global index
    index = tabela.index(linha_selecionada)
    aluno=alunos[index]
    limparCampos()
    txtMatricula.config(state=NORMAL)
    txtMatricula.insert(END, str(aluno['matricula']))
    txtMatricula.config(state=DISABLED)
    txtNome.insert(END, aluno["nome"])
    txtIdade.insert(END, str(aluno["idade"]))
    comboCursos.set(aluno["curso"])

janela=Tk()
janela.title("Alunos - Infinity")

labelSaudacao=Label(janela, text="Seja-Bem Vindo(a)",
                    font=("Arial, 22 bold"), fg = "black")
labelSaudacao.grid(row=0, column=1, sticky=N)
labelInfo=Label(janela, text="Alunos Infinity",
                font=("Arial, 15"), fg="red")
labelInfo.grid(row=1, column=1,sticky=N)

labelMatricula=Label(janela, text="Matricula: ",
                     font="Tahoma 16",fg="black")
labelMatricula.grid(row=2,column=0,sticky=W)
txtMatricula=Entry(janela, font="Tahoma 16",width=25,state=DISABLED)
txtMatricula.grid(row=2, column=1)

labelNome = Label(janela, text="Nome: ",
                  font="Tahoma 16", fg="black")
labelNome.grid(row=3,column=0,sticky=W)
txtNome=Entry(janela, font="Tahoma 15", width=25)
txtNome.grid(row=3, column=1)
labelIdade = Label(janela,text="Idade: ",
                   font="Tahoma 16", fg="Black")
labelIdade.grid(row=4, column=0, sticky=W)
txtIdade=Entry(janela,font="Tahoma 15",width=25)
txtIdade.grid(row=4,column=1)
labelCurso=Label(janela, text="Curso: ",
                 font="Tahoma 15",fg="Black")
labelCurso.grid(row=5,column=0,sticky=W)

cursos = ["Javascript", "Python", "React", "NodeJs"]
comboCursos = ttk.Combobox(janela, font="Tahoma 15", values=cursos, width=23)
comboCursos.grid(row=5,column=1)

labelNovato=Label(janela,text="Novato?",font="Tahoma 16", fg="black")
labelNovato.grid(row=6,column=0,sticky=W)

opcao=BooleanVar(value=False)
checkNovato = ttk.Checkbutton(janela, width=30, text="Marcar apenas para novos alunos", variable=opcao)
checkNovato.grid(row=6,column=1)

btnAdicionar = Button(janela,text="Adicionar",
                      font="Calibri 12 bold", bg="papayawhip",fg="black",command=adicionarAluno)
btnAdicionar.grid(row=7,column=0)
btnEditar = Button(janela, text="Editar",
                   font="Calibri 12 bold", bg="papayawhip", fg="black",command=None)
btnEditar.grid(row=7, column=1)
btnExcluir=Button(janela,text="Excluir",
                  font="Calibri 12 bold", bg="papayawhip", fg="black",command=None)
btnExcluir.grid(row=7,column=2)

colunas=["Matricula","Nome","Idade","Curso","Novato"]
tabela= ttk.Treeview(janela,columns=colunas, show="headings")
for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column(coluna,width=110)
tabela.grid(row=8, columnspan=3)
tabela.bind("<ButtonRelease-1>", preencherCampos)

atualizarTabela()
janela.mainloop()
