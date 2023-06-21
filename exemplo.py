from distancia_pontos import Point
from distancia_pontos import closest

# Cria uma array de tuplas
data = [(4, 2), (6, 9), (7, 5), (0, 10), (8, 3)]


# converte o array de tuplas em um array de pontos
data = Point.from_tuples(data)

# Aplica o algoritmo de menor distancia entre os pontos 

distancia_minima, pontos_minimos = closest(data, len(data))
ponto1, ponto2 = pontos_minimos
print("Distância mínima:", distancia_minima)
print("Pontos com distância mínima:", ponto1, ponto2)