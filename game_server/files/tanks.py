from game_server.files.constants import *
from game_server.files.bullets import *
from game_server.grpc_out import game_pb2 as game_proto


class Tank:
    def __init__(self, x, y, healths, speed, field, id, name, direction='up', szx=TANK_SZ, szy=TANK_SZ):
        self.x, self.y = x, y
        self.healths = healths
        # self.burrels = burrels
        # barrels - информация о всех дулах танка.
        self.speed = speed
        self.direction = direction
        self.field = field
        self.id = id[:2:]
        self.num_fired_bullets = 0
        self.szx, self.szy = szx, szy
        self.field.add_object(self)
        self.object_type = 'tank'
        self.is_moving = False
        self.name = name
        self.password = id

    def move_on_one_pixel(self):
        global new_x, new_y
        new_x, new_y = self.x, self.y
        if self.direction == 'up':
            new_y = self.y - 1
        elif self.direction == 'down':
            new_y = self.y + 1
        elif self.direction == 'left':
            new_x = self.x - 1
        elif self.direction == 'right':
            new_x = self.x + 1
        if self.field.free(new_x, new_y, CELL_SZ, ignore=[self]):
            self.x, self.y = new_x, new_y

    def move(self):
        if self.is_moving:
            for i in range(self.speed):
                self.move_on_one_pixel()
            self.is_moving = False
            for i in self.field.player_movements_information.keys():
                self.field.player_movements_information[i].append(
                    game_proto.PlayerMovement(id=self.id, new_x=self.x, new_y=self.y))

    def fire(self):
        self.num_fired_bullets += 1
        global x, y
        if self.direction == 'left':
            x = self.x - BULLET_INDENT
        elif self.direction == 'up' or self.direction == 'down':
            x = self.x + TANK_SZ // 2
        else:
            x = self.x + TANK_SZ + BULLET_INDENT

        if self.direction == 'up':
            y = self.y - BULLET_INDENT
        elif self.direction == 'left' or self.direction == 'right':
            y = self.y + TANK_SZ // 2
        else:
            y = self.y + TANK_SZ + BULLET_INDENT

        self.field.bullets[self.id + str(self.num_fired_bullets)] = (
            Bullet(x, y, BULLET_RADIUS, BULLET_SPEED, self.direction, BULLET_DAMAGE, self.field))

    def __str__(self):
        return str(self.id) + SEPARATORS[0] + str(self.x) + SEPARATORS[0] + str(self.y)
