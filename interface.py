import matplotlib.pyplot as plt
from teste import le_csv
from distancia_pontos import closest
import distancia_pontos
from itera_points import itera_Points

########################### cordenadas #####################

cordenadas_inicias = [(40.7128, -74.0060),(34.0522, -118.2437),(-33.8688, 151.2093),(19.0760, 72.8777),(37.7749, -122.4194),(55.7558, 37.6176),(-22.9068, -43.1729),(51.5074, -0.1278),(37.9838, 23.7275),(32.7767, -96.7970),(28.6139, 77.2090),(-34.6037, -58.3816),(-33.4489, 70.6693),(41.9028, 12.4964),(25.2048, 55.2708),(35.6895, 139.6917),(48.8566, 2.3522)]
cordenadas_finais = tabela = [(51.5074, -0.1278),(35.6895, 139.6917),(55.7558, 37.6176),(-22.9068, -43.1729),(22.5726, 88.3639),(39.9042, 116.4074),(48.8566, 2.3522),(-34.6037, -58.3816),(52.5200, 13.4050),(41.9028, 12.4964),(19.4326, -99.1332),(31.5204, 74.3587),(-12.0464, -77.0428),(-22.9068, -43.1729),( 33.6844, 73.0479),(51.5074, -0.1278),(40.7128, -74.0060),(22.5726, 88.3639),(40.7128, -74.0060),( 37.7749, -122.4194)]


 

cordenadas_inicias = [(int(x), int(y)) for x, y in cordenadas_inicias]
cordenadas_finais = [(int(x), int(y)) for x, y in cordenadas_finais]

# converte as cordenadas em array de tuplas para points

pontos_inicias = distancia_pontos.Point.from_tuples(cordenadas_inicias)
pontos_finais = distancia_pontos.Point.from_tuples(cordenadas_finais)


def gerar_plano_cartesiano(coordenadas_iniciais, coordenadas_finais):
    # Extrai as coordenadas iniciais x e y do array
    x_inicial = [coordenada[0] for coordenada in coordenadas_iniciais]
    y_inicial = [coordenada[1] for coordenada in coordenadas_iniciais]

    # Extrai as coordenadas finais x e y do array
    x_final = [coordenada[0] for coordenada in coordenadas_finais]
    y_final = [coordenada[1] for coordenada in coordenadas_finais]

    # Cria um novo gráfico
    fig, ax = plt.subplots()

    # Configura os limites dos eixos
    ax.set_xlim(min(x_inicial + x_final) - 1, max(x_inicial + x_final) + 1)
    ax.set_ylim(min(y_inicial + y_final) - 1, max(y_inicial + y_final) + 1)

    # Configura os rótulos dos eixos
    ax.set_xlabel('latitude ')
    ax.set_ylabel('Longitude ')

    # Inicializa os pontos com as coordenadas iniciais
    pontos = ax.scatter(x_inicial, y_inicial)

    # Mostra o gráfico
    plt.grid(True)
    plt.ion()  # Ativa o modo de atualização interativa
    tamanho = len(coordenadas_iniciais)

    # Atualiza os pontos até que alcancem as coordenadas finais
    while x_inicial != x_final or y_inicial != y_final:
        # Atualiza as coordenadas iniciais para cada ponto
        i = 0
        while i < tamanho:
            if x_inicial[i] < x_final[i]:
                x_inicial[i] += 1
            elif x_inicial[i] > x_final[i]:
                x_inicial[i] -= 1

            if y_inicial[i] < y_final[i]:
                y_inicial[i] += 1
            elif y_inicial[i] > y_final[i]:
                y_inicial[i] -= 1

            if (x_inicial[i] >= x_final[i]-1 and x_inicial[i] <= x_final[i]+1):
                if (y_inicial[i] >= y_final[i]-1 and y_inicial[i] <= y_final[i]+1):
                    x_final.pop(i)
                    x_inicial.pop(i)
                    y_inicial.pop(i)
                    y_final.pop(i)
                    tamanho-=1
            
            moved = itera_Points(pontos_inicias, pontos_finais)

            distancia_minima, pontos_minimos = closest(moved, len(moved))
            ponto1, ponto2 = pontos_minimos
            print("menor distancia: ",distancia_minima)

            i+=1

        
            # Atualiza as coordenadas dos pontos no gráfico
        if len(x_inicial)>0 and len(y_inicial)>0:
            plt.plot([ponto1.x, ponto2.x], [ponto1.y, ponto2.y], 'b-')
            plt.text((ponto1.x + ponto2.x) / 2, (ponto1.y + ponto2.y) / 2, str(distancia_minima), ha='center', va='bottom')
            plt.scatter([ponto1.x, ponto2.x], [ponto1.y, ponto2.y], color='green')
            pontos.set_offsets(list(zip(x_inicial, y_inicial)))


        # Força a atualização do gráfico
        plt.draw()
        plt.pause(0.1)  # Pausa para permitir a visualização das alterações

    plt.ioff()  # Desativa o modo de atualização interativa
    plt.show()

gerar_plano_cartesiano(cordenadas_inicias,cordenadas_finais)


