from pygame import *

window = display.set_mode((700,500))


class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys_pressed = key.get_pressed()

        if keys[K_w] :
            self.rect.y -= self.speed
        if keys[K_s] :
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()

        if keys[K_UP] :
            self.rect.y -= self.speed
        if keys[K_DOWN] :
            self.rect.y += self.speed

player1 = Player("Table.png", 20, 200, 50, 200, 5)
player2 = Player("Table.png", 500, 200, 50, 200, 5)
ball = GameSprite("ball.png", 200, 200, 50, 200, 5)

