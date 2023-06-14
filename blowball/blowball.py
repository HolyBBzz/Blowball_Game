from pygame import *
from random import randint
import time as Timer
resurce_water = 45
live = 20
font.init()
my_font = font.SysFont(None, 40)
class GameSprite(sprite.Sprite):
    def __init__(self, _image, x, y, width,height, per):
        super().__init__()
        self.image = transform.scale(image.load(_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.per = per
        self.rect.y = y
    def clear(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #draw.rect(window, (0, 255, 0), self.rect, 10)
    def move(self):
        k = key.get_pressed()
        if k[K_w] and k[K_s]:
            self.rect.y = self.rect.y
            self.rect.x = self.rect.x    
        elif k[K_w] and background.rect.y < 0 and shop_act == False:
            self.rect.y += 10  
        elif k[K_s] and background.rect.y > -200 and shop_act == False: 
            self.rect.y -= 10  
class Flower(GameSprite):
    def update(self):
        k = key.get_pressed()  
        #if k[K_t]:
            #global resurce_water
            #resurce_water += 1100000
        if root.per > 10:
            root.per -= 1
        if flow.per > 16:
            flow.per -= 1
class Bee(GameSprite):
    def fly(self):
        global live
        global bee_steps
        global bee
        global b
        if bee_steps == 0:
            bee_steps = 1
            b = 1
        if bee_steps == 1:
            bee.rect.x -= 2
        if bee.rect.x < 319:
            live += 10
            bee_steps = 2
        if bee_steps == 2:
            b = 2
            bee.rect.x += 2
        if bee.rect.x > 700:
            bee_steps = 4
class Button(GameSprite):
    def mou(self):           
        mout = mouse.get_pos()
        if self.rect.x < mout[0] < self.rect.x + self.rect.width and self.rect.y < mout[1] < self.rect.y + self.rect.height:
            self.per = 1
        else:
            self.per = 0
tutor = GameSprite('tutorial.png', 600, 300, 50, 100, 0)
background = GameSprite('background.png', 0, -200, 700, 700, 0)
flow = Flower('flow1.png', 140, -142, 400, 274, 1)
root = Flower('root1.png', 286, 116, 146, 136, 1)
live_bar = GameSprite('live_bar.png', 570, 10, 100, 100, 20)
min_bar = GameSprite('min_bar.png', 570, 110, 100, 100, 20)
shop = GameSprite('shop.png', 25, 25, 500, 450, 0)
flow_but = Button('flow_button0.png', 75, 75, 210, 60, 0)
root_but = Button('root_button0.png', 75, 140, 210, 60, 0)
but_shop = Button('button_shop0.png', 0, 0, 70, 70, 0)
bee = Bee('bee0-1.png', 700, flow.rect.y - 15, 61, 53, 0) 
resolution = (700,500)
window = display.set_mode(resolution)
display.set_caption('BlowBall Simulator :3')
clock = time.Clock()
game = True
FPS = 60
tutorial = 0
shop_act = False
tick_bee = 0
b = 1
bee_steps = 4
while game:
    flow_but = Button('flow_button'+ str(flow_but.per) + '.png', 75, 75, 210, 60, flow_but.per)
    root_but = Button('root_button'+ str(root_but.per) + '.png', 75, 140, 210, 60, root_but.per)
    but_shop = Button('button_shop'+ str(but_shop.per) + '.png', 0, 0, 70, 70, but_shop.per)
    Ticks = clock.tick(FPS)
    bee = Bee('bee' + str(bee.per) + '-' + str(b) + '.png', bee.rect.x, flow.rect.y - 15, 61, 53, bee.per) 
    background.clear()
    k = key.get_pressed() 
    if 15 > flow.per > 10:
        tick_bee += 0.01
    if resurce_water < 0:
        resurce_water = 0
    if live < 0:
        game = False 
    if root.per > 1:
        resurce_water += root.per * 0.003
    if flow.per > 3:
        resurce_water += flow.per * 0.001
    if resurce_water < 10:
        live -= 0.01 - flow.per * 0.001 
    if flow.per > 10:
        live += 0.001
    if round(tick_bee, 0) == randint(10, 300) and 15 > flow.per > 10:
        bee_steps = 0
        tick_bee = 0
        bee.per = randint(0, 2)
        if bee.per == 2:
            bee.per = randint(1, 2)
    live_font = my_font.render(str(round(live, 0)), True,(255,255,255))
    root_font = my_font.render(str(round(resurce_water, 0)), True,(255,255,255))
    flow_sale = my_font.render(str(round(live_bar.per, 0)), True,(255,255,255))
    root_sale = my_font.render(str(round(min_bar.per, 0)), True,(255,255,255))
    root.clear()
    root.move()
    flow.clear()
    flow.move()
    bee.clear()
    bee.fly() 
    if shop_act == True:
        shop.clear()
        if root.per < 9:
            root_but.clear()
            window.blit(root_sale, (222, 157))
        if flow.per < 16:
            flow_but.clear()
            window.blit(flow_sale, (222, 92))
    but_shop.clear()
    live_bar.clear()
    min_bar.clear()
    window.blit(live_font, (605, 75))
    window.blit(root_font, (605, 175))
    if k[K_f]:
        fps_show = my_font.render('FPS ' + str(Ticks), True,(255,255,255))  
        window.blit(fps_show, (10, 450))
    if k[K_w] and tutorial == 0 or k[K_s] and tutorial == 0:
        tutorial = 1
    if tutorial == 0:
        tutor.clear()
    background.move()
    flow.update()
    root.update()
    sh_x = but_shop.rect.x
    sh_y = but_shop.rect.y
    ro_x = root_but.rect.x
    ro_y = root_but.rect.y
    fl_x = flow_but.rect.x
    fl_y = flow_but.rect.y 
    for i in event.get():
        if i.type == QUIT:
            game = False
        elif i.type == MOUSEMOTION:
            but_shop.mou()
            flow_but.mou()
            root_but.mou()
        elif i.type == MOUSEBUTTONDOWN:
            mout = mouse.get_pos()
            if sh_x < mout[0] < sh_x + but_shop.rect.width and sh_y < mout[1] < sh_y + but_shop.rect.height and shop_act == False:
                shop_act = True
            elif sh_x < mout[0] < sh_x + but_shop.rect.width and sh_y < mout[1] < sh_y + but_shop.rect.height and shop_act == True:
                shop_act = False
            if shop_act == True:
                if ro_x < mout[0] < ro_x + root_but.rect.width and ro_y < mout[1] < ro_y + root_but.rect.height and root.per < 10:
                    if resurce_water > min_bar.per - 1:
                        resurce_water -= min_bar.per
                        root.per += 1
                        min_bar.per += 10
                if fl_x < mout[0] < fl_x + flow_but.rect.width and fl_y < mout[1] < fl_y + flow_but.rect.height and flow.per < 16:
                    if resurce_water > live_bar.per - 1:
                        resurce_water -= live_bar.per
                        flow.per += 1
                        live_bar.per += 10
    root = Flower('root' + str(root.per) + '.png', root.rect.x, root.rect.y, 146, 136, root.per)
    flow = Flower('flow'  + str(flow.per) + '.png', flow.rect.x, flow.rect.y, 400, 274, flow.per)
    Ticks
    display.update()