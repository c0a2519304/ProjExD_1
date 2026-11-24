import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,  True, False)
    tmr = 0
    kokaton_3 = pg.image.load("fig/3.png")
    kokaton_3 = pg.transform.flip(kokaton_3, True, False)
    kk_rct = kokaton_3.get_rect()
    kk_rct.center = 300, 200
 

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        x = -1
        y = 0
        if key_lst[pg.K_UP]:
            y = -1
        if key_lst[pg.K_DOWN]:
            y = 1
        if key_lst[pg.K_RIGHT] and key_lst[pg.K_LEFT]:
            x = 0
        elif key_lst[pg.K_RIGHT]:
            x = 1
        elif key_lst[pg.K_LEFT]:
            x = -2

        kk_rct.move_ip((x, y))

        background = tmr
        background = tmr % 3200
        screen.blit(bg_img, [-background, 0])
        screen.blit(bg_img2, [-background + 1600, 0])
        screen.blit(bg_img, [-background + 3200, 0])

        screen.blit(kokaton_3, kk_rct)
        pg.display.update()
        
        tmr += 1
        clock.tick(200)
        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()