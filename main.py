# importando tkinter
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

# Importando Pandas
import pandas as pd

# Importar Babel formatar valor
from babel.numbers import format_currency

# importando Pillow
from PIL import Image, ImageTk

# importando barra de progresso do tkinter
from tkinter.ttk import Progressbar

# Importando Matplolib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# Importar Calendario tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date, datetime

# Importando funções da view
from View import bar_valores, pie_valores, porcento_valor,  inserir_categoria, ver_categoria, inserir_receita, inserir_despesa, tabela, deletar_despesas, deletar_receitas

################# cores ###############
co0 = "#2e2d2b"   # Preta
co1 = "#feffff"   # branca
co2 = "#4fa882"   # verde
co3 = "#38576b"   # Cinza
co4 = "#403d3d"   # Marron
co5 = "#e06636"   # Laranja
co6 = "#038cfc"   # azul
co7 = "#5994b3"   # azul meio cinza Frame cima
co8 = "#263238"   # Cinza escuro
co9 = "#e9edf5"   # Branco
co10 = "#daed6b"  # Amarelo
co11 = "#ffffff"  # Branco
co12 = "#CCCCCC"  # Cinza
co13 = "#EEEEEE"  # Branco
co14 = "#545454"  # Cinza Escuro
co15 = "#83a9e6"  # Azul meio roxo
co16 = "#5c7178"  # Cinza frame meio
co17 = "#6f777a"  # Cinza frame baixo
co18 = "#2d3133"  # Cinza Frame pie
co19 = "#000000"  # preto
co20 = "#969a9c"  # Cinza claro
co21 = "#de6f6f"  # Vermelho frame configurações despesas
co22 = "#86dbc7"  # Azul frame configurações receitas

colors = ['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555']

# Função para formatar um valor em reais


def formatar_valor_em_reais():
    return format_currency('BRL', locale='pt_BR')


# Criando Janela
janela = Tk()
janela.title()
janela.geometry('905x660')
janela.configure(background=co18)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")


# Criando Frames para divisão da tela
frameCima = Frame(janela, width=1043, height=50, bg=co16, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=361,
                  bg=co16, pady=20, relief="raised")
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co17, relief="flat")
frameBaixo.grid(row=2, column=0, pady=3, padx=10, sticky=NSEW)

frame_gra_pie = Frame(frameMeio, width=580, height=250, bg=co1)
frame_gra_pie.place(x=415, y=5)

# Frame Cima
# acessando a Imagem
app_img = Image.open('Logo.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text="    Controle Financeiro", width=900,
                 compound=LEFT, padx=5, relief=RAISED, font=('Verdana 20 bold'), bg=co7, fg=co19)
app_logo.place(x=0, y=0)

# Conectando a função ao Banco de dados
# Definindo tree como global
global tree

# Função inserir categoria


def inserir_categoria_b():
    nome = e_categoria.get()

    lista_inserir = [nome]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    # passando a lista para a função inserir despesas na view
    inserir_categoria(lista_inserir)

    messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso')

    e_categoria.delete(0, 'end')

    # Pegando os valores da categoria
    categorias_funcao = ver_categoria()
    categoria = []

    for i in categorias_funcao:
        categoria.append(i[1])

    # Atualizando a lista de categorias
    combo_categoria_despesas['values'] = (categoria)

# Função inserir Receitas


def inserir_receitas_r():
    nome = 'Receita'
    data = l_cal_receitas.get()
    valor = e_valor_receitas.get()

    lista_inserir = [nome, data, valor]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    # Chamando função Inserir Receitas na View
    inserir_receita(lista_inserir)

    messagebox.showinfo('Sucesso', 'Receita inserida com sucesso')

    l_cal_receitas.delete(0, 'end')
    e_valor_receitas.delete(0, 'end')

    # atualizando dados
    mostrar_renda()
    percentagem()
    grafico_bar()
    resumo()
    grafico_pie()

# Função inserir Despesas na view


def inserir_receitas_b():
    nome = combo_categoria_despesas.get()
    data = e_cal_despesas.get()
    # Ajustando formato de data
    # data = datetime.strptime(data, '%m/%d/%y').strftime('%d/%m/%Y')
    valor = e_valor_despesas.get()

    lista_inserir = [nome, data, valor]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    # Chamando função Inserir Despesas na View
    inserir_despesa(lista_inserir)

    messagebox.showinfo('Sucesso', 'Despesa inserida com sucesso')

    combo_categoria_despesas.delete(0, 'end')
    e_cal_despesas.delete(0, 'end')
    e_valor_despesas.delete(0, 'end')

    # atualizando dados
    mostrar_renda()
    percentagem()
    grafico_bar()
    resumo()
    grafico_pie()

# Função Deletar


def deletar_dados():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        nome = treev_lista[1]

        if nome == 'Receita':
            deletar_receitas([valor])
            messagebox.showinfo('Sucesso', 'Receita deletada com sucesso')

            # atualizando dados
            mostrar_renda()
            percentagem()
            grafico_bar()
            resumo()
            grafico_pie()

        else:
            deletar_despesas([valor])
            messagebox.showinfo('Sucesso', 'Despesa deletada com sucesso')

            # atualizando dados
            mostrar_renda()
            percentagem()
            grafico_bar()
            resumo()
            grafico_pie()

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


# Porcentagem


def percentagem():
    l_nome = Label(frameMeio, text="Porcentagem da Receita",
                   height=1, anchor=NW, font=('Verdana 12'), bg=co20, fg=co19)
    l_nome.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background=co10)
    style.configure("TProgressbar", thickness=25)
    bar = Progressbar(frameMeio, length=180,
                      style="black.Horizontal.TProgressbar")
    bar.place(x=10, y=35)
    bar['value'] = porcento_valor()[0]

    valor = porcento_valor()[0]

    l_percentagem = Label(frameMeio, text="{:,.2f}%".format(
        valor), anchor=NW, font=('Verdana 12'), bg=co20, fg=co19)
    l_percentagem.place(x=200, y=35)

# Função para Grafico Barra


def grafico_bar():
    lista_categorias = ['Receita', 'Despesas', 'Saldo']
    lista_valores = bar_valores()

    # Faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    # ax.autoscale(enabre=true, axis='both', tight=Nome)
    ax.bar(lista_categorias, lista_valores, color=colors, width=0.9)
    # create a list to collect the plt.patches data

    c = 0
    # set individual bar lables using above list
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom', color='dimgrey')
        c += 1

    ax.set_xticks(range(len(lista_categorias)))
    ax.set_xticklabels(lista_categorias, fontsize=16)

    ax.patch.set_facecolor(co11)
    ax.spines['bottom'].set_color(co19)
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color(co19)
    ax.spines['left'].set_linewidth(1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color=co19)
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)

# Função de Resumo total


def resumo():
    valor = bar_valores()

    l_sumario = Label(frameMeio, text="Despesas".upper(
    ), anchor=NW, font=('Verdana 12'), bg=co20, fg=co19)
    l_sumario.place(x=609, y=15)
    l_linha = Label(frameMeio, text="", width=180, height=1,
                    anchor=NW, font=('Arial 1'), bg=co19)
    l_linha.place(x=309, y=52)
    l_sumario = Label(frameMeio, text="Total Receita      ".upper(
    ), anchor=NW, font=('Verdana 12'), bg=co20, fg=co19)
    l_sumario.place(x=309, y=35)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(
        valor[0]), anchor=NW, font=('arial 17'), bg=co20, fg=co19)
    l_sumario.place(x=309, y=70)

    l_linha = Label(frameMeio, text="", width=180, height=1,
                    anchor=NW, font=('Arial 1'), bg=co19)
    l_linha.place(x=309, y=132)
    l_sumario = Label(frameMeio, text="Total Despesa     ".upper(
    ), anchor=NW, font=('Verdana 12'), bg=co20, fg=co19)
    l_sumario.place(x=309, y=115)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(
        valor[1]), anchor=NW, font=('arial 17'), bg=co20, fg=co19)
    l_sumario.place(x=309, y=150)

    l_linha = Label(frameMeio, text="", width=180, height=1,
                    anchor=NW, font=('Arial 1'), bg=co19)
    l_linha.place(x=309, y=207)
    l_sumario = Label(frameMeio, text="Total Saldo        ".upper(
    ), anchor=NW, font=('Verdana 12'), bg=co20, fg=co19)
    l_sumario.place(x=309, y=190)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(
        valor[2]), anchor=NW, font=('arial 17'), bg=co20, fg=co19)
    l_sumario.place(x=309, y=220)

# função Grafico pizza


def grafico_pie():
    # faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = pie_valores()[1]
    lista_categorias = pie_valores()[0]

    # only "explode" the 2nd slice (i.e. 'Hogs')
    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.legend(lista_categorias, loc="center right",
              bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie)
    canva_categoria.get_tk_widget().grid(row=0, column=0)


percentagem()
grafico_bar()
resumo()
grafico_pie()

# Criando Frames dentro do Frame Baixo
frame_renda = Frame(frameBaixo, width=300, height=250, bg=co19, relief="flat")
frame_renda.grid(row=0, column=0)

frame_operacoes = Frame(frameBaixo, width=220,
                        height=250, bg=co21, relief="flat")
frame_operacoes.grid(row=0, column=1, padx=35)

frame_configuracao = Frame(frameBaixo, width=220,
                           height=250, bg=co22, relief="flat")
frame_configuracao.grid(row=0, column=2, padx=5)

# Tabela Renda Mensal -------------------------
app_tabela = Label(frameMeio, text=" Tabela Receitas e Despesas ",
                   anchor=NW, font=('Verdana 12'), bg=co20, fg=co19)
app_tabela.place(x=5, y=309)

# funcao mostrar_renda


def mostrar_renda():
    # creating a treeview with dual scrollbars
    tabela_head = ['ID', 'Categoria', 'Data', 'Valor']

    lista_itens = tabela()

    global tree

    tree = ttk.Treeview(frame_renda, selectmode="extended",
                        columns=tabela_head, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd = ["center", "center", "center", "center"]
    h = [30, 100, 100, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # ajustando a coluna
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in lista_itens:
        tree.insert('', 'end', values=item)


mostrar_renda()

# Configuração Despesas -----------------------
l_info = Label(frame_operacoes, text='Insira Despesas', height=1,
               anchor=NW, font=('Verdana 10 bold'), bg=co21, fg=co19)
l_info.place(x=10, y=10)

# Categoria --------
l_categoria = Label(frame_operacoes, text='Categoria',
                    height=1, anchor=NW, font=('ivy 10'), bg=co21, fg=co19)
l_categoria.place(x=10, y=40)

# Pegando categorias
categoria_funcao = ver_categoria()
categoria = []

for i in categoria_funcao:
    categoria.append(i[1])

combo_categoria_despesas = ttk.Combobox(
    frame_operacoes, width=10, font=('ivy 10'))
combo_categoria_despesas['values'] = (categoria)
combo_categoria_despesas.place(x=110, y=41)

# Data de Despesas ----------
e_cal_despesas = Label(frame_operacoes, text='Data',
                       height=1, anchor=NW, font=('ivy 10'), bg=co21, fg=co19)
e_cal_despesas.place(x=10, y=70)

e_cal_despesas = DateEntry(frame_operacoes, width=12, background='darkblue',
                           foregorund='white', borderwidth=2, year=2024, date_pattern='dd/mm/yyyy')
e_cal_despesas.place(x=110, y=71)

# Valor despesas ----------
l_valor_despesas = Label(frame_operacoes, text='Valor Despesas',
                         height=1, anchor=NW, font=('ivy 10'), bg=co21, fg=co19)
l_valor_despesas.place(x=10, y=100)

e_valor_despesas = Entry(frame_operacoes, width=14,
                         justify='left', relief='solid')
e_valor_despesas.place(x=110, y=101)

# Botão Inserir Despesas
img_add_despesas = Image.open('add.png')
img_add_despesas = img_add_despesas.resize((17, 17))
img_add_despesas = ImageTk.PhotoImage(img_add_despesas)

botao_inserir_despesas = Button(frame_operacoes, command=inserir_receitas_b, image=img_add_despesas, text=" Adicionar".upper(), width=80,
                                compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co19, overrelief=RIDGE)
botao_inserir_despesas.place(x=110, y=131)

# Botão Excluir
l_excluir = Label(frame_operacoes, text='Excluir ação',
                  height=1, anchor=NW, font=('ivy 10 bold'), bg=co21, fg=co19)
l_excluir.place(x=10, y=190)

img_deletar = Image.open('delete.png')
img_deletar = img_deletar.resize((17, 17))
img_deletar = ImageTk.PhotoImage(img_deletar)

botao_deletar = Button(frame_operacoes, command=deletar_dados, image=img_deletar, text=" Deletar".upper(), width=80,
                       compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co19, overrelief=RIDGE)
botao_deletar.place(x=110, y=190)

# Configurações Receitas ----------------------------
l_info = Label(frame_configuracao, text='Insira Receitas', height=1,
               anchor=NW, font=('Verdana 10 bold'), bg=co22, fg=co19)
l_info.place(x=10, y=10)

# Data das Receitas ----------
l_cal_receitas = Label(frame_configuracao, text='Data',
                       height=1, anchor=NW, font=('ivy 10'), bg=co22, fg=co19)
l_cal_receitas.place(x=10, y=40)

l_cal_receitas = DateEntry(frame_configuracao, width=12, background='darkblue',
                           foregorund='white', borderwidth=2, year=2024, date_pattern='dd/mm/yyyy')
l_cal_receitas.place(x=110, y=41)

# Valor Receitas ----------
l_valor_receitas = Label(frame_configuracao, text='Valor Receitas',
                         height=1, anchor=NW, font=('ivy 10'), bg=co22, fg=co19)
l_valor_receitas.place(x=10, y=71)

e_valor_receitas = Entry(frame_configuracao, width=14,
                         justify='left', relief='solid')

e_valor_receitas.place(x=110, y=71)


# Botão Inserir Receitas
img_add_rececitas = Image.open('add.png')
img_add_rececitas = img_add_rececitas.resize((17, 17))
img_add_rececitas = ImageTk.PhotoImage(img_add_rececitas)

botao_inserir_rececitas = Button(frame_configuracao, command=inserir_receitas_r, image=img_add_rececitas, text=" Adicionar".upper(), width=80,
                                 compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief=RIDGE)
botao_inserir_rececitas.place(x=110, y=111)

# Operação nova categoria ----------------------------
l_info = Label(frame_configuracao, text='Categoria', height=1,
               anchor=NW, font=('Ivy 10 bold'), bg=co22, fg=co19)
l_info.place(x=10, y=160)

e_categoria = Entry(frame_configuracao, width=14,
                    justify='left', relief='solid')
e_categoria.place(x=110, y=160)

# Botão Inserir Categoria
img_add_categoria = Image.open('add.png')
img_add_categoria = img_add_categoria.resize((17, 17))
img_add_categoria = ImageTk.PhotoImage(img_add_categoria)

botao_inserir_categoria = Button(frame_configuracao, command=inserir_categoria_b, image=img_add_categoria, text=" Adicionar".upper(), width=80,
                                 compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co19, overrelief=RIDGE)
botao_inserir_categoria.place(x=110, y=190)


janela.mainloop()
