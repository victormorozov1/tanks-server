from functions import *


# Данный файл содржит класс взрыва.
# Взрыв появляется после попадание снаряда в цель.


class Explosion:
    # Класс базового взрыва.
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


class SmallExplosion(Explosion):
    # Базовый класс обычного взрыва.
    # Имеет маленькие размеры, таким образом действует только на один объект в который попал.
    def __init__(self, x, y, damage):
        super().__init__(x, y, 2)
        self.damage = damage


class SniperExplosion(SmallExplosion):
    # Класс снайперского взрыва.
    def __init__(self, x, y):
        super().__init__(x, y, 100)


class SimpleExplosion(SmallExplosion):
    # Класс обычного взрыва.
    def __init__(self, x, y):
        super().__init__(x, y, 20)


class BigExplosion(Explosion):
    # Класс большого взрыва.
    # Особенность - большой урон в центре и маленький по краям.
    def __init__(self, x, y, center_damage, last_damage):
        super().__init__(x, y, 20)
        self.center_damage = center_damage
        self.last_damage = last_damage

    def get_damage(self, object):
        d = object_to_point_diff(object, (self.x, self.y))
        if d > self.radius:
            return 0
        return d / self.radius * (self.center_damage - self.last_damage) + self.center_damage


class BombExplosion(BigExplosion):
    # Класс взрыва BombBullet
    def __init__(self, x, y):
        super().__init__(x, y, 50, 5)


class ConsequenceExplosion(Explosion):
    # Класс взрыва, который оставляет такну некоторый эффект. Например заморозку.
    def __init__(self, x, y, damage, time, effect):
        super().__init__(x, y, 20)
        self.x = x
        self.y = y
        self.time = time  # time - количество игровых итераций, которое
        # поражённый танк будет подвергаться воздействию эффекта.
        self.effect = effect
        self.damage = damage


class FreezeExplosion(ConsequenceExplosion):
    # Класс замораживающего взрыва
    def __init__(self, x, y):
        super().__init__(x, y, 15, 16, 'freeze')


class FireExplosion(ConsequenceExplosion):
    # Класс сжигающего взрыва
    def __init__(self, x, y):
        super().__init__(x, y, 15, 16, 'fire')
