import re
import requests
from bs4 import BeautifulSoup

# https://asloterias.com.br/lista-de-resultados-da-lotofacil

response = requests.get(url='https://asloterias.com.br/lista-de-resultados-da-lotofacil')

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    texto = str(soup).strip()

    padrao = r'<strong>(\d+)<\/strong>\s*-\s*(\d{2}\/\d{2}\/\d{4})\s*-\s*((?:\d+\s+)+\d+)'
    correspondencias = re.findall(padrao, texto)

    for correspondencia in correspondencias:
        numero_sorteio = correspondencia[0]
        data_sorteio = correspondencia[1]
        numeros_sorteados = correspondencia[2].split(' ')

        print(f'numero_sorteio: {numero_sorteio}')
        print(f'data_sorteio: {data_sorteio}')
        print(f'numeros_sorteados: {numeros_sorteados}')
        
        bola1 = numeros_sorteados[0]
        bola2 = numeros_sorteados[1]
        bola3 = numeros_sorteados[2]
        bola4 = numeros_sorteados[3]
        bola5 = numeros_sorteados[4]
        bola6 = numeros_sorteados[5]
        bola7 = numeros_sorteados[6]
        bola8 = numeros_sorteados[7]
        bola9 = numeros_sorteados[8]
        bola10 = numeros_sorteados[9]
        bola11 = numeros_sorteados[10]
        bola12 = numeros_sorteados[11]
        bola13 = numeros_sorteados[12]
        bola14 = numeros_sorteados[13]
        bola15 = numeros_sorteados[14]

        print(100 * '-')

