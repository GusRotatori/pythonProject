import pygame
import os

# Configurações do jogo
largura_tela = 640
altura_tela = 480
titulo_tela = "Jogo de Cavaleiro Medieval"
caminho_projeto = os.path.dirname(os.path.abspath(__file__))  # Diretório do projeto
caminho_imagens = os.path.join(caminho_projeto, "imagens")  # Caminho para a pasta de imagens
FPS = 60

# Inicialização do Pygame
pygame.init()
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption(titulo_tela)
clock = pygame.time.Clock()

# Carregamento de imagens
cavaleiro_imagem = pygame.image.load(os.path.join(caminho_imagens, 'cavaleiro.png'))
cavaleiro_imagem = pygame.transform.scale(cavaleiro_imagem, (64, 64))
cavaleiro_rect = cavaleiro_imagem.get_rect()
cavaleiro_rect.centerx = largura_tela // 2
cavaleiro_rect.bottom = altura_tela - 20

# Loop principal do jogo
while True:
    # Lidar com eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualizar lógica do jogo

    # Renderizar tela
    tela.fill((0, 0, 0))
    tela.blit(cavaleiro_imagem, cavaleiro_rect)
    pygame.display.flip()
    clock.tick(FPS)
