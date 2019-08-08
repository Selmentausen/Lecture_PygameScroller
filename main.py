import time
import pygame as pg
import settings
import events
import entities
import physics

pg.init()

st = settings.Settings()
mc = entities.MainChar(st)
st.objs.append(mc)

platforms = [entities.Platform(st.plt_image, st.plt_image.get_rect(), i) for i in st.platforms_rect]
for platform in platforms:
    st.objs.append(platform)

enemy = entities.Enemy(st.en_image, st.en_rect, st.ens_map_rect, st.en_speed, st.en_jump_speed)
st.objs.append(enemy)

ct = time.time()
tt = 0
while True:
    pt = ct             # Past Time
    ct = time.time()    # Current Time
    dt = ct - pt        # Delta Time
    tt += dt            # Total Time

    events.keyboard_events(st, mc)

    # Updating objects and background position/velocity
    physics.velocity_restrictions([mc])
    events.update_movement([mc, enemy])
    hit_objects, collision = physics.check_collision(mc, [*platforms, enemy])
#    events.update_all(st, dt, hit_objects, collision, [mc])
    physics.update_all(st, dt, [mc])
    events.update_background(st, mc)

    st.screen.blit(st.main_map_image, [-i for i in st.main_map_pos])
    events.draw_objects(st.screen, st.main_map_pos, [mc, enemy, *platforms])
    pg.display.flip()

    time.sleep(0.016)
a