import pygame as pg


class MainChar:
    def __init__(self, st):
        self.image = st.mc_image
        self.rect = st.mc_rect
        self.temp_rect = pg.Rect(*st.mc_rect)
        self.map_rect = st.mc_map_rect

        self.movement_speed = st.mc_speed
        self.max_movement_speed = st.mc_max_speed
        self.jump_speed = st.mc_jump_speed
        self.jump_cooldown = st.mc_jump_cooldown
        self.max_jump_count = st.mc_jump_count
        self.jump_count = self.max_jump_count
        self.max_falling_speed = st.mc_max_falling_speed

        self.friction = st.mc_friction
        self.gravity = st.mc_gravity

        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration_y = 0
        self.direction = 0

    def update(self, st, dt, hit_objects, collisions):
        for obj in hit_objects:
            if type(obj).__name__ == 'Enemy':
                self._get_hit(obj)
        self._update_velocity(st)
        self._handle_movement_restrictions(st)
        self._handle_collisions(st, collisions)
        self.jump_cooldown -= dt

    def jump(self, st):
        if self.jump_count and self.jump_cooldown <= 0:
            self.velocity_y = self.jump_speed
            self.jump_count -= 1
            self.jump_cooldown = st.mc_jump_cooldown

    def _get_hit(self, obj):
        pass

    def _update_velocity(self, st):
        keys = pg.key.get_pressed()
        if self.velocity_x > 0:
            self.velocity_x -= self.friction
        self.velocity_y += self.gravity

        if keys[st.movement_keys['forward']]:
            self.velocity_x += self.movement_speed
            self.direction = 1

        if keys[st.movement_keys['backward']]:
            self.velocity_x += self.movement_speed
            self.direction = -1
        # Velocity restriction
        if self.velocity_x > self.max_movement_speed:
            self.velocity_x = self.max_movement_speed
        elif self.velocity_x < 0:
            self.velocity_x = 0

        if self.velocity_y > self.max_falling_speed:
            self.velocity_y = self.max_falling_speed

    def _handle_movement_restrictions(self, st):
        if self.map_rect.right >= st.main_map_rect.right:
            self.map_rect.right = st.main_map_rect.right - 0.1
        elif self.map_rect.left <= 0:
            self.map_rect[0] = 0.1

    def _handle_collisions(self, st,  collisions):
        if collisions:
            for collision in collisions:
                if collision == 'bottom':
                    if self.velocity_y > 0:
                        self.jump_count = self.max_jump_count
                        self.map_rect[1] -= self.velocity_y
                        self.velocity_y = 0
                if collision == 'top':
                    if self.velocity_y < 0:
                        self.map_rect[1] -= self.velocity_y
                        self.velocity_y = 0
                if collision in ['bottom_right_edge', 'top_right_edge', 'left']:
                    if self.direction == -1:
                        if self.velocity_x > 0:
                            self.map_rect[0] += self.velocity_x
                            self.velocity_x = 0
                if collision in ['bottom_left_edge', 'top_left_edge', 'right']:
                    if self.direction == 1:
                        if self.velocity_x > 0:
                            self.map_rect[0] -= self.velocity_x
                            self.velocity_x = 0


class Enemy:
    def __init__(self, image, rect, map_rect, speed, jump_speed):
        self.image = image
        self.rect = rect
        self.map_rect = map_rect
        self.speed = speed
        self.jump_speed = jump_speed
        self.velocity_x = 2
        self.velocity_y = 0
        self.direction = 1

    def update(self):
        pass

    def _handle_movement(self):
        pass

    def _handle_collision(self):
        pass


class Platform:
    def __init__(self, image, rect, map_rect):
        self.image = image
        self.rect = rect
        self.map_rect = map_rect

