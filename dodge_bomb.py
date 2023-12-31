import sys
import pygame as pg
import random

def check_bound(rect):
    yoko,tate = True, True
    if rect.left < 0 or WIDTH < rect.right:
        yoko = False
    if rect.top <0 or HEIGHT < rect.bottom:
        tate = False
    return yoko, tate

WIDTH, HEIGHT = 1600, 900
delta = {
    pg.K_UP : (0,-5),
    pg.K_DOWN : (0,+5),
    pg.K_LEFT : (-5,0),
    pg.K_RIGHT : (+5,0),
}
kk_img = pg.image.load("ex02/fig/3.png")
kk_img1 = pg.transform.flip(kk_img,True,False)
muki = {
    (0,0) : kk_img1,
    (+5,0) : kk_img1,
    (+5,-5) : pg.transform.rotozoom(kk_img1,45,1.0),
    (0,-5) :  pg.transform.rotozoom(kk_img1,90,1.0),
    (-5,-5) : pg.transform.rotozoom(kk_img,-45,1.0),
    (-5,0) :kk_img,
    (-5,+5) : pg.transform.rotozoom(kk_img,45,1.0),
    (0,+5) : pg.transform.rotozoom(kk_img1,-90,1.0),
    (+5,+5) : pg.transform.rotozoom(kk_img1,-45,1.0)
    }
accs = [a for a in range(1,11)]#加速度
for r in range(1,11):
    bb_img = pg.Surface((20*r, 20*r))
    pg.draw.circle(bb_img, (255, 0, 0), (10*r, 10*r), 10*r)
    bb_imgs.append(bb_img)
#空欄修正済み

def main():
    """
    画面外か中かを判定する、Trueで内、Falseで外判定。すべてのオブジェクトに適用
    """
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct= kk_img.get_rect()
    kk_rct.center = 900,400

    bb = pg.Surface((20,20))
    pg.draw.circle(bb,(255,0,0),(10,10),10)
    bb.set_colorkey((0,0,0))
    x = random.randint(0,WIDTH)
    y = random.randint(0,HEIGHT)
    bb_rct = bb.get_rect()#爆弾座標抽出
    bb_rct.center = x, y #爆弾の座標を乱数指定
    vx, vy = +5 ,+5
    clock = pg.time.Clock()
    tmr = 0


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        if kk_rct.colliderect(bb_rct):
            print("ゲームオーバー")
            return
        
        key_lst = pg.key.get_pressed()
        sum_mv = [0,0]
        for k, mv in delta.items():
            if key_lst[k]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_img = muki[tuple(sum_mv)]
        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        screen.blit(bb,bb_rct)
        bb_rct.move_ip(vx,vy)
        yoko, tate = check_bound(bb_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        screen.blit(bb,bb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()