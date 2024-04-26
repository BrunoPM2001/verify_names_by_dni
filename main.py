# Libs
import argparse
import requests as r
from bs4 import BeautifulSoup

# Argumentos
parser = argparse.ArgumentParser(description='Script para obtener nombres, apellido paterno y materno en base a un n° de DNI')
parser.add_argument('-dni', type=str, help='N° de DNI (8 dígitos)')
args = parser.parse_args()

# Obtención de cookies
s = r.Session()
res1 = s.get("https://dni-peru.com/buscar-dni-nombres-apellidos/")

# Envío de información
res2 = s.post("https://dni-peru.com/buscar-dni-nombres-apellidos/", data = {'dni4': args.dni, 'buscar_dni':''})

# Obtención de variables
soup = BeautifulSoup(res2.text, 'html.parser')
div = soup.find('div', { 'id' : 'resultado_busqueda' })
datos = div.find_all('p', recursive=True)

bs_nombre = BeautifulSoup(str(datos[2]), 'html.parser')
p_nombre = bs_nombre.find('p')
nombre = ''.join(p_nombre.find_all(string=True, recursive=False))

bs_paterno = BeautifulSoup(str(datos[3]), 'html.parser')
p_paterno = bs_paterno.find('p')
paterno = ''.join(p_paterno.find_all(string=True, recursive=False))

bs_materno = BeautifulSoup(str(datos[4]), 'html.parser')
p_materno = bs_materno.find('p')
materno = ''.join(p_materno.find_all(string=True, recursive=False))

print("Nombres: ", nombre.strip())
print("Apellido paterno: ", paterno.strip())
print("Apellido materno: ", materno.strip())