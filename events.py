import sys
import pygame as pg


def keyboard_events(st, mc):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == st.quit_key:
                sys.exit()
            elif event.key == st.movement_keys['jump']:
                mc.jump(st)


def update_all(st, dt, hit_objects, collisions, objects):
    for obj in objects:
        obj.update(st, dt, hit_objects, collisions)


def update_movement(objects):
    for obj in objects:
        if obj.velocity_x or obj.velocity_y:
            obj.map_rect = obj.map_rect.move([obj.velocity_x * obj.direction, obj.velocity_y])


def update_background(st, mc):
    if st.width / 2 <= mc.map_rect[0] <= (st.main_map_rect.right - st.width / 2):
        st.main_map_pos[0] = mc.map_rect[0] - st.width / 2


def draw_objects(screen, screen_pos, objects):
    for obj in objects:
        obj.rect[0], obj.rect[1] = obj.map_rect[0] - screen_pos[0], obj.map_rect[1] - screen_pos[1]
        screen.blit(obj.image, (obj.rect[0], obj.rect[1]))


