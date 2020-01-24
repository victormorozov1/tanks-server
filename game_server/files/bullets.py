from game_server.files.functions import *
from game_server.files.constants import *
from game_server.grpc_out import game_pb2 as game_proto


class Bullet:
    # Класс снаряда
    def __init__(self, x, y, sz, speed, direction, damage, field, id):
        self.x = x
        self.y = y
        self.szx, self.szy = sz, sz
        self.speed = speed
        self.direction = direction
        self.field = field
        self.damage = damage  # У снаряда не будет поля damage если будет поле explosion
        # self.explosion = explosion
        self.healths = 100
        self.object_type = 'bullet'
        self.id = id

    def check_for_hit_on_target(self):
        for tank in self.field.objects.values():
            id = tank.id
            if diff(tank.x + TANK_SZ // 2, tank.y + TANK_SZ // 2, self.x + self.szx // 2, self.y + self.szy // 2) < self.szx // 2 + TANK_SZ // 2:
                tank.healths -= self.damage
                self.healths = -1
                for i in self.field.players_healths_changing_information.keys():
                    self.field.players_healths_changing_information[i].append(
                        game_proto.HealthsChanging(id=tank.id[:2:], change=tank.healths))

        if not self.field.map.is_free_for_bullet(self.x, self.y):
            self.healths = -1
            print('bullet healths = -1', self.id)
            # Тут ещё нужно будет понижать здоровье стены

    def move(self):
        if self.direction == 'up':
            for i in range(self.speed):
                self.y -= 1  # если будет тормозить нужно упростить этот кусок кода!!!
                self.check_for_hit_on_target()
                if self.healths <= 0:
                    return
        elif self.direction == 'down':
            for i in range(self.speed):
                self.y += 1  # если будет тормозить нужно упростить этот кусок кода!!!
                self.check_for_hit_on_target()
                if self.healths <= 0:
                    return
        elif self.direction == 'left':
            for i in range(self.speed):
                self.x -= 1  # если будет тормозить нужно упростить этот кусок кода!!!
                self.check_for_hit_on_target()
                if self.healths <= 0:
                    return
        elif self.direction == 'right':
            for i in range(self.speed):
                self.x += 1  # если будет тормозить нужно упростить этот кусок кода!!!
                self.check_for_hit_on_target()
                if self.healths <= 0:
                    return

    def __str__(self):
        return SEPARATORS[0].join(
            [str(self.x), str(self.y)])  # Если улучшать игру то нажно будет добавить другую информацию
