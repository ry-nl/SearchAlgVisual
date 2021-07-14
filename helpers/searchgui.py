import sys
import pygame as pg
from helpers.graph import *
import math

pg.init()

screen_sz = 1500, 1100
screen = pg.display.set_mode(screen_sz)

weightfont = pg.font.SysFont('Corbel', 15)
smallfont = pg.font.SysFont('Corbel', 25)

weight = 1

def click_handler(mousex, mousey, button):
    global weight
    
    node = None

    if 0 <= mousex <= 1500 and 100 <= mousey <= 1100:
        col = math.floor(mousex/20)
        row = math.floor((mousey - 100)/20)
        
        node = graph[row][col]
        
        if button == 1:
            if startendNodes[0] == node or startendNodes[1] == node:
                if startendNodes[0] == node:
                    startendNodes[0] = None
                if startendNodes[1] == node:
                    startendNodes[1] = None
            node.makeObstruct()
        if button == 3: 
            if startendNodes[0] == node or startendNodes[1] == node:
                if startendNodes[0] == node:
                    startendNodes[0] = None
                if startendNodes[1] == node:
                    startendNodes[1] = None
                node.makeNeutral()
            elif node.nodeType == 'obstruct':
                node.makeNeutral()
            else:
                if startendNodes[0] == None:
                    if startendNodes[1] != node:
                        startendNodes[0] = node
                        node.makeStart()
                if startendNodes[1] == None:
                    if startendNodes[0] != node:
                        startendNodes[1] = node
                        node.makeEnd()
        if button == 4:
            if node.nodeType == 'neutral':
                node.weight = weight
                
                
        return 'draw'
    else:
        if 20 <= mousey <= 50:
            if 15 <= mousex <= 95:
                return 'reset'
            elif 110 <= mousex <= 190:
                return 'astar'
            elif 205 <= mousex <= 285:
                return 'dijkstras'
            elif 300 <= mousex <= 380: 
                return 'bfs'
            elif 1300 <= mousex <= 1380:
                weight += 1
                if weight >= 6:
                    weight = 1
                return 'weight'


def color_node(row, col):
    pg.draw.rect(screen, graph[row][col].color, pg.Rect(1 + col * 20, 101 + row * 20, 19, 19))

    if graph[row][col].weight > 1:
        g_weight_text = weightfont.render(f'{graph[row][col].weight}', True, pg.Color('black'))
        screen.blit(g_weight_text, (5 + col * 20, 105 + row * 20))

    pg.display.update()

def color_nodes():
    for row in range(50):
        for col in range(75):
            pg.draw.rect(screen, graph[row][col].color, pg.Rect(1 + col * 20, 101 + row * 20, 19, 19))
    
            if graph[row][col].weight > 1:
                g_weight_text = weightfont.render(f'{graph[row][col].weight}', True, pg.Color('black'))
                screen.blit(g_weight_text, (5 + col * 20, 105 + row * 20))

    pg.display.update()

def color_finished():
    for row in range(50):
        for col in range(75):
            if graph[row][col].nodeType == 'open' or graph[row][col].nodeType == 'closed':
                graph[row][col].makeFinished()
    
    color_nodes()

# button colors
hovered_color = (200, 200, 200)
nothovered_color = (100, 100, 100)
# button text
weight_text = smallfont.render('weight', True, pg.Color('black'))
bfs_text = smallfont.render('bfs', True, pg.Color('black'))
dij_text = smallfont.render('dijk', True, pg.Color('black'))
astar_text = smallfont.render('astar', True, pg.Color('black'))
reset_text = smallfont.render('reset', True, pg.Color('black'))


# DRAW BUTTONS FUNCTION
def draw_buttons(mouse):
    global weight
    
    button_area = pg.Surface([80, 30])

    button_area.fill(pg.Color(nothovered_color))

    if 15 <= mouse[0] <= 95 and 20 <= mouse[1] <= 50:
        button_area.fill(pg.Color(hovered_color))

    screen.blit(button_area, (15, 20))
    screen.blit(reset_text, (30, 22))
    
    button_area.fill(pg.Color(nothovered_color))

    if 110 <= mouse[0] <= 190 and 20 <= mouse[1] <= 50:
        button_area.fill(pg.Color(hovered_color))
    
    screen.blit(button_area, (110, 20))
    screen.blit(astar_text, (125, 22))

    button_area.fill(pg.Color(nothovered_color))

    if 205 <= mouse[0] <= 285 and 20 <= mouse[1] <= 50:
        button_area.fill(pg.Color(hovered_color))
        
    screen.blit(button_area, (205, 20))
    screen.blit(dij_text, (225, 22))
    
    button_area.fill(pg.Color(nothovered_color)) 

    if 300 <= mouse[0] <= 380 and 20 <= mouse[1] <= 50:
        button_area.fill(pg.Color(hovered_color))
    
    screen.blit(button_area, (300, 20))
    screen.blit(bfs_text, (330, 22))

    button_area.fill(pg.Color(nothovered_color)) 

    if 1300 <= mouse[0] <= 1380 and 20 <= mouse[1] <= 50:
        button_area.fill(pg.Color(hovered_color))
    
    screen.blit(button_area, (1300, 20))
    screen.blit(weight_text, (1308, 22))

    weightval_text = smallfont.render(f'{weight}', True, pg.Color('black'))
    
    screen.blit(weightval_text, (1270, 22))

def draw_bg():
    mouse = pg.mouse.get_pos()
    
    screen.fill(pg.Color('white'))

    for col in range(75):
        pg.draw.line(screen, pg.Color('black'), pg.Vector2(20 * col, 100), pg.Vector2(20 * col, 1100), 1)
    for row in range(50):
        pg.draw.line(screen, pg.Color('black'), pg.Vector2(0, 100 + 20 * row), pg.Vector2(1500, 100 + 20 * row), 1)

    draw_buttons(mouse)
    color_nodes()

def main_loop():
    global weight

    action = None
    mouse = pg.mouse.get_pos()

    lmb_held = pg.mouse.get_pressed()[0]
    wkey_held = pg.key.get_pressed()[pg.K_w]

    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 3:
                action = click_handler(mouse[0], mouse[1], 3)

        if lmb_held:
            assert 0 <= mouse[0] <= 1500 and 0 <= mouse[1] <= 1100, print('click out of bounds')
            action = click_handler(mouse[0], mouse[1], 1)
        
        if wkey_held:
            action = click_handler(mouse[0], mouse[1], 4)

    draw_bg()

    pg.display.flip()

    pg.time.delay(1)

    return action