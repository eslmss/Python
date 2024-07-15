# incluidas python
import os
import re
import logging
from datetime import datetime
import requests # http, apis
from bs4 import BeautifulSoup # html 

#url = "https://datos.gob.ar/dataset/energia-precios-gas-natural"
url = "https://data.buenosaires.gob.ar/dataset/flujo-vehicular-anillo-digital"

response = requests.get(url)

html_content = response.content

page_folder = url.split("/")[-1]

if not os.path.exists(page_folder):
    os.mkdir(page_folder)

filename = f"{page_folder}.html"

path = f"{page_folder}/{filename}"

# wb -> write and binary
with open(path, "wb") as file:
    file.write(html_content)

logging.basicConfig(filename=f"{page_folder}.log", level=logging.INFO)

# creo una instancia del objeto BeautifulSoup
content_soup = BeautifulSoup(html_content, "html.parser")

# genero lista de links
links = []
expresion = re.compile(r"\.(csv|xlsx|xls)$")

for link in content_soup.find_all("a", href=expresion):

    links.append(link.get("href"))

# guardo los archivos

if links:

    for link in links:
        try:
            r = requests.get(link)

            name = link.split("/")[-1]

            path = f"{page_folder}/{name}"

            with open(path, "wb") as file:
                file.write(r.content)

            logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Archivo {name} se descargó correctamente de la web {url}")
        
        except requests.exceptions.HTTPError as e:
            logging.error(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -  No se pudo descargar el archivo {name} de la web {url}. Error: {e}")
            continue
        
        except Exception as e:
            logging.error(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -  No se pudo descargar el archivo {name} de la web {url}. Error: {e}")
            continue
else:
    logging.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - No hay archivos csv, xls o xlsx descargables en la web {url}")

