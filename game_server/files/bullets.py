from game_server.files.functions import *
from game_server.files.constants import *
from game_server.grpc_out import game_pb2 as game_proto


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
            if diff(tank.x + TANK_SZ // 2, tank.y + TANK_SZ // 2, self.x, self.y) < self.radius + TANK_SZ // 2:
                tank.healths -= self.damage
                for i in self.field.players_healths_changing_information.keys():
                    self.field.players_healths_changing_information[i].append(
                        game_proto.HealthsChanging(id=i[:2:], change=-self.damage))
                self.deleted = True

        if not self.field.map.is_free(self.x, self.y):
            self.deleted = True
            # Тут ещё нужно будет понижать здоровье стены

    def move(self):
        if self.moving_direction == 'up':
            for i in range(self.speed):
                self.y -= 1  # если будет тормозить нужно упростить этот кусок кода!!!
                self.check_for_hit_on_target()
                if self.deleted:
                    break
        elif self.moving_direction == 'down':
            for i in range(self.speed):
                self.y += 1  # если будет тормозить нужно упростить этот кусок кода!!!
                self.check_for_hit_on_target()
                if self.deleted:
                    break
        elif self.moving_direction == 'left':
            for i in range(self.speed):
                self.x -= 1  # если будет тормозить нужно упростить этот кусок кода!!!
                self.check_for_hit_on_target()
                if self.deleted:
                    break
        elif self.moving_direction == 'right':
            for i in range(self.speed):
                self.x += 1  # если будет тормозить нужно упростить этот кусок кода!!!
                self.check_for_hit_on_target()
                if self.deleted:
                    break

    def __str__(self):
        return SEPARATORS[0].join(
            [str(self.x), str(self.y)])  # Если улучшать игру то нажно будет добавить другую информацию
