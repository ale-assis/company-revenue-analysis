#!/usr/bin/env python
# coding: utf-8

# **Vamos criar a lógica de programação do nosso Desafio de Análise de Dados**

# In[1]:


import os
import pandas as pd


lista_arquivo = os.listdir("D:\Desktop\Cursos HUB\Curso Básico de Python\Vendas")
#display(lista_arquivo)

tabela_total = pd.DataFrame()


for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f"D:\Desktop\Cursos HUB\Curso Básico de Python\Vendas\{arquivo}")
        tabela_total = tabela_total.append(tabela)
#display(tabela_total)
    
tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos [["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
display(tabela_produtos)

tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"] 
tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento[["Quantidade Vendida", "Faturamento"]].sort_values(by="Faturamento", ascending=False)
display(tabela_faturamento)

tabela_loja = tabela_total.groupby("Loja").sum()
tabela_loja = tabela_loja[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
display(tabela_loja)

import plotly.express as px
# importei o plotly express aqui pois quando eu coloquei ele no começo, deu erro

grafico = px.bar(tabela_loja, x=tabela_loja.index, y="Faturamento")
grafico.show()


# In[ ]:




