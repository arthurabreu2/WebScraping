from config import URL, URL_BASE
import requests
from bs4 import BeautifulSoup
import csv


paginas = []

# Criando um arquivo csv para gravar todas as informações
arquivo_csv = csv.writer(open('nomes_artistas_z.csv', 'w', newline='\n'))
arquivo_csv.writerow(['Nomes_Artistas', 'URL_Artistas'])

for num_page in range(1, 5):
    paginas.append(f"https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ{num_page}.htm")


for url_por_pagina in paginas:
    pagina = requests.get(url_por_pagina)
    soup = BeautifulSoup(pagina.text, 'html.parser')
    # Remover links inferiores
    ultimos_links = soup.find(class_='AlphaNav')
    ultimos_links.decompose()
    # Pegar o conteudo da bodytext
    bloco_nome_artista = soup.find(class_='BodyText')
    lista_nome_artistas = bloco_nome_artista.find_all('a')

    for nome_artista in lista_nome_artistas:
        nomes = nome_artista.contents[0]
        links = f"{URL_BASE}{nome_artista.get('href')}"
        arquivo_csv.writerow([nomes, links])
        print(nomes)
        print(links)





