def update_all(st, dt, objects):
    for obj in objects:
        hit_objects, collisions = check_collision(obj, [*st.objs])
        obj.update(st, dt, hit_objects, collisions)


def velocity_restrictions(objects):
    for obj in objects:
        if obj.velocity_x > obj.max_movement_speed:
            obj.velocity_x = obj.max_movement_speed
        elif obj.velocity_x < 0:
            obj.velocity_x = 0

        if obj.velocity_y > obj.max_falling_speed:
            obj.velocity_y = obj.max_falling_speed


def check_collision(obj, colliders):
    left_collision, right_collision, bottom_collision, top_collision = False, False, False, False
    hit_collisions = []
    hit_objects = []
    for collider in colliders:
        if collider != obj:
            if collider.rect.colliderect(obj):
                # checking main char sides for collision
                hit_objects.append(collider)
                left = obj.rect[0]
                top = obj.rect[1]
                right = obj.rect[0] + obj.rect[2]
                bottom = obj.rect[1] + obj.rect[3]

                for x in range(left, right):     # top/left > top/right, bottom/left, bottom/ right
                    if collider.rect.collidepoint([x, top]):
                        top_collision = True
                    if collider.rect.collidepoint([x, bottom]):
                        bottom_collision = True
                for y in range(top, bottom):     # top/right > bottom/right
                    if collider.rect.collidepoint([right, y]):
                        right_collision = True
                    if collider.rect.collidepoint([left, y]):
                        left_collision = True

                if top_collision is False and (bottom_collision and left_collision or right_collision):
                    if obj.rect.right - 10 < collider.rect[0]:
                        hit_collisions.append('bottom_left_edge')
                    elif obj.rect[0] + 10 > collider.rect.right:
                        hit_collisions.append('bottom_right_edge')
                    else:
                        hit_collisions.append('bottom')
                elif bottom_collision is False and (top_collision and left_collision or right_collision):
                    if obj.rect.right - 10 < collider.rect[0]:
                        hit_collisions.append('top_left_edge')
                    elif obj.rect[0] + 10 > collider.rect.right:
                        hit_collisions.append('top_right_edge')
                    else:
                        hit_collisions.append('top')
                elif left_collision is False and (right_collision and top_collision or bottom_collision):
                    hit_collisions.append('right')
                elif right_collision is False and (left_collision and top_collision or bottom_collision):
                    hit_collisions.append('left')
            right_collision, left_collision, top_collision, bottom_collision = False, False, False, False
    return hit_objects, hit_collisions
