import pygame
import constantes
import sprites
import os

class Game:
    def __init__(self):
        # criando a tela do jogo
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantes.LARGURA, constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_JOGO)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
        self.fonte = pygame.font.match_font(constantes.FONTE)
        self.carregar_arquivos()

    def novo_jogo(self):
        # instancia as classes das sprites do jogo
        self.todas_as_sprites = pygame.sprite.Group()
        self.rodar()

    def rodar(self):
        # loop do jogo
        self.jogando = True
        while self.jogando:
            self.relogio.tick(constantes.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        # define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.esta_rodando = False

    def atualizar_sprites(self):
        # atualiza as sprites
        self.todas_as_sprites.update()

    def desenhar_sprites(self):
        # desenha as sprites
        self.tela.fill(constantes.PRETO)
        self.todas_as_sprites.draw(self.tela)
        pygame.display.flip()

    def carregar_arquivos(self):
        # carrega os arquivos de audio e de imagem
        self.diretorio_bg = os.path.join(os.getcwd(), 'img', 'bg')
        self.diretorio_sprites = os.path.join(os.getcwd(), 'img', 'pokemon_parado')
        self.diretorio_movimento = os.path.join(os.getcwd(), 'img', 'pokemon_movimento')
        self.diretorio_mapas = os.path.join(os.getcwd(), 'img', 'mapas')
        self.diretorio_cries = os.path.join(os.getcwd(), 'som', 'cries')
        self.diretorio_efeitos = os.path.join(os.getcwd(), 'som', 'efeitos_gerais')
        self.diretorio_movesound = os.path.join(os.getcwd(), 'som', 'moves')
        self.diretorio_soundtrack = os.path.join(os.getcwd(), 'som', 'soundtrack')
        self.kanto_spritesheet = os.path.join(self.diretorio_sprites, constantes.KANTO_PARADO)
        self.kanto_movimento = os.path.join(self.diretorio_sprites, constantes.KANTO_MOVIMENTO)


    def mostrar_texto(self, texto, tamanho, cor, x, y):
        # exibe um texto na tela
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, False, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x, y)
        self.tela.blit(texto, texto_rect)

    def mostrar_tela_start(self):
        pygame.mixer.music.load(os.path.join(self.diretorio_soundtrack, '01 - Opening Movie.mp3'))
        pygame.mixer.music.play()
        self.mostrar_texto(
            'Pokémon Tower Defense',
            32,
            constantes.BRANCO,
            constantes.LARGURA / 2,
            constantes.ALTURA * 0.09
        )
        self.mostrar_texto(
            'Desenvolvido por Níkollas Antes',
            18,
            constantes.BRANCO,
            constantes.LARGURA / 2,
            constantes.ALTURA * 0.9
        )
        pygame.display.flip()
        self.esperar_musica()

    def esperar_musica(self):
        esperando_musica = True
        while esperando_musica:
            self.relogio.tick(constantes.FPS)
            if not pygame.mixer.music.get_busy():
                esperando_musica = False

    def esperar_comando(self):
        esperando_comando = True
        while esperando_comando:
            self.relogio.tick(constantes.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando_comando = False
                    self.esta_rodando = False
                if event.type == pygame.MOUSEBUTTONUP:
                    esperando_comando = False

    def mostrar_tela_game_over(self):
        pass

g = Game()
g.mostrar_tela_start()

while g.esta_rodando:
    g.novo_jogo()
    g.mostrar_tela_game_over()