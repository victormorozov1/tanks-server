class Tank:
    def __init__(self, x, y, barrels, healths, speed):  # barrels - информация о всех дулах танка.
        self.x, self.y = x, y
        self.barrels = barrels
        self.healths = healths
        self.speed = speed
