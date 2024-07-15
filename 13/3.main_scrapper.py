import os
import re
import logging
from datetime import datetime
import requests # http, apis
from bs4 import BeautifulSoup # html 

def extract_links(html_content, expresion):
    content_soup = BeautifulSoup(html_content, "html.parser")
    links = []
    
    for link in content_soup.find_all("a", href=expresion):
        links.append(link.get("href"))
    
    return links


def download_html(url, page_folder):
    response = requests.get(url)
    html_content = response.content # genera un html con la response.content
    
    if not os.path.exists(page_folder): # si no existe la carpeta, la crea
        os.mkdir(page_folder)
        
    filename = f"{page_folder}.html"    # nombre del archivo

    path = f"{page_folder}/{filename}"  # nombre del path
    # wb -> write and binary
    with open(path, "wb") as file:  # escribe en el archivo todo el html del principio
        file.write(html_content)
    
    return html_content # retorna el contenido html para ser iterado
    
    
def download_files(links, folder, url):
    if links:   # si links tiene al menos 1 link
        for link in links:
            try:
                r = requests.get(link)
                name = link.split("/")[-1]
                path = f"{folder}/{name}"

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
        
        
def main():
    url = "https://datos.gob.ar/dataset/energia-precios-gas-natural"
    page_folder = url.split("/")[-1]    # nombre de la folder
    logging.basicConfig(filename=f"{page_folder}.log", level=logging.INFO)  # configuracion de log básica
    
    try:
        html_content = download_html(url, page_folder)
        # genero lista de links
        expresion = re.compile(r"\.(csv|xlsx|xls)$")
        links = extract_links(html_content, expresion)
        download_files(links, page_folder, url)
    except Exception as e:   # porque no sabemos qué excepciones pueden haber
        logging.error(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Error: {e}")
        
if __name__ == "__main__":   # normativa para correr main() en py
    main()