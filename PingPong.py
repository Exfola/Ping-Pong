import pygame
pygame.init()

class GameSprite():

    def __init__(self):
        #cria a variavel racket e põe uma imagem
        racket = pygame.image.load("racket.png")

        #Cria a variavel racket_R e muda o tamanho da imagem
        racket_R = pygame.transform.scale(racket, (200, 200))

        #cria a variavel ball e põe uma imagem
        ball = pygame.image.load("racket.png")

        #Cria a variavel ball_R e muda o tamanho da imagem
        ball_R = pygame.transform.scale(racket, (200, 200))

        #Determinar a velocidade X e Y da racket
        vRX = 3
        vRY = 3

        #Determinar a velocidade X e Y da ball
        vBX = 3
        vBY = 3

class Player (GameSprite):

    def update_r(self):
        keys = Key.get_pressed()
        if keys[K_UP] and self.rect.y > 5 :
            self.rect.y -= self.speed

        if keys[K_DOWN]:
            self.rect.y -= self.speed

        if keys[K_UP]:
            self.rect.x += self.speed
