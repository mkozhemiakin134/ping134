from pygame import *
font.init()
font1 = font.SysFont("Arial", 36)

from time import time as timer 

#создай окно игры
win_width = 900
win_height = 700
game_win = display.set_mode((win_width, win_height))
display.set_caption("Пинг-понг")

#задай фон сцены
background = image.load("table.jpg")
background = transform.scale(background, (win_width,win_height))
clock = time.Clock()
FPS = 60

dx = 5
dy = 5

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
        self.size_x = size_x
        self.size_y = size_y
    def reset(self):
        game_win.blit(self.image, (self.rect.x, self.rect.y))

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Player(GameSprite):
    def update_right(self):
        keys = key.get_pressed()
        
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 5:
            self.rect.y += self.speed

    def update_left(self):
        keys = key.get_pressed()
        
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 5:
            self.rect.y += self.speed

#обработай событие «клик по кнопке "Закрыть окно"»
rocket1 = Player("platform.png", win_width - 20, win_height // 2 - 50, 20, 100, 10)
rocket2 = Player("platform.png", 5, win_height // 2 - 50, 20, 100, 10)

class Ball(GameSprite):
    def update(self):
        global dx, dy
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.y <= 0 or self.rect.y > 650:
            dy = dy * (-1)
        
        if self.rect.x > 890:
            self.rect.x = win_width // 2
            self.rect.y = win_height // 2

        if  self.rect.x < 10:
            self.rect.x = win_width // 2
            self.rect.y = win_height // 2

        if self.colliderect(rocket1.rect) or self.colliderect(rocket2.rect):
            dx = dx * (-1)

ball = Ball("ball.png", win_width // 2, win_height // 2, 50, 50, 7)

finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        game_win.blit(background, (0,0))
        rocket1.update_right()
        rocket1.reset()
        rocket2.update_left()
        rocket2.reset()
        ball.update()
        ball.reset()

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
      

    display.update()
    clock.tick(FPS)
