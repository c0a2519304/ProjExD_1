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
 

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        background = tmr
        background = tmr % 3200
        screen.blit(bg_img, [-background, 0])
        screen.blit(bg_img2, [-background + 1600, 0])
        screen.blit(bg_img, [-background + 3200, 0])

        screen.blit(kokaton_3, [300, 200])
        pg.display.update()
        
        tmr += 1
        clock.tick(2000)
        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()