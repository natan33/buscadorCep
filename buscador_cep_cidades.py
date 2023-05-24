import requests
import openpyxl
import pandas as pd 
from IPython.display import display
from time import sleep

uf = str(input('UF >. '))
cidade = str(input('Cidade>.'))
endereco = str(input('Endereço>. '))
print('Carregando...')
sleep(1)

link = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'

requisicao = requests.get(link)
print(f"Statuc Code: {requisicao}")

dic_requisicao = requisicao.json()
#print(dic_requisicao)

tabela = pd.DataFrame(dic_requisicao)
display(tabela)
tabela.to_csv('endereco_completo.csv')


