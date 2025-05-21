from pygame import *
from Game import *

class Player (GameSprite):

    def update_r(self):
        keys = Key.get_pressed()
        if keys[K_UP] and self.rect.y > 5 :
            self.rect.y -= self.speed

        if keys[K_DOWN]:
            self.rect.y -= self.speed

        if keys[K_UP]:
            self.rect.x += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K-w] and self.rect.y > 5 :
            self.rect.y -= self.speed

        if keys[k_w]:
            self.rect.x += self.speed

        if keys[k_s]:
            self.rect.y += self.speed


    cor_fundo = (100, 149, 237)
    win_width = 600
    win_height = 500
    janela = display.set_mode((win_width, win_height))
    display.set_caption("Ping-Pong")


    clock = time.Clock()
    finish = False
    Game = True
    while Game:
        for evento in event.get():
            if evento.type == QUIT:
                Game = False
        janela.fill(cor_fundo)
        display.flip()
    
    clock.tick(60)

    racket1 = Player("racket.png", 100, 100, 5, 55, 55)
