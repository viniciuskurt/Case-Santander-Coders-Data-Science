#!/usr/bin/env python
# coding: utf-8

# # <center>Santander Coders & Let's Code | Ciência de Dados<center>

# ## Case = Quantas pastas dentais são vendidas no Brasil por mês?
# 
# - O presente estudo tem o objetivo didático de simular o descobrimento referente ao total de vendas mensal de pastas de creme tental no Brasil.
# 
# 
# Realizando uma breve analise lógica, é provável que uma boa solução para essa questão seria tentar estipular o número de consumidores do produto e verificar a quantidade de consumo individual diáriac  calculando o total de consumo x consumidores afim de chegarmos a uma estimativa plausível.
# 
# ----------

# ### <center>Referências e Coleta de Dados<center>
# 
# Para esse estudo foram realizados pesquisa e coletados os dados das seguintes fontes:
#  -  Instituto Brasileiro de Geografia - IBGE
#  -  Agência Global de Comunicação Edelman Insights
#  -  Conselho Federal de Odontologia
#  -  Pesquisador Daniel Duque do Instituto Brasileiro de Economia da Fundação Getúlio Vargas
# 

# ------------------------------------------

# # <center>Metodologia</center>
# 

# Para uma melhor compreensão o estudo foi dividido em 5 etapas:
# 
# - 1ª Etapa: Levantamento da População do Estudo.
# - 2ª Etapa: Tratamento dos Dados.
# - 3ª Etapa: Cálculo de média de consumo diário e mensal de pasta de dente.
# - 4ª Etapa: Cálculo de média de consumo de pasta por mês pelo total de consumidores.
# - 5ª Etapa: Conclusão do Estudo.
# 
# Vejamos minunciosamente a seguir cada uma delas.
# 
# -------------------------

# # <center>Etapa 1 - Levantamento da População do Estudo </center>

# Para iniciar do estudo, foi necessário pesquisar sobre a quantidade da população geral do  Brasil atualmente (julho 2021).
# 
# Para obter esses valores foi consultado a seguinte base de dados do IBGE.
# 
# - Estimado que a População do Brasil é de **<span style = "color: red">213.368.687</span>**
# 
# Vamos criar a variável **<span style = "color: blue">PGB</span>** (População Geral Brasil) e armazenar esse valor nela:
# 
# ##### <center><span style = "color: blue">PGB = <span style = "color: red">213.368.687</span></span></center>

# In[5]:


PGB = 213368687


# OBS:

#     Devemos tomar um certo cuidado aqui, pois devemos ter em mente que não são todos os elementos dessa população que se enquadram dentro da nossa pesquisa. Veremos sobre essa questão na próxima etapa.
#     
# Fonte: https://www.ibge.gov.br/apps/populacao/projecao/index.html
#     
# --------------------------

# In[6]:


#Importanto Bibliotecas Python necessárias para Manipulação de Dados:

import pandas as pd
import numpy as np


# # <center>Etapa 2 - Tratamento dos Dados </center>
# 
# 

# 
# Muitos elementos que estão classificados dentro da População geral não se enquandram dentro da nossa pesquisa, pois não possuem a carcterística de consumidores de creme dental ou seja, **por algum motivo não fazem o consumo do produto**. 
# 
# 
# Precisamos tratar esses dados retirando esses elementos afim de evitar um viés equívoco do projeto e assegurarmos um valor estimado de população de consumidores mais fiel para a base de nossos cálculos.
# 

# ### <center>**Tipos de elementos inválidos para a População de nosso Estudo:**<center>
# 
# Definídos como critérios desse estudo, temos 3 tipos de elementos que não fazem parte, são eles:
#     
# - Crianças entre 0 a 4 anos;
# - Brasileiros que não possuem nenhum dente;
# - Pessoas que vivem em situação de Extrema Pobreza.    
# 
# Vejamos a seguir mais detalhes sobre elas:

# 
# #### Crianças entre 0 a 4 anos:
#     
#     Sabemos que crianças dessa faixa etária não escovam os dentes ou não escovam os dentes de maneira adequada para      contabilizar significativamente no resultado de nosso estudo.
# 
# - Segundo o IBGE a estimativa dessa faixa etária é de aproximadamente **<span style = "color: red">7%</span>** da população.
# 
# - Logo se multiplicarmos essa porcentagem pela População Geral obtemos o valor aproximado de:
# 
# #####    <center style = "color: red">**213.368.687 x 0,07 = 14.935.808,09**</center>
# 
# 
# Vamos armazenar esse valor numa variável chamada <span style = "color: blue">**CB**</span> (crianças brasileiras):
# 
# 
# 
# ##### <center><span style = "color: blue">CB = <span style = "color: red">14.935.808,09</span></span></center>

# In[22]:


CB = PGB * 0.07

print("%.2f" %CB)


# Fonte: https://educa.ibge.gov.br/jovens/conheca-o-brasil/populacao/18318-piramide-etaria.html
# 
# ------------------------------

# 
# #### Brasileiros que não possuem nenhum dente:
#     
#     
#    Segundo um estudo de ***Percepções Latino-americanas sobre Perda de Dentes e Autoconfiança*** , realizado pela **Agência Global de Comunicação Edelman Insights** cerca de **<span style = "color:red">16.000.000</span>** de brasileiros vivem sem nenhum dente. Logo sabemos que essas pessoas não contabilizam acertivamente para nossa pesquisa.
#     
#     
# Vamos armazenar esse valor numa variável chamada <span style = "color: blue">**PNPD**</span> (População q Não Possuem Dente).
# 
# 
# ##### <center><span style = "color: blue">PNPD = <span style = "color: red">16.000.000</span></span></center>    
#     
# 
#     
# 

# In[8]:


PNPD = 16000000


# OBS: 
# 
# 

# 
# Já foi retirado dessa estatística os brasileiros que usam prótese dentária.
# 
# Fonte: https://ohoje.com/noticia/cidades/n/163244/t/a-perda-de-dentes-e-o-segundo-fator-que-mais-prejudica-a-qualidade-de-vida-das-pessoas/
# 
# --------------------------

# #### Pessoas que vivem em situação de Extrema Pobreza:
#     
# O Pesquisador ***Daniel Duque do Instituto Brasileiro de Economia da Fundação Getúlio Vargas*** em parceria com o IBGE,  informou em seu estudo que cerca de <span style = "color: red">6,5%</span> da população vivem em situação de miséria no Brasil.
# 
# Sabemos que essa população basicamente vive com doações portanto não faz parte dos consumidores de nosso estudo.
# 
# 
# #####    <center style = "color: red">**213.368.687 x 0,065% = 13.868.964,66**</center>
# 
# 
# Vamos armazenar esse valor numa variável chamada <span style = "color: blue">**PEP**</span> (População Extrema Pobreza):
# 
# 
# 
# ##### <center><span style = "color: blue">PEP = <span style = "color: red">13.868.964,66</span></span></center>
# 
#   

# In[9]:


PEP = PGB * 0.065
print("%.2f" % PEP)


# Fonte: https://agenciadenoticias.ibge.gov.br/agencia-sala-de-imprensa/2013-agencia-de-noticias/releases/29431-sintese-de-indicadores-sociais-em-2019-proporcao-de-pobres-cai-para-24-7-e-extrema-pobreza-se-mantem-em-6-5-da-populacao#:~:text=de%20Notícias%20%7C%20IBGE-,Síntese%20de%20Indicadores%20Sociais%3A%20em%202019%2C%20proporção%20de%20pobres%20cai,em%206%2C5%25%20da%20população
# 
# -------------------------

# #### Estimativa de População Real de Consumidores
# 
# 1-) Para chegarmos a um valor de consumidores mais ideal dentro da possível realidade, vamos somar o total de dados considerados inválidos para nosso estudo e armazená-lo na variável <span style = "color: blue"> **PCI** </span> (população de consumidores inválidos):
# 
# ##### <center><span style = "color: blue"> PCI = CB + PNPD + PEP </span></center>
# 
# 
# ##### <center><span style = "color: blue"> PCI = </span><span style = "color: red">44.804.772,75 </center>
# 

# In[58]:


PCI = CB + PNPD + PEP
print("%.2f" % PCI)


# In[85]:


data = {
    'Nome Variável': ['CB', 'PNPD', 'PEP', 'PCI'],
    'População Inválida': ['Crianças Brasileiras', 'Não Possuem Dente', 'Extrema Pobreza','Total População Inválida'],
    'Total': ["%.2f" % CB, "%.2f" % PNPD, "%.2f" % PEP, "%.2f" % PCI]}

df = pd.DataFrame(data, columns=['Nome Variável','População Inválida','Total'])

df


# 2-) Em seguida realizamos o cálculo para retirar da População Geral (PG) o total de População de Consumidores Inválidos (PCI) e armazenamos esse valor na váriavel <span style = "color: blue"> **PCV** </span>:
# 
# ##### <center><span style = "color: blue"> PCV = PGB - PCI </span></center>
# 
# 
# ##### <center><span style = "color: blue"> PCV = </span><span style = "color: red">168.563.914,25 </center>
# 

# In[97]:


PCV = PGB - PCI
print("%.2f" % PCV)


# In[107]:


data = {
    'Nome Variável': ['PGB', 'PCI', 'PCV'],
    'População': ['População Geral','População Inválida', 'Consumidores Válidos'],
    'Total': ["%.2f" % PGB, "%.2f" % PCI, "%.2f" %PCV ]}

dfg = pd.DataFrame(data, columns=['Nome Variável','População', 'Total'])

dfg


# In[ ]:





# --------------------------------

# # <center>Etapa 3 - Média de Consumo Diário e Mensal Individual </center>

# ## Média de Consumo Diário
# 
# Nesta etapa, precisamos descobrir a média de consumo diário de pastas de dente usadas pelos consumidores. 
# 
# A princípio pensaremos no consumo diário de um único consumidor!
# 
# Vamos utilizar como requisito de parâmetros as informações sugeridas pelo **Conselho Federal de Odontologia** que são:
# 
# - Número ideal de escovação diária é de pelo menos 4 vezes ao dia.
# 
# - Quantidade média ideal de creme dental recomendada em cada escovação é de 2 gramas.
# 
# 
# Logo obtemos o seguinte cáculo:
# 
# ##### <center style = "color: red" >4 x 2g = 8g</center>
# 
# Vamos armazenar esse valor numa variável chamada <span style = "color: blue">**MD**</span> (crianças brasileiras):
# 
# 
# ##### <center><span style = "color: blue"> MD = </span><span style = "color: red">8g </center>
# 
# -------------

# In[12]:


MD = 4 * 2
print(MD)


# ## Média de Consumo Mensal
# 
# Para chegar a esse valor precisamos multiplicar a média de consumo diário (MD) pelo total de dias do mês.
# 
# A princípio pensaremos no consumo mensal de um único consumidor!
# 
# Vamos armazenar esse resultado na variável <span style = "color: blue"> **MM** </span>.
# 
# - Para caráter didático, vamos considerar o mês com 30 dias.
# 
# ##### <center><span style = "color: blue"> MM = MD x </span><span style = "color: red">30</span> </center>
# 
# ##### <center><span style = "color: blue"> MM = </span><span style = "color: red"> 240g </span></center>
# 

# In[13]:


MM = MD * 30
print(MM)


# # Etapa 4 - Média de Consumo Mensal Total

# Agora que obtivemos a média mensal <span style = "color: blue">MM</span> de consumo por individuo, temos que calcular a média mensal pelo total de consumidores <span style = "color: blue">PCV</span>.
# 
# - Lembrando que o valor das variáveis MM e CMT terão a unidade de medida em gramas
# 
# 
# - Iremos armazenar o resultado na variável <span style = "color: blue">CMT</span> (Consumo Mensal Total)
# 
# ##### <center><span style = "color: blue">CMT = MM x PCV</span></center>
# 
# ##### <center><span style = "color: blue"> CMT = </span><span style = "color: red"> 40.455.339.421,20g </span></center>
# 

# In[14]:


CMT = MM * PCV
print(CMT)


# ## Conversão de valor de variável CMT para de gramas para kilos.

# Para melhor compreensão do resultado da case vamos converter o valor do Consumo Mensal Total <span style = "color: blue">**CMT**</span> de gramas para kilos:
# 
# - Iremos armazenar o resultado na variável <span style = "color: blue">CMK</span> (Consumo Mensal Kilos)
# 
# ##### <center><span style = "color: blue">CMK = CMT / 100</span></center>
# 
# ##### <center><span style = "color: blue"> CMK = </span><span style = "color: red"> 40.455.339,42k </span></center>
# 
# 

# In[17]:


CMK = CMT / 1000
print("%.2f" % CMK)


# # Etapa 5 - Conclusão do Estudo

# 
# 
# Baseado nos estudos realizados acima, podemos concluir que aproximadamente <span style = "color: red">40.455.339,42</span> de kilos pastas dentais são vendidas no Brasil por mês.
# 
# 
# É importante salientar que devido a fatores de demanda de mercado, sempre serão produzidos pela indústria uma quantidade maior do kilos do produto de pasta de dente que se pode consumir ou vender mensalmente. 
# 
# 
# Finalmente para presumir valores mais assertivos de vendas deste produto, seria necessário realizar um estudo com mais tempo para pesquisa em campo com consumidores ou com fontes da indústria de cremes dentais.
# 
