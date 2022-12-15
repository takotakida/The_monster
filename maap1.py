import pygame as pg
import random as rd
import datetime as dt


def plaay():
    pg.init()

    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT  = 1000
    SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("game")
    background = pg.image.load("image.png")
    clock = pg.time.Clock()

    class obj:
        def __init__(self):
            self.x = 0
            self.y = 0
            self.move = 0
        def put_img(self,address):
            self.img = pg.image.load(address)
            self.sx,self.sy = self.img.get_size()
        def change_size(self,sx,sy):
            self.img = pg.transform.scale(self.img,(sx,sy))
            self.sx,self.sy = self.img.get_size()
        def show(self):
            SCREEN.blit(self.img,(self.x,self.y))

    def crash(a,b):
        if (a.x - b.sx <= b.x) and (b.x <= a.x + a.sx):
            if (a.y - b.sy <= b.y) and (b.y - a.y + a.sy):
                return True
            else:
                return False
        else:
            return False 

    durability = 100

    monster_spawn = 199

    over = False

    t1 = obj()
    t1.put_img("IMG_0381.png")
    t1.change_size(100,150)
    t1.x = SCREEN_WIDTH / 8 - t1.sx / 2 
    t1.y =  (SCREEN_HEIGHT / 2 + 160) - t1.sy / 2

    t2 = obj()
    t2.put_img("IMG_0382.png")
    t2.change_size(100,150)
    t2.x = (SCREEN_WIDTH / 8 + 150) - t2.sx / 2
    t2.y =  (SCREEN_HEIGHT / 2 + 160) - t2.sy / 2

    t3 = obj()
    t3.put_img("IMG_0385.png")
    t3.change_size(100,150)
    t3.x = (SCREEN_WIDTH / 8 + 350) - t3.sx / 2
    t3.y =  (SCREEN_HEIGHT / 2 + 160) - t3.sy / 2

    t4 = obj()
    t4.put_img("IMG_0387.png")
    t4.change_size(100,150)
    t4.x = (SCREEN_WIDTH / 8 + 500) - t4.sx / 2
    t4.y =  (SCREEN_HEIGHT / 2 + 160) - t4.sy / 2

    m1_list = []
    m2_list = []
    m3_list = []
    m4_list = []

    r1_list = []
    r2_list = []
    r3_list = []
    r4_list = []

    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0

    at1 = 40
    at2 = 40
    at3 = 40
    at4 = 40
    
    coin = 0

    start_time = dt.datetime.now()
    
    play = True
    while play:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                play = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    if coin >= 100:
                        coin -= 100
                        r1 = rd.randrange(1,101)
                        if r1 <= 50:
                            at1 = 40
                        elif r1 > 50 and r1 <= 75:
                            at1 = 30
                        elif r1 >75 and r1 <= 88:
                            at1 = 20
                        elif r1 > 88 and r1 <= 96:
                            at1 = 10
                        elif r1 > 96 and r1 <= 100:
                            at1 = 5

                if event.key == pg.K_UP:
                    if coin >= 100:
                        coin -= 100
                        r1 = rd.randrange(1,101)
                        if r1 <= 50:
                            at2 = 40
                        elif r1 > 50 and r1 <= 75:
                            at2 = 30
                        elif r1 >75 and r1 <= 88:
                            at2 = 20
                        elif r1 > 88 and r1 <= 96:
                            at2 = 10
                        elif r1 > 96 and r1 <= 100:
                            at2 = 5

                if event.key == pg.K_DOWN:
                    if coin >= 100:
                        coin -= 100
                        r1 = rd.randrange(1,101)
                        if r1 <= 50:
                            at3 = 40
                        elif r1 > 50 and r1 <= 75:
                            at3 = 30
                        elif r1 >75 and r1 <= 88:
                            at3 = 20
                        elif r1 > 88 and r1 <= 96:
                            at3 = 10
                        elif r1 > 96 and r1 <= 100:
                            at3 = 5

                if event.key == pg.K_RIGHT:
                    if coin >= 100:
                        coin -= 100
                        r1 = rd.randrange(1,101)
                        if r1 <= 50:
                            at4 = 40
                        elif r1 > 50 and r1 <= 75:
                            at4 = 30
                        elif r1 >75 and r1 <= 88:
                            at4 = 20
                        elif r1 > 88 and r1 <= 96:
                            at4 = 10
                        elif r1 > 96 and r1 <= 100:
                            at4 = 5

        coin += 1

        now_time = dt.datetime.now()
        delta_time = round((now_time - start_time).total_seconds())

        if rd.randint(1,201) > monster_spawn:
            m1 = obj()
            m1.put_img("IMG_0337.png")
            m1.change_size(50,50)
            m1.x = SCREEN_WIDTH / 8 - m1.sx / 2
            m1.y = 0
            m1.move = 5 
            m1_list.append(m1)
    
        d_list = []
    
        for i in range(len(m1_list)):
            mo1 = m1_list[i]
            mo1.y += mo1.move
            if mo1.y >= 560:
                d_list.append(i)
                
        d_list.reverse()
    
        for d in d_list:
            del m1_list[d]
            durability -= 1
    

        if rd.randint(1,201) > monster_spawn:
            m2 = obj()
            m2.put_img("IMG_0337.png")
            m2.change_size(50,50)
            m2.x = (SCREEN_WIDTH / 8 + 150) - m2.sx / 2
            m2.y = 0
            m2.move = 5
            m2_list.append(m2)

        d_list = []

        for i in range(len(m2_list)):
            mo2 = m2_list[i]
            mo2.y += mo2.move
            if mo2.y >= 560:
                d_list.append(i)
                
        d_list.reverse()
        
        for d in d_list:
            del m2_list[d]
            durability -= 1

        if rd.randint(1,201) > monster_spawn:
            m3 = obj()
            m3.put_img("IMG_0341.png")
            m3.change_size(50,50)
            m3.x = (SCREEN_WIDTH / 8 + 350) - m3.sx / 2
            m3.y = 0
            m3.move = 5
            m3_list.append(m3)

        d_list = []

        for i in range(len(m3_list)):
            mo3 = m3_list[i]
            mo3.y += mo3.move
            if mo3.y >= 560:
                d_list.append(i)
        
        d_list.reverse()
        
        for d in d_list:
            del m3_list[d]
            durability -= 1

        if rd.randint(1,201) > monster_spawn:
            m4 = obj()
            m4.put_img("IMG_0364.png")
            m4.change_size(50,50)   
            m4.x = (SCREEN_WIDTH / 8 + 500) - m4.sx / 2
            m4.y = 0
            m4.move = 5
            m4_list.append(m4)

        d_list = []
        
        for i in range(len(m4_list)):
            mo4 = m4_list[i]
            mo4.y += mo4.move
            if mo4.y >= 560:
                d_list.append(i)
        
        d_list.reverse()
        
        for d in d_list:
            del m4_list[d]
            durability -= 1

        if k1 > at1:
            k1 = 0
            r1 = obj()
            r1.put_img("missle.png")
            r1.change_size(50,50)
            r1.x = (SCREEN_WIDTH / 8 - r1.sx / 2)
            r1.y = (SCREEN_HEIGHT / 2 + 80) - r1.sy
            r1.move = 10
            r1_list.append(r1)
        
        d_list = []
        k1 += 1
        k2 += 1
        k3 += 1
        k4 += 1
        for i in range(len(r1_list)):
            ro1 = r1_list[i]
            ro1.y -= ro1.move
            if ro1.y <= 0:
                d_list.append(i)
        
        d_list.reverse()
        
        for d in d_list:
            del r1_list[d]

        if k2 > at2:
            k2 = 0
            r2 = obj()
            r2.put_img("missle.png")
            r2.change_size(50,50)
            r2.x = ((SCREEN_WIDTH / 8 + 150) - r2.sx / 2)
            r2.y = (SCREEN_HEIGHT / 2 + 80) - r2.sy
            r2.move = 10
            r2_list.append(r2)

        d_list = []
        
        for i in range(len(r2_list)):
            ro2 = r2_list[i]
            ro2.y -= ro2.move
            if ro2.y <= 0:
                d_list.append(i)
        
        d_list.reverse()
        
        for d in d_list:
            del r2_list[d]

        if k3 > at3:
            k3 = 0
            r3 = obj()
            r3.put_img("missle.png")
            r3.change_size(50,50)
            r3.x = ((SCREEN_WIDTH / 8 + 350) - r3.sx / 2)
            r3.y = (SCREEN_HEIGHT / 2 + 80) - r3.sy
            r3.move = 10
            r3_list.append(r3)

        d_list = []
        
        for i in range(len(r3_list)):
            ro3 = r3_list[i]
            ro3.y -= ro3.move
            if ro3.y <= 0:
                d_list.append(i)
        
        d_list.reverse()
        
        for d in d_list:
            del r3_list[d]

        if k4 > at4:
            k4 = 0
            r4 = obj()
            r4.put_img("missle.png")
            r4.change_size(50,50)
            r4.x = ((SCREEN_WIDTH / 8 + 500) - r4.sx / 2)
            r4.y = (SCREEN_HEIGHT / 2 + 80) - r4.sy
            r4.move = 10
            r4_list.append(r4)

        d_list = []
        
        for i in range(len(r4_list)):
            ro4 = r4_list[i]
            ro4.y -= ro4.move
            if ro4.y <= 0:
                d_list.append(i)
        
        d_list.reverse()    
        
        for d in d_list:
            del r4_list[d]

        dm_list = []
        dr_list = []

        for i in range(len(r1_list)):
            for j in range(len(m1_list)):
                mo1 = m1_list[j]
                ro1 = r1_list[i]
                if crash(ro1,mo1) == True:
                    dm_list.append(i)
                    dr_list.append(j)
        
        dm_list = list(set(dm_list))
        dr_list = list(set(dr_list))

        dm_list.reverse()
        dr_list.reverse()

        try:
            for dm in dm_list:
                del m1_list[dm]
            for dr in dr_list:
                del r1_list[dr]
        except:
            pass
        
        dm_list = []
        dr_list = []

        for i in range(len(r2_list)):
            for j in range(len(m2_list)):
                mo2 = m2_list[j]
                ro2 = r2_list[i]
                if crash(ro2,mo2) == True:
                    dm_list.append(i)
                    dr_list.append(j)
        
        dm_list = list(set(dm_list))
        dr_list = list(set(dr_list))

        dm_list.reverse()
        dr_list.reverse()

        try:
            for dm in dm_list:
                del m2_list[dm]
            for dr in dr_list:
                del r2_list[dr]
        except:
            pass
        
        dm_list = []
        dr_list = []

        for i in range(len(r3_list)):
            for j in range(len(m3_list)):
                mo3 = m3_list[j]
                ro3 = r3_list[i]
                if crash(ro3,mo3) == True:
                    dm_list.append(i)
                    dr_list.append(j)
        
        dm_list = list(set(dm_list))
        dr_list = list(set(dr_list))

        dm_list.reverse()
        dr_list.reverse()
        
        try:
            for dm in dm_list:
                del m3_list[dm]
            for dr in dr_list:
                del r3_list[dr]
        except:
            pass
        
        dm_list = []
        dr_list = []

        for i in range(len(r4_list)):
            for j in range(len(m4_list)):
                mo4 = m4_list[j]
                ro4 = r4_list[i]
                if crash(ro4,mo4) == True:
                    dm_list.append(i)
                    dr_list.append(j)
        
        dm_list = list(set(dm_list))
        dr_list = list(set(dr_list))

        dm_list.reverse()
        dr_list.reverse()

        try:
            for dm in dm_list:
                del m4_list[dm]
            for dr in dr_list:
                del r4_list[dr]
        except:
            pass

        SCREEN.blit(background,(0,0))
        for mo1 in m1_list:
            mo1.show()
        for mo2 in m2_list:
            mo2.show()
        for mo3 in m3_list:
            mo3.show()
        for mo4 in m4_list:
            mo4.show()
        t1.show()
        t2.show()
        t3.show()
        t4.show()
        for ro1 in r1_list:
            ro1.show()
        for ro2 in r2_list:
            ro2.show()
        for ro3 in r3_list:
            ro3.show()
        for ro4 in r4_list:
            ro4.show()

        font = pg.font.Font(None,30)
        text_durability = font.render("durability : {} / 100".format(durability),True, (0,0,0))
        SCREEN.blit(text_durability,(760,100))

        text_time = font.render("time : {} ".format(delta_time),True, (0,0,0))
        SCREEN.blit(text_time,(760,70))

        text_coin = font.render("coin : {} ".format(coin),True, (0,0,0))
        SCREEN.blit(text_coin,(760,130))

        monster_spawn -= 0.002  

        if durability <= 0:
            play = False
            over = True
            

        pg.display.flip()

    while over == True:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                over = False
        font = pg.font.Font(None,100)
        text = font.render("Game over",True,(0,0,0))
        SCREEN.blit(text,(350,350))

        font = pg.font.Font(None,50)
        teext = font.render("time : {}".format(delta_time),True,(0,0,0))
        SCREEN.blit(teext,(350,450))
        pg.display.flip()
    pg.quit()


if __name__ == '__main__':
    plaay()