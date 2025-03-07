from client.game_client import *
from time import sleep
from client.drawing.game import Game
from client.drawing.pictures import *
from client.drawing.get_name import get_name
from random import choice


def delete_tank(id):
    my_game.field.remove_object(id)
    del tanks[id]


def player_healths_change_received(message):
    tanks[message.id].healths = message.change
    if message.change <= 0:
        if message.id == tank.id:
            my_game.running = False
        else:
            delete_tank(message.id)


def player_movement_received(message):
    id, new_x, new_y = message.id, message.new_x, message.new_y
    if id in tanks.keys():
        tanks[id].move_to(new_x, new_y)
    else:
        tanks[id] = Tank(id, choice(tank_pictures), x=new_x, y=new_y)
        my_game.field.add_object(id, tanks[id])


def player_turn_received(message):
    id, direction = message.id, message.direction
    if id in tanks.keys():
        tanks[id].turn(direction)
    else:
        print(f'ERROR: received new tank turn with id={id}')


def on_kill_received(message):
    my_game.messages.append(my_game.messages_font.render(f'{tanks[message.killer_id].name} killed {message.victim_name}', 1, (255, 255, 255)))
    if len(my_game.messages) > my_game.max_messages_size:
        my_game.messages = my_game.messages[1::]
    print(len(my_game.messages))


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
    def __init__(self, id, picture, direction='up', x=-100, y=-100, healths=100):
        self.x = x
        self.y = y
        self.id = id[:2:]
        self.direction = direction
        self.healths = healths
        self.pictures = {'up': picture,
                         'down': pygame.transform.rotate(picture, 180),
                         'right': pygame.transform.rotate(picture, -90),
                         'left': pygame.transform.rotate(picture, 90)}
        self.turn(self.direction)
        my_game.field.add_object(id, self)
        self.name = gk.get_player_name(id)

        self.font = pygame.font.Font(None, 18)
        self.text = self.font.render(self.name, 1, (255, 255, 255))

    def move_on(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def move_to(self, new_x, new_y):
        self.x, self.y = new_x, new_y

    def draw(self, win, start=(0, 0)):
        win.blit(self.picture, (self.x - start[0], self.y - start[1]))  # Отрисовка танка
        pygame.draw.rect(win, (255 - self.healths * 2, self.healths * 2, 0),  # Отрисовка линии здоровья
                         (self.x - start[0], self.y - 17 - start[1], int(CELL_SZ * self.healths / 100), 5))

        win.blit(self.text, (self.x - start[0], self.y - 12 - start[1]))

    def turn_up(self):
        self.turn('up')

    def turn_down(self):
        self.turn('down')

    def turn_left(self):
        self.turn('left')

    def turn_right(self):
        self.turn('right')

    def turn(self, direction):
        self.picture = self.pictures[direction]

    def __str__(self):
        return f'Tank(id={self.id}, x={self.x}, y={self.y}, direction={self.direction}'


class MyGame(Game):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.messages = []
        self.max_messages_size = 3
        self.messages_font = pygame.font.Font(None, 36)

    def move_tank(self, id, new_x, new_y):
        tank = my_game.field.get_object_by_id(id)
        if not tank:
            self.field.add_object(id, choice(tank_pictures), new_x, new_y)
        else:
            self.field.move_object_to(id, new_x, new_y)

    def handle_pressed(self, key):
        if key in [pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s]:
            gk.move()

    def handle_event(self, ev):
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_d:
                gk.turn('right')
            elif ev.key == pygame.K_a:
                gk.turn('left')
            elif ev.key == pygame.K_w:
                gk.turn('up')
            elif ev.key == pygame.K_s:
                gk.turn('down')
            elif ev.key == pygame.K_SPACE:
                gk.fire()

    def game_iteration(self):
        self.field.show(win, (self.szx, self.szy), start=(tank.x - self.field.szx // 2, tank.y - self.field.szy // 2))
        x = 10
        for i in range(len(self.messages)):
            y = i * 25
            win.blit(self.messages[i], (x, y))
        pygame.display.update()


def start_game(win):
    global my_game, gk, tanks, tank

    tanks = dict()

    gk = GameClient()

    x, y, direction = gk.connect(name=name)
    while not gk.connected:  # Вроде этот while можно убрать
        sleep(0.1)

    field_arr = gk.get_map()

    field_dict = dict()
    field_dict['#'] = box_pict
    field_dict['@'] = bush_pict
    field_dict['*'] = river_pict

    my_game = MyGame(SZX, SZY, win, sleep=0.01, cell_field_sz=CELL_SZ, bg=(0, 0, 0),
                     field='cell field',
                     field_arr=field_arr,
                     field_dict=field_dict)

    tank = Tank(gk.id, choice(tank_pictures), x=x, y=y, direction=direction)
    tanks[tank.id] = tank

    print('my id =', gk.id)

    for i in gk.get_all_players():
        if i[0] != tank.id:
            tanks[i[0]] = Tank(i[0], choice(tank_pictures), x=i[1], y=i[2], healths=i[3])
        print(tanks[i[0]])

    gk.start_listening_for_players_movements(player_movement_received)
    gk.start_listening_for_players_turns(player_turn_received)
    gk.start_listening_for_bullets_positions(bullets_received)
    gk.start_listening_for_healths_changing(player_healths_change_received)
    gk.start_listening_for_kills(on_kill_received)

    tank.draw(win, start=(tank.x - my_game.field.szx // 2, tank.y - my_game.field.szy // 2))

    return my_game.run()


if __name__ == '__main__':
    global name
    pygame.init()
    win = pygame.display.set_mode((SZX, SZY), pygame.RESIZABLE)

    win.blit(choice(savers), (0, 0))
    name = get_name(win, 5, (SZX // 2 - 30, SZY // 2))

    if name:
        while not start_game(win):
            sleep(1)

