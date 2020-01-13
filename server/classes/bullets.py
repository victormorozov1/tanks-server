class Bullet:
    # Класс снаряда
    def __init__(self, x, y, radius, speed, moving_direction, explosion):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.moving_direction = moving_direction
        self.explosion = explosion

    def move(self):
        self.x += self.moving_direction[0]
        self.y += self.moving_direction[1]
