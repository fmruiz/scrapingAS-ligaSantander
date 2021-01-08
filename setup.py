import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.now()

h = {
    "user-agents":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

url = "https://resultados.as.com/resultados/futbol/primera/clasificacion/"

resp = requests.get(url, headers=h)

soup = BeautifulSoup(resp.content, "html.parser")

#EQUIPOS

eq = soup.find_all("span", class_="nombre-equipo")

teams = list()

count = 0

for e in eq:
    if count < 20:
        teams.append(e.text.replace("\n",""))
    else:
        break
    count += 1

#PUNTOS

point = soup.find_all("td", class_="destacado")

points = list()

count = 0

for p in point:
    if count < 20:
        points.append(p.text.replace("\n",""))
    else:
        break
    count += 1

#DATAFRAME

df = pd.DataFrame({"Equipos:":teams, "Puntos:":points}, index=range(1,21))
df.to_csv("./data.csv")

#CREANDO ARCHIVO .TXT

file = open("LaLiga-Santander.txt", "w")
file.write("TABLA DE POSICIONES LA LIGA SANTANDER - " + str(now.day) + "/" + str(now.month) + "/" + str(now.year) + "\n")
file.write(str(df) + "\n" + "\n" + "\n")
file.close()