import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
LARGURA_TELA = 600
ALTURA_TELA = 700
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Jogo de Carro")

# Cores
COR_FUNDO = (100, 100, 100)
COR_CARRO = (0, 255, 0)
COR_OBSTACULO = (255, 0, 0)

# Configurações do carro
LARGURA_CARRO = 50
ALTURA_CARRO = 90
posicao_carro_x = LARGURA_TELA // 2 - LARGURA_CARRO // 2
posicao_carro_y = ALTURA_TELA - ALTURA_CARRO - 20
velocidade_carro = 5

# Configurações do obstáculo
LARGURA_OBSTACULO = 50
ALTURA_OBSTACULO = 90
velocidade_obstaculo = 7
obstaculos = []

# Função para criar um obstáculo
def criar_obstaculo():
    x = random.randint(0, LARGURA_TELA - LARGURA_OBSTACULO)
    y = -ALTURA_OBSTACULO
    obstaculos.append(pygame.Rect(x, y, LARGURA_OBSTACULO, ALTURA_OBSTACULO))

# Variáveis de controle do jogo
clock = pygame.time.Clock()
pontuacao = 0
jogando = True

# Loop do jogo
while jogando:
    tela.fill(COR_FUNDO)
    
    # Verificar eventos do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False

    # Movimento do carro
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and posicao_carro_x > 0:
        posicao_carro_x -= velocidade_carro
    if teclas[pygame.K_RIGHT] and posicao_carro_x < LARGURA_TELA - LARGURA_CARRO:
        posicao_carro_x += velocidade_carro

    # Criar e movimentar obstáculos
    if random.randint(1, 60) == 1:
        criar_obstaculo()
    for obstaculo in obstaculos:
        obstaculo.y += velocidade_obstaculo
        if obstaculo.y > ALTURA_TELA:
            obstaculos.remove(obstaculo)
            pontuacao += 1
        if obstaculo.colliderect((posicao_carro_x, posicao_carro_y, LARGURA_CARRO, ALTURA_CARRO)):
            jogando = False

    # Desenhar carro e obstáculos
    pygame.draw.rect(tela, COR_CARRO, (posicao_carro_x, posicao_carro_y, LARGURA_CARRO, ALTURA_CARRO))
    for obstaculo in obstaculos:
        pygame.draw.rect(tela, COR_OBSTACULO, obstaculo)

    # Mostrar pontuação
    fonte = pygame.font.Font(None, 36)
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, (255, 255, 255))
    tela.blit(texto_pontuacao, (10, 10))

    # Atualizar tela e configurar FPS
    pygame.display.flip()
    clock.tick(60)

# Encerrar o jogo
pygame.quit()