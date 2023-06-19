import matplotlib.pyplot as plt
from teste import le_csv

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

            i+=1

        # Atualiza as coordenadas dos pontos no gráfico
        if len(x_inicial)>0 and len(y_inicial)>0:
            pontos.set_offsets(list(zip(x_inicial, y_inicial)))

        # Força a atualização do gráfico
        plt.draw()
        plt.pause(0.1)  # Pausa para permitir a visualização das alterações

    plt.ioff()  # Desativa o modo de atualização interativa
    plt.show()


# Exemplo de utilização
coordenadas_iniciais, coordenadas_finais, voos = le_csv()
gerar_plano_cartesiano(coordenadas_iniciais, coordenadas_finais)
