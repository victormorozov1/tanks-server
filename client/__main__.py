import pygame, os
from client.game_client import *
from time import sleep
from client.drawing.game import Game
import pygame
from client.drawing.constants import *
from client.drawing.pictures import *


def delete_tank(id):
    my_game.field.remove_object(id)
    del tanks[id]


def player_healts_change_received(message):
    print('----')
    for id, tank in tanks.items():
        print(id)
    print('----')
    tanks[message.id].healths = message.change
    if message.change <= 0:
        print('deleteng tank wiht id =', message.id)
        delete_tank(message.id)
        print('--2--')
        for id, tank in tanks.items():
            print(id)
        print('--2--')


def player_movement_received(message):
    id, new_x, new_y = message.id, message.new_x, message.new_y
    if id in tanks.keys():
        tanks[id].move_to(new_x, new_y)
    else:
        field_object = my_game.field.add_object(id, tank_pict, new_x, new_y)
        tanks[id] = Tank(id, field_object, x=new_x, y=new_y)


def player_turn_received(message):
    id, direction = message.id, message.direction
    if id in tanks.keys():
        tanks[id].turn(direction)
    else:
        print(f'ERROR: received new tank turn with id={id}')


def bullets_received(message):
    my_game.field.bullets = []
    rec = 0
    for i in message.s.split(SEPARATORS[1]):
        rec += 1
        try:
            x, y = [int(j) for j in i.split(SEPARATORS[0])]
            my_game.field.bullets.append((x, y))
        except BaseException:
            pass


class Tank:
    def __init__(self, id, field_object, direction='up', x=-100, y=-100, healths=100):
        self.field_object = field_object
        self.field_object.x = x
        self.field_object.y = y
        self.id = id[:2:]
        self.direction = direction
        self.healths = healths

    def move_on(self, move_x, move_y):
        self.field_object.rect.x += move_x
        self.field_object.rect.y += move_y

    def move_to(self, new_x, new_y):
        self.field_object.rect.x, self.field_object.rect.y = new_x, new_y

    def turn_up(self):
        self.turn('up')

    def turn_down(self):
        self.turn('down')

    def turn_left(self):
        self.turn('left')

    def turn_right(self):
        self.turn('right')

    def turn(self, direction):
        self.direction = direction
        self.field_object.turn(direction)


class MyGame(Game):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def move_tank(self, id, new_x, new_y):
        tank = my_game.field.get_object_by_id(id)
        if not tank:
            self.field.add_object(id, tank_pict, new_x, new_y)
        else:
            self.field.move_object_to(id, new_x, new_y)

    def handle_pressed(self, key):
        if key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
            gk.move()

    def handle_event(self, ev):
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RIGHT:
                gk.turn('right')
            elif ev.key == pygame.K_LEFT:
                gk.turn('left')
            elif ev.key == pygame.K_UP:
                gk.turn('up')
            elif ev.key == pygame.K_DOWN:
                gk.turn('down')
            elif ev.key == pygame.K_SPACE:
                gk.fire()

    def game_iteration(self):
        self.field.show(self.field.win, (self.szx, self.szy), start=(tank.field_object.rect.x - self.field.szx // 2, tank.field_object.rect.y - self.field.szy // 2))


if __name__ == '__main__':
    global mar_id, tanks_sprite_group, my_game

    tanks = dict()
    bullets = []

    gk = GameClient()
    x, y, direction = gk.connect()
    while not gk.connected:  # Вроде этот while можно убрать
        sleep(0.1)

    field_arr = gk.get_map()

    field_dict = dict()
    field_dict[10] = load_picture('box.png')

    pygame.init()
    display_size = pygame.display.Info()
    my_game = MyGame(display_size.current_w, display_size.current_h, sleep=0.001, cell_field_sz=CELL_SZ, bg=(122, 233, 111),
                     field='cell field',
                     field_arr=field_arr,
                     field_dict=field_dict)

    tank = Tank(gk.id, my_game.field.add_object(gk.id[:2:], tank_pict, x, y))

    for i in gk.get_all_players():
        if i[0] != tank.id:
            tanks[i[0]] = Tank(i[0], my_game.field.add_object(i[0], tank_pict, i[1], i[2]), x=i[1], y=i[2])

    gk.start_listening_for_players_movements(player_movement_received)
    gk.start_listening_for_players_turns(player_turn_received)
    gk.start_listening_for_bullets_positions(bullets_received)
    gk.start_listening_for_healths_changing(player_healts_change_received)

    tanks[tank.id] = tank

    my_game.run()

