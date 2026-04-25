from pygame import *

from random import randint

win_width = 700
win_height = 500

window = display.set_mode((700,500))
display.set_caption('Пинг понг')
window.fill((216, 219, 124))

speed_x = 3
speed_y = 3



class GameSprite(sprite.Sprite):
    def __init__(self,color,x,y,w, h, spd):
        super().__init__()
        self.image = Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = spd

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Platform(GameSprite):
    def __init__(self, x, y, w, h=20):
        super().__init__((60, 179, 60), x, y, w, h, 0)

p = Platform(0, 480, 700)
platforms = sprite.Group()
platforms.add(p)

v = Platform(100, 300, 100)
platforms.add(v)

s = Platform(200, 200, 100)
platforms.add(s)

x = Platform(300, 300, 100)
platforms.add(x)

m = Platform(400, 200, 100)
platforms.add(m)

j = Platform(500, 300, 100)
platforms.add(j)

class Player(GameSprite):
    def __init__(self, color, x, y, w, h, spd):
        super().__init__(color, x, y, w, h, spd)
        self.vel_y = 0
        self.on_ground = False

    def update(self):
       



        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
           self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 100:
           self.rect.x += self.speed
        if keys[K_SPACE] and self.on_ground:
           self.vel_y = -13
           self.on_ground = False

        self.vel_y += 0.6
        self.rect.y += int(self.vel_y)

        self.on_ground = False
        for p in platforms:
            if self.rect.colliderect(p.rect):
                if self.vel_y > 0:
                    self.rect.bottom = p.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = p.rect.bottom
                    self.vel_y = 0

player = Player((70, 130, 180), 60, 400, 40, 50, 5)

   
font.init()
font = font.Font(None,35)
lose1 = font.render('player1 lost', True,(180,0,0))
lose2 = font.render('player2 lost', True,(180,0,0))

game = True
finish = False


while game:

    

    for e in event.get():
        if e.type == QUIT:
            game = False

        
    if finish != True:


        window.fill((216, 219, 124))

        platforms.draw(window)

        player.update()
        player.reset()



        display.update()

        time.delay(25)