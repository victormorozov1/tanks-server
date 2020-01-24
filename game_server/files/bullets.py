from game_server.files.functions import *
from game_server.files.constants import *
from game_server.grpc_out import game_pb2 as game_proto


class Bullet:
    # Класс снаряда
    def __init__(self, x, y, sz, speed, moving_direction, damage, field):
        self.x = x
        self.y = y
        self.szx, self.szy = sz, sz
        self.speed = speed
        self.moving_direction = moving_direction
        self.field = field
        self.damage = damage  # У снаряда не будет поля damage если будет поле explosion
        # self.explosion = explosion
        self.healths = 100
        self.object_type = 'bullet'

    def check_for_hit_on_target(self):
        for player in self.field.players.values():
            tank = player.tank
            id = player.id
            if diff(tank.x + TANK_SZ // 2, tank.y + TANK_SZ // 2, self.x + self.szx // 2, self.y + self.szy // 2) < self.szx // 2 + TANK_SZ // 2:
                tank.healths -= self.damage
                self.healths = -1
                for i in self.field.players_healths_changing_information.keys():
                    self.field.players_healths_changing_information[i].append(
                        game_proto.HealthsChanging(id=tank.id[:2:], change=tank.healths))
                self.deleted = True

        if not self.field.map.is_free_for_bullet(self.x, self.y):
            self.deleted = True
            self.healths = -1
            # Тут ещё нужно будет понижать здоровье стены

    def move(self):
        if self.moving_direction == 'up':
            for i in range(self.speed // (CELL_SZ // 2)):
                self.y -= CELL_SZ // 2  # если будет тормозить нужно упростить этот кусок кода!!!
                self.check_for_hit_on_target()
                if self.deleted:
                    break
        elif self.moving_direction == 'down':
            for i in range(self.speed):
                self.y += CELL_SZ // 2  # если будет тормозить нужно упростить этот кусок кода!!!
                self.check_for_hit_on_target()
                if self.deleted:
                    break
        elif self.moving_direction == 'left':
            for i in range(self.speed):
                self.x -= CELL_SZ // 2  # если будет тормозить нужно упростить этот кусок кода!!!
                self.check_for_hit_on_target()
                if self.deleted:
                    break
        elif self.moving_direction == 'right':
            for i in range(self.speed):
                self.x += CELL_SZ // 2  # если будет тормозить нужно упростить этот кусок кода!!!
                self.check_for_hit_on_target()
                if self.deleted:
                    break

    def __str__(self):
        return SEPARATORS[0].join(
            [str(self.x), str(self.y)])  # Если улучшать игру то нажно будет добавить другую информацию
