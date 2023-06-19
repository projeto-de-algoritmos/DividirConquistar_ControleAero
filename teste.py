import distancia_pontos
from distancia_pontos import Point
import pandas as pd

def le_csv():
    df = pd.read_csv("voos.csv")
    df = df.reset_index()

    ponto = []

    for x, y, z in zip(df['latitude_partida'], df['longitude_partida'], df['numero_voo']):
        ponto.append([x, y, z])

    pontos = []

    for i in ponto:
        pont = Point(x = i[0], y = i[1], voo = i[2])
        pontos.append(pont)

    return pontos