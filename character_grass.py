from pico2d import*
import os

os.chdir('C:\\github_upload\\01')

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400, 30)
character.draw_now(400, 90)

while(True):
    x = 0
    while(x < 785):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)

    y = 90
    while(y < 560):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(785, y)
        y = y + 2
        delay(0.01)

    x = 785
    while(x > 10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 560)
        x = x - 2
        delay(0.01)

    y = 560
    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(10, y)
        y = y - 2
        delay(0.01)

    

    
