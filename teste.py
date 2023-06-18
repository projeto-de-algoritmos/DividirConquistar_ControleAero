import distancia_pontos
from distancia_pontos import Point
import pandas as pd

def main():
    df = pd.read_csv("voos.csv")
    df = df.reset_index()

    ponto = []

    count = 0

    for x, y, z in zip(df['latitude_partida'], df['longitude_partida'], df['numero_voo']):
        ponto[count] == [x, y, z]

    pontos = []

    for i in ponto:
        pont = Point(i)
        pontos.append(pont)

    n = len(pontos)

    print(distancia_pontos.closest(pontos, n))

main()