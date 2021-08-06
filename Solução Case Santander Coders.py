#!/usr/bin/env python
# coding: utf-8

# # <center>Santander Coders & Let's Code | Ciência de Dados<center>

# ## Case = Quantas pastas dentais são vendidas no Brasil por mês?

# ### <center>Referências e Coleta de Dados<center>
# 
# Para esse estudo foram realizados pesquisa e coletados os dados das seguintes fontes:
#  -  Instituto Brasileiro de Geografia - IBGE
#  -  Agência Global de Comunicação Edelman Insights
#  -  Conselho Federal de Odontologia
#  -  Pesquisador Daniel Duque do Instituto Brasileiro de Economia da Fundação Getúlio Vargas
# 

# ------------------------------------------------

# Etapa 1 - Levantamento da População do Estudo

PGB = 213368687

#Importanto Bibliotecas Python necessárias para Manipulação de Dados:

import pandas as pd
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

# --------------------------------

# Etapa 2 - Transformação dos Dados


CB = PGB * 0.07

print("%.2f" %CB)

PNPD = 16000000

PEP = PGB * 0.065
print("%.2f" % PEP)

PCI = CB + PNPD + PEP
print("%.2f" % PCI)

data = {
    'Nome Variável': ['CB', 'PNPD', 'PEP', 'PCI'],
    'População Inválida': ['Crianças Brasileiras', 'Não Possuem Dente', 'Extrema Pobreza','Total População Inválida'],
    'Total':["%.2f" % CB, "%.2f" % PNPD, "%.2f" % PEP, "%.2f" % PCI]}

df = pd.DataFrame(data, columns=['Nome Variável','População Inválida','Total'])
print(df)

PCV = PGB - PCI
print("%.2f" % PCV)

data = {
    'Nome Variável': ['PGB', 'PCI', 'PCV'],
    'População': ['População Geral','População Inválida', 'Consumidores Válidos'],
    'Total': ["%.2f" % PGB, "%.2f" % PCI, "%.2f" %PCV ]}

dfg = pd.DataFrame(data, columns=['Nome Variável','População', 'Total'])
print(dfg)

# --------------------------------

# Etapa 3 -  Cálculo: Média de Consumo Diário e Mensal Individual
MD = 4 * 2
print(MD)

MM = MD * 30
print(MM)

# --------------------------------

#  Etapa 4 -  Cálculo: Média de Consumo Mensal - Total de Consumidores

CMT = MM * PCV
print(CMT)

# Conversão de valor de variável CMT para de gramas para kilos.

CMK = CMT / 1000
print("%.2f" % CMK)

# --------------------------------

# Etapa 5 - Conclusão do Estudo
print("%.2f" % CMK)