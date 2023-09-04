import pygame
import random

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da janela
largura = 800
altura = 600

# Criar a janela do jogo
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Labirinto")

# Definir as cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Definir as dimensões dos blocos
bloco_largura = 40
bloco_altura = 40

# Definir as dimensões do labirinto
labirinto_largura = largura // bloco_largura
labirinto_altura = altura // bloco_altura

# Gerar o labirinto aleatório
def gerar_labirinto():
    labirinto = []
    for i in range(labirinto_altura):
        linha = []
        for j in range(labirinto_largura):
            linha.append(random.choice([0, 1]))
        labirinto.append(linha)
    labirinto[0][0] = 0
    labirinto[labirinto_altura-1][labirinto_largura-1] = 0
    return labirinto

# Desenhar o labirinto na tela
def desenhar_labirinto(labirinto):
    for i in range(labirinto_altura):
        for j in range(labirinto_largura):
            x = j * bloco_largura
            y = i * bloco_altura
            cor = branco if labirinto[i][j] == 0 else preto
            pygame.draw.rect(janela, cor, [x, y, bloco_largura, bloco_altura])

# Executar o jogo
def executar_jogo():
    labirinto = gerar_labirinto()
    jogador_posicao = [0, 0]

    while True:
        # Lidar com eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Desenhar o labirinto e o jogador na tela
        janela.fill(branco)
        desenhar_labirinto(labirinto)
        x = jogador_posicao[1] * bloco_largura
        y = jogador_posicao[0] * bloco_altura
        pygame.draw.rect(janela, (255, 0, 0), [x, y, bloco_largura, bloco_altura])

        # Atualizar a tela
        pygame.display.update()

# Executar o jogo
executar_jogo()