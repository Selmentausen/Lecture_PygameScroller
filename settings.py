import pygame as pg


class Settings:
    def __init__(self):
        # screen settings
        self.width = 1024
        self.height = 768
        self.resolution = (self.width, self.height)
        self.screen = pg.display.set_mode(self.resolution)

        self.objs = []

        # Main character settings
        self.mc_image = pg.image.load('images/main_char.png').convert()
        self.mc_rect = self.mc_image.get_rect()
        self.mc_map_rect = self.mc_image.get_rect()
        self.mc_friction = 2
        self.mc_gravity = 0.25
        self.mc_speed = 5
        self.mc_max_speed = 8
        self.mc_max_falling_speed = 10
        self.mc_jump_speed = -7
        self.mc_jump_cooldown = 0.2
        self.mc_jump_count = 2

        # Enemy Settings
        self.en_image = pg.image.load('images/enemy.png').convert()
        self.en_rect = self.en_image.get_rect()
        self.ens_map_rect = pg.Rect(200, 350, self.en_image.get_width(), self.en_image.get_height())
        self.en_friction = 0
        self.en_gravity = 0
        self.en_speed = 0
        self.en_max_speed = 0
        self.en_max_falling_speed = 0
        self.en_jump_speed = 0
        self.en_jump_cooldown = 0

        # Platform settings
        self.plt_image = pg.image.load('images/platform.png').convert()
        self.plt_rect = self.plt_image.get_rect()
        self.platforms_rect = [pg.Rect(0, 600, self.plt_image.get_width(), self.plt_image.get_height()),
                               pg.Rect(370, 600, self.plt_image.get_width(), self.plt_image.get_height()),
                               pg.Rect(740, 600, self.plt_image.get_width(), self.plt_image.get_height()),
                               pg.Rect(1110, 600, self.plt_image.get_width(), self.plt_image.get_height())]

        # images/background settings
        self.main_map_image = pg.image.load('images/background0.png').convert()
        self.main_map_rect = self.main_map_image.get_rect()
        self.main_map_pos = [0, 0]

        # input keys
        self.quit_key = pg.K_ESCAPE
        self.movement_keys = {'forward': pg.K_d, 'backward': pg.K_a, 'boost': pg.K_v,
                              'down': pg.K_s, 'up': pg.K_w, 'jump': pg.K_SPACE}

