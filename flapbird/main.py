import pygame # indica que utilizaremos pygame
from scripts.cenas import Partida
from scripts.cenas import Menu
# from scripts.jogador import Jogador
# from scripts.cano import Cano

pygame.init() # inicia o pygame

tamanhoTela = [600,400] # define o tamanho da janela do jogo
tela = pygame.display.set_mode(tamanhoTela) #cria a janela que utilizaremos
pygame.display.set_caption("FlappyBird bb") #define o titulo da janela
relogio = pygame.time.Clock() # cria um relogio para controlar a velocidade do jogo
corFundo = (28, 70, 87) # cria uma cor de fundo em formato RGB
# jog = Jogador(tela,100, 100)
# cano = Cano(tela)

listaCenas = {
    'partida': Partida(tela),
    'menu' : Menu(tela)
}

cenaAtual = 'menu'

while True: # cria um laço infinito para manter o jogo aberto
    for e in pygame.event.get(): # laço que passa em cada evento do pygame
        if e.type == pygame.QUIT: # verifica se é do tipo sair; que ocorre quando fecha a tela
            pygame.quit() # finaliza o pygame
    tela.fill(corFundo) # pinta a tela de fundo

    cenaAtual = listaCenas[cenaAtual].atualizar()

    # jog.atualizar()
    # jog.desenhar()
    # cano.atualizar()
    # cano.desenhar()

    relogio.tick(60) #controla a tela para atualizar 60 vezes por segundo
    pygame.display.flip() # atualiza a tela, mostrando as alterações feitas