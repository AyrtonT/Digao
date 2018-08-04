
# coding: utf-8

# Programa Copa do Mundo com Pandas
# versão: 1.0
# revisão: 0
# data: 2018-08-04
# 

# In[97]:


import requests
import pandas as pd

g = [['RUS', 'KSA', 'EGY', 'URU'], ['MAR', 'IRN', 'POR', 'ESP'], ['FRA', 'AUS', 'PER', 'DEN'], ['ARG', 'ISL', 'CRO', 'NGA'], ['BRA', 'SUI', 'CRC', 'SRB'], ['SWE', 'MEX', 'GER', 'KOR'], ['ENG', 'PAN', 'BEL', 'TUN'], ['JPN', 'SEN', 'POL', 'COL']]
e = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
cod = 1

jogos = pd.read_json('https://t.co/5kiIGpo1vg', orient='columns')


def transf_pd(table, data):
    a = table.loc[:,data]
    lista = []
    for i in a:
        lista.append(i)
    return pd.DataFrame(lista)


away_pd = transf_pd(jogos,'away_team')
home_pd = transf_pd(jogos,'home_team')


def grupo(grupo):
    global cod
    print('Grupo', e[grupo])
    print(f" {'ID'} {'Data'}        {'Hora'}   {'Score'}           {'Estádio'}")
    for cont in range(0,63):
        if home_pd.loc[cont,'code'] in g[grupo] and jogos.loc[cont,'stage_name'] == 'First stage':
            data = str(jogos.loc[cont, 'datetime'])
            print(f' {cod:>2} {data[:11]} {data[11:16]}', end="")
            print(' ', home_pd.loc[cont, 'code'], home_pd.loc[cont, 'goals'], 'x', away_pd.loc[cont, 'goals'], away_pd.loc[cont, 'code'], end="   ")
            print(jogos.loc[cont, 'location'])
            cod += 1
        cont += 1
    print()
 

def mata(fase):
    global cod
    print(fase)
    print(f" {'ID'} {'Data'}        {'Hora'}   {'Score'}          {'Penaltis'}  {'Estádio'}")
    for cont in range(0,64):
        if jogos.loc[cont,'stage_name'] == fase:
            data = str(jogos.loc[cont, 'datetime'])
            print('', cod, data[:11], data[11:16], end="")
            if home_pd.loc[cont, 'goals'] == away_pd.loc[cont, 'goals']:
                print(' ', home_pd.loc[cont, 'code'], home_pd.loc[cont, 'goals'], 'x', away_pd.loc[cont, 'goals'], away_pd.loc[cont, 'code'], '(', home_pd.loc[cont, 'penalties'],'x',away_pd.loc[cont, 'penalties'],')', end="  ")
            else:
                print(' ', home_pd.loc[cont, 'code'], home_pd.loc[cont, 'goals'], 'x', away_pd.loc[cont, 'goals'], away_pd.loc[cont, 'code'], end="            ")
            print(jogos.loc[cont, 'location'])
            cod += 1
        cont += 1
    print()
    
            
for i in range(0, 7):
    grupo(i)

mata('Round of 16')
mata('Quarter-finals')
mata('Semi-finals')
mata('Play-off for third place')
mata('Final')

