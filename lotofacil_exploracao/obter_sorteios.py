import re
import sqlite3
import requests
import pandas as pd
from bs4 import BeautifulSoup

conn = sqlite3.connect('./dados/lotofacil.db')

response = requests.get(url='https://asloterias.com.br/lista-de-resultados-da-lotofacil')

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Texto (com as tags HTML).
    texto = str(soup).strip()
    
    # Expressão Regular.
    padrao = r'<strong>(\d+)<\/strong>\s*-\s*(\d{2}\/\d{2}\/\d{4})\s*-\s*((?:\d+\s+)+\d+)'

    # Obtenção das correspondências.
    correspondencias = re.findall(padrao, texto)

    dados = []

    for correspondencia in correspondencias:
        # Número do sorteio.
        numero_sorteio = correspondencia[0]
        # Data do sorteio.
        data_sorteio = correspondencia[1]
        # Lista com os números sorteados.
        numeros_sorteados = correspondencia[2].split(' ')

        print(f'numero_sorteio: {numero_sorteio}')
        print(f'data_sorteio: {data_sorteio}')
        print(f'numeros_sorteados: {numeros_sorteados}')
        
        # Obtenção dos números sorteados. Da bola 1 até a 15.
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
        
        # Montagem dos dados.
        dados.append({
            'numero_sorteio': numero_sorteio,
            'data_sorteio': data_sorteio,
            'bola1': bola1,
            'bola2': bola2,
            'bola3': bola3,
            'bola4': bola4,
            'bola5': bola5,
            'bola6': bola6,
            'bola7': bola7,
            'bola8': bola8,
            'bola9': bola9,
            'bola10': bola10,
            'bola11': bola11,
            'bola12': bola12,
            'bola13': bola13,
            'bola14': bola14,
            'bola15': bola15,
        })

        print(100 * '-')
    
    # Obtenção do DataFrame a partir dos dados.
    df = pd.DataFrame(dados)
    print(df)

    # Salva o DataFrame na tabela resultados do banco de dados.
    df.to_sql('resultados', conn, if_exists='replace')

    print(f'Fim da extração dos resultados.')