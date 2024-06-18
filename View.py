# importando SQLite
import sqlite3 as lite

# Importando Pandas
import pandas as pd

# Criando Conexão com BD
con = lite.connect('dados.db')

# Funções de Inserir ----------------------------
# Inserir Categorias


def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, i)

# teste de incerção -- inserir_categoria(["Gasolina"])
# Inserir Receitas


def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)

# Inserir Despesas


def inserir_despesa(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Despesas (categoria, retirado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)

# Funções para Deletar ----------------------------
# Deletar Receitas


def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query, i)

# Deletar Despesas


def deletar_despesas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Despesas WHERE id=?"
        cur.execute(query, i)

# Funções para dados ---------------------------
# Ver Categoria


def ver_categoria():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

# Ver Receitas


def ver_receitas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    return lista_itens

# Ver Despesas


def ver_despesas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Despesas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

# Função para dados da tabela


def tabela():
    despesas = ver_despesas()
    receitas = ver_receitas()

    tabela_lista = []

    for i in despesas:
        tabela_lista.append(i)

    for i in receitas:
        tabela_lista.append(i)

    return tabela_lista

# Função para dados do grafico de bar
def bar_valores():
    # Receita Total -------------
    receitas = ver_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)

    # Despesas Total -------------
    despesas = ver_despesas()
    despesas_lista = []

    for i in despesas:
        despesas_lista.append(i[3])

    despesas_total = sum(despesas_lista)

    # Saldo total -----------
    saldo_total = receita_total - despesas_total

    return [receita_total, despesas_total, saldo_total]

# função grafico pie


def pie_valores():
    despesas = ver_despesas()
    tabela_lista = []

    for i in despesas:
        tabela_lista.append(i)

    dataframe = pd.DataFrame(tabela_lista, columns=[
                             'id', 'categoria', 'Data', 'valor'])
    dataframe = dataframe.groupby('categoria')['valor'].sum()

    lista_quantidade = dataframe.values.tolist()
    lista_categorias = []

    for i in dataframe.index:
        lista_categorias.append(i)

    return ([lista_categorias, lista_quantidade])

# Função Porcentagem
def porcento_valor():
    # Receita Total -------------
    receitas = ver_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)

    # Despesas Total -------------
    despesas = ver_despesas()
    despesas_lista = []

    for i in despesas:
        despesas_lista.append(i[3])

    despesas_total = sum(despesas_lista)

    # Porcentagem total -----------
    total = ((receita_total - despesas_total) / receita_total)* 100

    return [total]