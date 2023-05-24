import requests
from time import sleep
import pandas as pd
from IPython.display import display

cep = str(input('Digite seu cep>. '))
print('Carregando..')
sleep(1)

if len(cep) == 8:
    link = f"https://viacep.com.br/ws/{cep}/json/"

    requisicao = requests.get(link)
    print(f'Status Code: {requisicao}')

    dic_requisicao = requisicao.json()
    
    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    bairro = dic_requisicao['bairro']
    rua = dic_requisicao['logradouro']
    lis = {'Estado':uf,'Cidade':cidade,'Bairro':bairro ,'Rua':rua}
    
else:
    print('CEP INVALIDO')

display(lis)