import pygame
from random import randint

pygame.init()
x = 30
y = 250
pos_x = 1500
pos_y = 200
posi_x = 1900
posi_y = 400
position_x = -300
position_y = 510

velocidade = 15
velocidade_outros = 13

fundo = pygame.image.load('ceu.png')
gol = pygame.image.load('gol1.png')
azul = pygame.image.load('azulpequeno.png')
latam = pygame.image.load('latampequeno.png')
avianca = pygame.image.load('avianca.png')

janela = pygame.display.set_mode((1300, 600))
pygame.display.set_caption("Criando um jogo com Python")


janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

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
        posi_x = randint(1300, 1800)
        position_x = randint(-150, -10)

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
