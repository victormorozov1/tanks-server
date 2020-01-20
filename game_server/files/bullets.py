from game_server.files.functions import *
from game_server.files.constants import *


class Bullet:  # В классе храняться координаты ЦЕНТРА снаряда
    # Класс снаряда
    def __init__(self, x, y, radius, speed, moving_direction, damage, field):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.moving_direction = moving_direction
        self.field = field
        self.damage = damage  # У снаряда не будет поля damage если будет поле explosion
        # self.explosion = explosion
        self.deleted = False

    def check_for_hit_on_target(self):
        for player in self.field.players.values():
            tank = player.tank
            if object_to_point_diff(tank, (self.x, self.y)) < self.radius:
                tank.healths -= self.damage
                self.deleted = True

        arr_x = [self.x - self.radius, self.x + self.radius]
        arr_y = [self.y - self.radius, self.x + self.radius]
        for x in arr_x:
            for y in arr_y:
                if not self.field.map.is_free(x, y):
                    self.deleted = True
                    # Тут ещё нужно будет понижать здоровье стены

    def move(self):
        if self.moving_direction == 'up':
            for i in range(self.speed):
                self.y -= 1  # если будет тормозить нужно упростить этот кусок кода!!!
                self.check_for_hit_on_target()
                if self.deleted:
                    break

    def __str__(self):
        return SEPARATORS[0].join([str(self.x), str(self.y)])  # Если улучшать игру то нажно будет добавить другую информацию
