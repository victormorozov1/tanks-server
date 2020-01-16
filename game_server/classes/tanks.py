class Tank:
    def __init__(self, x, y, barrels, healths, speed, moving_direction='up'):  # barrels - информация о всех дулах танка.
        self.x, self.y = x, y
        self.barrels = barrels
        self.healths = healths
        self.speed = speed
        self.moving_direction = moving_direction

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y
