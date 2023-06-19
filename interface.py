import matplotlib.pyplot as plt

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
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')

    # Inicializa os pontos com as coordenadas iniciais
    pontos = ax.scatter(x_inicial, y_inicial)

    # Mostra o gráfico
    plt.grid(True)
    plt.ion()  # Ativa o modo de atualização interativa

    # Atualiza os pontos até que alcancem as coordenadas finais
    while x_inicial != x_final or y_inicial != y_final:
        # Atualiza as coordenadas iniciais para cada ponto
        for i in range(len(coordenadas_iniciais)):
            if x_inicial[i] < x_final[i]:
                x_inicial[i] += 1
            elif x_inicial[i] > x_final[i]:
                x_inicial[i] -= 1

            if y_inicial[i] < y_final[i]:
                y_inicial[i] += 1
            elif y_inicial[i] > y_final[i]:
                y_inicial[i] -= 1

        # Atualiza as coordenadas dos pontos no gráfico
        pontos.set_offsets(list(zip(x_inicial, y_inicial)))

        # Força a atualização do gráfico
        plt.draw()
        plt.pause(0.1)  # Pausa para permitir a visualização das alterações

    plt.ioff()  # Desativa o modo de atualização interativa
    plt.show()


# Exemplo de utilização
coordenadas_iniciais = [(-74.0060, 40.7128), (-118.2437, 34.0522), (-0.1278, 51.5074), (151.2093, -33.8688)]
coordenadas_finais = [(-0.1278, 51.5074), (139.6917, 35.6895), (37.6176, 55.7558), (-43.1729, -22.9068)]
gerar_plano_cartesiano(coordenadas_iniciais, coordenadas_finais)
