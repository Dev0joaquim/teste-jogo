import pygame           # importa o estilo jogo do puthon
from random import randint  # importa o estilo aleatório

pygame.init()           # para iniciar o python
x = 30          # posição horizontal inicial do boneco, no caso, GOL
y = 250         # posição vertical inicial do boneco, no caso, GOL
pos_x = 1500            # posição horizontal inicial do boneco, no caso, AZUL
pos_y = 200         # posição vertical inicial do boneco, no caso, AZUL
posi_x = 1900           # posição horizontal inicial do boneco, no caso, LATAM
posi_y = 400            # posição vertical inicial do boneco, no caso, LATAM
position_x = -300           # posição horizontal inicial do boneco, no caso, AVIANCA
position_y = 510            # posição vertical inicial do boneco, no caso, AVIANCA

velocidade = 35         # velocidade do boneco GOL
velocidade_outros = 33          # velocidade dos outros bonecos


fundo = pygame.image.load('ceu.png')            # imagem de fundo
gol = pygame.image.load('gol1.png')         # imagem do boneco principal
azul = pygame.image.load('azulpequeno.png')         # imagem de outro boneco
latam = pygame.image.load('latampequeno.png')         # imagem de outro boneco
avianca = pygame.image.load('avianca.png')         # imagem de outro boneco
aireuropa = pygame.image.load('aireuropa.png')         # imagem de outro boneco

janela = pygame.display.set_mode((1300, 600))           # define a largura x altura da janela do jogo
pygame.display.set_caption("Criando um jogo com Python")            # acho que é o nome do jogo


janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)           # valor em milessegudos

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP] and y >= 0:
        y -= velocidade
    if comandos[pygame.K_DOWN] and y <= 520:
        y += velocidade
    if comandos[pygame.K_LEFT] and x >= 10:
        x -= velocidade
    if comandos[pygame.K_RIGHT] and x <= 1110:
        x += velocidade

    if (pos_x <= -300) and (posi_x <= -300) and (position_x > 1300):
        pos_x = randint(1400, 1500)
        posi_x = randint(1300, 1700)
        position_x = randint(-30, -10)
        pos_y = randint(0, 300)
        posi_y = randint(300, 400)
        position_y = randint(0, 560)

        if position_y + 50 >= pos_y and position_y + 50 >= posi_y:
            position_y + 50
        if position_y - 50 <= pos_y and position_y - 50 <= posi_y:
            position_y - 50

    pos_x -= velocidade_outros
    posi_x -= velocidade_outros +5
    position_x += velocidade -5

    janela.blit(fundo,(0,0))
    janela.blit(gol, (x,y))
    janela.blit(azul, (pos_x, pos_y))
    janela.blit(latam, (posi_x, posi_y))
    janela.blit(avianca, (position_x, position_y))

    pygame.display.update()

pygame.quit()
