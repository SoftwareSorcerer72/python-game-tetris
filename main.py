import pygame
from copy import deepcopy

W, H = 10, 20
TILE = 45
GAME_RES = W * TILE, H * TILE
FPS = 60

pygame.init()
game_sc = pygame.display.set_mode(GAME_RES)
clock = pygame.time. Clock()

grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(W) for y in range(H)]

figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

figures = [[pygame.Rect(x + W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)


anim_count, anim_speed, anim_limit = 0, 60, 2000
figure= deepcopy(figures[3])


def check_borders():
    if figure[i].x < 0 or figure[i].x > W - 1:
        return False
    return True

while True:
    dx = 0
    game_sc.fill(pygame.Color('black'))
    #for control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
    #move x
    figure_old = deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not check_borders():
            figure = deepcopy(figure_old)
            break

#move y
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0 
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if not check_borders():
                figure = deepcopy(figure_old)
                break    


        #draw grid
    [pygame.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid]
        #draw figure
    for i in range(4):
        figure_rect.x = figure[i].x * TILE
        figure_rect.y = figure[i].y * TILE
        pygame.draw.rect(game_sc, pygame.Color('white'), figure_rect)


    pygame.display.flip()
    clock.tick(FPS)