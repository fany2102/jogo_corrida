import random
import time

# Função para mover o jogador
def mover_jogador(nome, posicao):
    movimento = random.randint(1, 6)  # Simulando o lançamento de um dado (movimento entre 1 e 6)
    posicao += movimento
    print(f"{nome} avançou {movimento} casas. Posição atual: {posicao}")
    return posicao

# Função para iniciar o jogo
def jogo_corrida():
    jogadores = ['Jogador 1', 'Jogador 2']  # Lista de jogadores
    posicoes = [0, 0]  # Posições iniciais dos jogadores

    vencedor = None
    while vencedor is None:
        for i in range(len(jogadores)):
            print(f"\nÉ a vez de {jogadores[i]}")
            time.sleep(1)
            posicoes[i] = mover_jogador(jogadores[i], posicoes[i])
            if posicoes[i] >= 30:  # Objetivo do jogo: chegar à casa 30
                vencedor = jogadores[i]
                print(f"\n{vencedor} venceu a corrida!")
                break
            time.sleep(1)

# Rodar o jogo
if __name__ == "__main__":
    jogo_corrida()
