from pygame import *

img_back = "background.png"

display.set_caption('Пинг-понг')
window = display.set_mode((800, 600))
background = transform.scale(image.load(img_back), (800, 600))

img_pl = "Red.png"
img_boll = "Boll.png"



clock = time.Clock()
clock.tick(30)

#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)
 
       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
#класс главного игрока
class Player(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 5:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 5:
            self.rect.y += self.speed

pl1 = Player(img_pl, 5, 100, 20, 100, 10)
pl2 = Player(img_pl, 775, 100, 20, 100, 10)
boll = GameSprite(img_boll, 400, 400, 50, 50, 10)

run = True
finish = False
while(run):
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        #обновляем фон
        window.blit(background,(0,0))
        #производим движения спрайтов
        pl1.update_l()
        pl2.update_r()
        boll.reset()
        pl1.reset()
        pl2.reset()
    display.update()
    time.delay(60)


