from pygame import *
from button import Button

window = display.set_mode((700,500))
clock = time.Clock()

game = True

btn_start = Button(200,200, 100, 50, "start_btn.png")
btn_end = Button(200,400, 100, 50, "exit_btn.png")

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if run:
        
        window.fill((255,0,0))
    else:
        window.fill((0,255,0))
        if btn_start.draw(window):
            run = True
        if btn_end.draw(window):
            game = False


    display.update()
    clock.tick(60)