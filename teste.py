import distancia_pontos
from distancia_pontos import Point
import pandas as pd

def le_csv():
    df = pd.read_csv("voos.csv")
    df = df.reset_index()

    ponto = []
    voos = []

    for x, y, z in zip(df['latitude_partida'], df['longitude_partida'], df['numero_voo']):
        ponto.append((x, y))
        voos.append(z)

    destinos = []

    for x, y in zip(df['latitude_destino'], df['longitude_destino']):
        destinos.append((x, y))

    return ponto, destinos, voos