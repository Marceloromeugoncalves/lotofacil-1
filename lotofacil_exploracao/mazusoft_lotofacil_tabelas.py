"""
import requests
from bs4 import BeautifulSoup

# Fazer a requisição HTTP
url = "https://www.exemplo.com"
response = requests.get(url)

# Parsear o conteúdo HTML
soup = BeautifulSoup(response.content, "html.parser")

# Encontrar todos os elementos de âncoras (links)
links = soup.find_all("a")

# Extrair o texto e a URL de cada link
for link in links:
    texto = link.text
    url = link["href"]
    print("Texto: ", texto)
    print("URL: ", url)
    print()
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = 'https://www.mazusoft.com.br/lotofacil/tabelas.php'

response = requests.get(url=URL)

# Parsear o conteúdo HTML.
soup = BeautifulSoup(response.content, 'html.parser')

# icon-lf
li_list = soup.find_all('li', class_='icon-lf')

dados = []

for li in li_list:
    link = li.find('a')

    texto = link.text
    url = f"https://www.mazusoft.com.br/lotofacil/{link['href']}"

    print(f'texto: {texto}')
    print(f'url: {url}')

    dados.append({'texto': texto, 'url': url})

    df = pd.DataFrame(dados)
    print(df)

    df.to_excel('./dados/tabelas.xlsx')

