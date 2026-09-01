import pygame
from scripts.cano import Cano
from scripts.jogador import Jogador
from scripts.interfaces import Texto #Importando texto
from scripts.interfaces import Botao



class Partida:

    def __init__(self, tela):
        self.tela = tela
        self.jogador = Jogador(tela, 100, 100)
        self.cano = Cano(tela)
        self.estado = "partida"

        self.pontosValor = 0 #valor dos pontos
        self.contador = 0   #o contador que subirá os pontos
        self.pontosTexto = Texto(tela,str(self.pontosValor),10,10,(255,255,255),30) #em texto

    def atualizar(self):
        self.estado = 'partida'
        self.jogador.atualizar()
        self.cano.atualizar()

        #contador de pontos
        self.contador +=1
        if self.contador > 60:
            self.pontosValor += 1
            self.contador = 0
            self.pontosTexto.atualizarTexto(str(self.pontosValor))
        #desenhando os pontos
        self.pontosTexto.desenhar()

        if self.cano.detectarColisao(self.jogador.getRect()):
            self.estado = "menu"
            self.jogador.posicao = (100,100)
            self.cano.x = self.tela.get_width()
            #zerando os pontos
            self.pontosValor = 0
        self.jogador.desenhar()
        self.cano.desenhar()

        return self.estado

class Menu:
    def __init__(self,tela):
        self.tela = tela
        self.titulo = Texto(tela,"FlappyBird",100,20,(255,255,255),50)
        self.estado = "menu" #estado atual da partida, indicando se está no jogo ou se perdeu
        self.botao_jogador = Botao(tela, "jogar",100,100,50,(200,0,0),(255,255,255))

    def atualizar(self):
        self.estado = "menu" #redefinimos todo o estado para "partida" a cada atualização
        self.titulo.desenhar()
        self.botao_jogador.desenhar()

        if self.botao_jogador.get_click():
            self.estado = "partida"

        return self.estado