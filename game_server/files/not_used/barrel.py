class Barrel:
    def __init__(self, x, y, attachment_point, bullet):
        self.x = x  # (x, y) - координаты конца дула относительно левого верхнего угла танка
        self.y = y
        self.attachment_point = attachment_point  # место крепления дула к танку: left, up, right или down
        self.bullet = bullet
